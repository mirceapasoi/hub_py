from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
ID_REGISTRY_EVENT_TYPE_NONE: IdRegistryEventType
ID_REGISTRY_EVENT_TYPE_REGISTER: IdRegistryEventType
ID_REGISTRY_EVENT_TYPE_TRANSFER: IdRegistryEventType

class IdRegistryEvent(_message.Message):
    __slots__ = ["block_hash", "block_number", "fid", "log_index", "to", "transaction_hash", "type"]
    BLOCK_HASH_FIELD_NUMBER: _ClassVar[int]
    BLOCK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    FID_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    LOG_INDEX_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_HASH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    block_hash: bytes
    block_number: int
    fid: int
    log_index: int
    to: bytes
    transaction_hash: bytes
    type: IdRegistryEventType
    def __init__(self, block_number: _Optional[int] = ..., block_hash: _Optional[bytes] = ..., transaction_hash: _Optional[bytes] = ..., log_index: _Optional[int] = ..., fid: _Optional[int] = ..., to: _Optional[bytes] = ..., type: _Optional[_Union[IdRegistryEventType, str]] = ..., **kwargs) -> None: ...

class IdRegistryEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
