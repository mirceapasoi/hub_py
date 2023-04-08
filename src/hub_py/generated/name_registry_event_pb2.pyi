from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
NAME_REGISTRY_EVENT_TYPE_NONE: NameRegistryEventType
NAME_REGISTRY_EVENT_TYPE_RENEW: NameRegistryEventType
NAME_REGISTRY_EVENT_TYPE_TRANSFER: NameRegistryEventType

class NameRegistryEvent(_message.Message):
    __slots__ = ["block_hash", "block_number", "expiry", "fname", "log_index", "to", "transaction_hash", "type"]
    BLOCK_HASH_FIELD_NUMBER: _ClassVar[int]
    BLOCK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_FIELD_NUMBER: _ClassVar[int]
    FNAME_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    LOG_INDEX_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_HASH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    block_hash: bytes
    block_number: int
    expiry: int
    fname: bytes
    log_index: int
    to: bytes
    transaction_hash: bytes
    type: NameRegistryEventType
    def __init__(self, block_number: _Optional[int] = ..., block_hash: _Optional[bytes] = ..., transaction_hash: _Optional[bytes] = ..., log_index: _Optional[int] = ..., fname: _Optional[bytes] = ..., to: _Optional[bytes] = ..., type: _Optional[_Union[NameRegistryEventType, str]] = ..., expiry: _Optional[int] = ..., **kwargs) -> None: ...

class NameRegistryEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
