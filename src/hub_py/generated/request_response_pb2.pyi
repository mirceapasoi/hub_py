import message_pb2 as _message_pb2
import hub_event_pb2 as _hub_event_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CastsByParentRequest(_message.Message):
    __slots__ = ["cast_id", "page_size", "page_token", "reverse"]
    CAST_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REVERSE_FIELD_NUMBER: _ClassVar[int]
    cast_id: _message_pb2.CastId
    page_size: int
    page_token: bytes
    reverse: bool
    def __init__(self, cast_id: _Optional[_Union[_message_pb2.CastId, _Mapping]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[bytes] = ..., reverse: bool = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class EventRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class FidRequest(_message.Message):
    __slots__ = ["fid", "page_size", "page_token", "reverse"]
    FID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REVERSE_FIELD_NUMBER: _ClassVar[int]
    fid: int
    page_size: int
    page_token: bytes
    reverse: bool
    def __init__(self, fid: _Optional[int] = ..., page_size: _Optional[int] = ..., page_token: _Optional[bytes] = ..., reverse: bool = ...) -> None: ...

class FidsRequest(_message.Message):
    __slots__ = ["page_size", "page_token", "reverse"]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REVERSE_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: bytes
    reverse: bool
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[bytes] = ..., reverse: bool = ...) -> None: ...

class FidsResponse(_message.Message):
    __slots__ = ["fids", "next_page_token"]
    FIDS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    fids: _containers.RepeatedScalarFieldContainer[int]
    next_page_token: bytes
    def __init__(self, fids: _Optional[_Iterable[int]] = ..., next_page_token: _Optional[bytes] = ...) -> None: ...

class HubInfoResponse(_message.Message):
    __slots__ = ["is_synced", "nickname", "root_hash", "version"]
    IS_SYNCED_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    ROOT_HASH_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    is_synced: bool
    nickname: str
    root_hash: str
    version: str
    def __init__(self, version: _Optional[str] = ..., is_synced: bool = ..., nickname: _Optional[str] = ..., root_hash: _Optional[str] = ...) -> None: ...

class IdRegistryEventByAddressRequest(_message.Message):
    __slots__ = ["address"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: bytes
    def __init__(self, address: _Optional[bytes] = ...) -> None: ...

class IdRegistryEventRequest(_message.Message):
    __slots__ = ["fid"]
    FID_FIELD_NUMBER: _ClassVar[int]
    fid: int
    def __init__(self, fid: _Optional[int] = ...) -> None: ...

class MessagesResponse(_message.Message):
    __slots__ = ["messages", "next_page_token"]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[_message_pb2.Message]
    next_page_token: bytes
    def __init__(self, messages: _Optional[_Iterable[_Union[_message_pb2.Message, _Mapping]]] = ..., next_page_token: _Optional[bytes] = ...) -> None: ...

class NameRegistryEventRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: bytes
    def __init__(self, name: _Optional[bytes] = ...) -> None: ...

class ReactionRequest(_message.Message):
    __slots__ = ["cast_id", "fid", "reaction_type"]
    CAST_ID_FIELD_NUMBER: _ClassVar[int]
    FID_FIELD_NUMBER: _ClassVar[int]
    REACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    cast_id: _message_pb2.CastId
    fid: int
    reaction_type: _message_pb2.ReactionType
    def __init__(self, fid: _Optional[int] = ..., reaction_type: _Optional[_Union[_message_pb2.ReactionType, str]] = ..., cast_id: _Optional[_Union[_message_pb2.CastId, _Mapping]] = ...) -> None: ...

class ReactionsByCastRequest(_message.Message):
    __slots__ = ["cast_id", "page_size", "page_token", "reaction_type", "reverse"]
    CAST_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    REVERSE_FIELD_NUMBER: _ClassVar[int]
    cast_id: _message_pb2.CastId
    page_size: int
    page_token: bytes
    reaction_type: _message_pb2.ReactionType
    reverse: bool
    def __init__(self, cast_id: _Optional[_Union[_message_pb2.CastId, _Mapping]] = ..., reaction_type: _Optional[_Union[_message_pb2.ReactionType, str]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[bytes] = ..., reverse: bool = ...) -> None: ...

class ReactionsByFidRequest(_message.Message):
    __slots__ = ["fid", "page_size", "page_token", "reaction_type", "reverse"]
    FID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    REVERSE_FIELD_NUMBER: _ClassVar[int]
    fid: int
    page_size: int
    page_token: bytes
    reaction_type: _message_pb2.ReactionType
    reverse: bool
    def __init__(self, fid: _Optional[int] = ..., reaction_type: _Optional[_Union[_message_pb2.ReactionType, str]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[bytes] = ..., reverse: bool = ...) -> None: ...

class SignerRequest(_message.Message):
    __slots__ = ["fid", "signer"]
    FID_FIELD_NUMBER: _ClassVar[int]
    SIGNER_FIELD_NUMBER: _ClassVar[int]
    fid: int
    signer: bytes
    def __init__(self, fid: _Optional[int] = ..., signer: _Optional[bytes] = ...) -> None: ...

class SubscribeRequest(_message.Message):
    __slots__ = ["event_types", "from_id"]
    EVENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    FROM_ID_FIELD_NUMBER: _ClassVar[int]
    event_types: _containers.RepeatedScalarFieldContainer[_hub_event_pb2.HubEventType]
    from_id: int
    def __init__(self, event_types: _Optional[_Iterable[_Union[_hub_event_pb2.HubEventType, str]]] = ..., from_id: _Optional[int] = ...) -> None: ...

class SyncIds(_message.Message):
    __slots__ = ["sync_ids"]
    SYNC_IDS_FIELD_NUMBER: _ClassVar[int]
    sync_ids: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, sync_ids: _Optional[_Iterable[bytes]] = ...) -> None: ...

class TrieNodeMetadataResponse(_message.Message):
    __slots__ = ["children", "hash", "num_messages", "prefix"]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    NUM_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    children: _containers.RepeatedCompositeFieldContainer[TrieNodeMetadataResponse]
    hash: str
    num_messages: int
    prefix: bytes
    def __init__(self, prefix: _Optional[bytes] = ..., num_messages: _Optional[int] = ..., hash: _Optional[str] = ..., children: _Optional[_Iterable[_Union[TrieNodeMetadataResponse, _Mapping]]] = ...) -> None: ...

class TrieNodePrefix(_message.Message):
    __slots__ = ["prefix"]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    prefix: bytes
    def __init__(self, prefix: _Optional[bytes] = ...) -> None: ...

class TrieNodeSnapshotResponse(_message.Message):
    __slots__ = ["excluded_hashes", "num_messages", "prefix", "root_hash"]
    EXCLUDED_HASHES_FIELD_NUMBER: _ClassVar[int]
    NUM_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    ROOT_HASH_FIELD_NUMBER: _ClassVar[int]
    excluded_hashes: _containers.RepeatedScalarFieldContainer[str]
    num_messages: int
    prefix: bytes
    root_hash: str
    def __init__(self, prefix: _Optional[bytes] = ..., excluded_hashes: _Optional[_Iterable[str]] = ..., num_messages: _Optional[int] = ..., root_hash: _Optional[str] = ...) -> None: ...

class UserDataRequest(_message.Message):
    __slots__ = ["fid", "user_data_type"]
    FID_FIELD_NUMBER: _ClassVar[int]
    USER_DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    fid: int
    user_data_type: _message_pb2.UserDataType
    def __init__(self, fid: _Optional[int] = ..., user_data_type: _Optional[_Union[_message_pb2.UserDataType, str]] = ...) -> None: ...

class VerificationRequest(_message.Message):
    __slots__ = ["address", "fid"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    FID_FIELD_NUMBER: _ClassVar[int]
    address: bytes
    fid: int
    def __init__(self, fid: _Optional[int] = ..., address: _Optional[bytes] = ...) -> None: ...
