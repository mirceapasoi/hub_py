import message_pb2 as _message_pb2
import id_registry_event_pb2 as _id_registry_event_pb2
import name_registry_event_pb2 as _name_registry_event_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
HUB_EVENT_TYPE_MERGE_ID_REGISTRY_EVENT: HubEventType
HUB_EVENT_TYPE_MERGE_MESSAGE: HubEventType
HUB_EVENT_TYPE_MERGE_NAME_REGISTRY_EVENT: HubEventType
HUB_EVENT_TYPE_NONE: HubEventType
HUB_EVENT_TYPE_PRUNE_MESSAGE: HubEventType
HUB_EVENT_TYPE_REVOKE_MESSAGE: HubEventType

class HubEvent(_message.Message):
    __slots__ = ["id", "merge_id_registry_event_body", "merge_message_body", "merge_name_registry_event_body", "prune_message_body", "revoke_message_body", "type"]
    ID_FIELD_NUMBER: _ClassVar[int]
    MERGE_ID_REGISTRY_EVENT_BODY_FIELD_NUMBER: _ClassVar[int]
    MERGE_MESSAGE_BODY_FIELD_NUMBER: _ClassVar[int]
    MERGE_NAME_REGISTRY_EVENT_BODY_FIELD_NUMBER: _ClassVar[int]
    PRUNE_MESSAGE_BODY_FIELD_NUMBER: _ClassVar[int]
    REVOKE_MESSAGE_BODY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    merge_id_registry_event_body: MergeIdRegistryEventBody
    merge_message_body: MergeMessageBody
    merge_name_registry_event_body: MergeNameRegistryEventBody
    prune_message_body: PruneMessageBody
    revoke_message_body: RevokeMessageBody
    type: HubEventType
    def __init__(self, type: _Optional[_Union[HubEventType, str]] = ..., id: _Optional[int] = ..., merge_message_body: _Optional[_Union[MergeMessageBody, _Mapping]] = ..., prune_message_body: _Optional[_Union[PruneMessageBody, _Mapping]] = ..., revoke_message_body: _Optional[_Union[RevokeMessageBody, _Mapping]] = ..., merge_id_registry_event_body: _Optional[_Union[MergeIdRegistryEventBody, _Mapping]] = ..., merge_name_registry_event_body: _Optional[_Union[MergeNameRegistryEventBody, _Mapping]] = ...) -> None: ...

class MergeIdRegistryEventBody(_message.Message):
    __slots__ = ["id_registry_event"]
    ID_REGISTRY_EVENT_FIELD_NUMBER: _ClassVar[int]
    id_registry_event: _id_registry_event_pb2.IdRegistryEvent
    def __init__(self, id_registry_event: _Optional[_Union[_id_registry_event_pb2.IdRegistryEvent, _Mapping]] = ...) -> None: ...

class MergeMessageBody(_message.Message):
    __slots__ = ["deleted_messages", "message"]
    DELETED_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    deleted_messages: _containers.RepeatedCompositeFieldContainer[_message_pb2.Message]
    message: _message_pb2.Message
    def __init__(self, message: _Optional[_Union[_message_pb2.Message, _Mapping]] = ..., deleted_messages: _Optional[_Iterable[_Union[_message_pb2.Message, _Mapping]]] = ...) -> None: ...

class MergeNameRegistryEventBody(_message.Message):
    __slots__ = ["name_registry_event"]
    NAME_REGISTRY_EVENT_FIELD_NUMBER: _ClassVar[int]
    name_registry_event: _name_registry_event_pb2.NameRegistryEvent
    def __init__(self, name_registry_event: _Optional[_Union[_name_registry_event_pb2.NameRegistryEvent, _Mapping]] = ...) -> None: ...

class PruneMessageBody(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: _message_pb2.Message
    def __init__(self, message: _Optional[_Union[_message_pb2.Message, _Mapping]] = ...) -> None: ...

class RevokeMessageBody(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: _message_pb2.Message
    def __init__(self, message: _Optional[_Union[_message_pb2.Message, _Mapping]] = ...) -> None: ...

class HubEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
