from io import BytesIO

from google.protobuf.message import Message
from google.protobuf.descriptor import FieldDescriptor


def patched_serialize_to_string(message: Message, deterministic: bool = True) -> bytes:
    out = BytesIO()
    descriptor = message.DESCRIPTOR
    if descriptor.GetOptions().map_entry:
        # Fields of map entry should always be serialized.
        descriptor.fields_by_name["key"]._encoder(out.write, message.key, deterministic)
        descriptor.fields_by_name["value"]._encoder(
            out.write, message.value, deterministic
        )
    else:
        for field_descriptor, field_value in message.ListFields():
            # This is a horrible hack due to serialization differences from ts-proto
            # https://github.com/farcasterxyz/hub-monorepo/issues/757 for details
            # The only message in Farcaster with int arrays is CastAddBody, so we patch
            # serialization only for that field
            if field_descriptor.name == "cast_add_body":

                def is_present(item: FieldDescriptor) -> bool:
                    if item[0].label == FieldDescriptor.LABEL_REPEATED:
                        # Force empty int arrays to be included in serialization
                        if item[0].type in (
                            FieldDescriptor.TYPE_INT64,
                            FieldDescriptor.TYPE_INT32,
                            FieldDescriptor.TYPE_UINT64,
                            FieldDescriptor.TYPE_UINT32,
                        ):
                            return True
                        return bool(item[1])
                    elif item[0].cpp_type == FieldDescriptor.CPPTYPE_MESSAGE:
                        return item[1]._is_present_in_parent
                    else:
                        return True

                def patched_list_fields(self):
                    all_fields = [
                        item for item in self._fields.items() if is_present(item)
                    ]
                    all_fields.sort(key=lambda item: item[0].number)
                    return all_fields

                field_value.__class__.ListFields = patched_list_fields
            field_descriptor._encoder(out.write, field_value, deterministic)
        for tag_bytes, value_bytes in message._unknown_fields:
            out.write(tag_bytes)
            out.write(value_bytes)
    return out.getvalue()
