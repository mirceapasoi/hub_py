from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
FARCASTER_NETWORK_DEVNET: FarcasterNetwork
FARCASTER_NETWORK_MAINNET: FarcasterNetwork
FARCASTER_NETWORK_NONE: FarcasterNetwork
FARCASTER_NETWORK_TESTNET: FarcasterNetwork
HASH_SCHEME_BLAKE3: HashScheme
HASH_SCHEME_NONE: HashScheme
MESSAGE_TYPE_CAST_ADD: MessageType
MESSAGE_TYPE_CAST_REMOVE: MessageType
MESSAGE_TYPE_LINK_ADD: MessageType
MESSAGE_TYPE_LINK_REMOVE: MessageType
MESSAGE_TYPE_NONE: MessageType
MESSAGE_TYPE_REACTION_ADD: MessageType
MESSAGE_TYPE_REACTION_REMOVE: MessageType
MESSAGE_TYPE_SIGNER_ADD: MessageType
MESSAGE_TYPE_SIGNER_REMOVE: MessageType
MESSAGE_TYPE_USER_DATA_ADD: MessageType
MESSAGE_TYPE_VERIFICATION_ADD_ETH_ADDRESS: MessageType
MESSAGE_TYPE_VERIFICATION_REMOVE: MessageType
REACTION_TYPE_LIKE: ReactionType
REACTION_TYPE_NONE: ReactionType
REACTION_TYPE_RECAST: ReactionType
SIGNATURE_SCHEME_ED25519: SignatureScheme
SIGNATURE_SCHEME_EIP712: SignatureScheme
SIGNATURE_SCHEME_NONE: SignatureScheme
USER_DATA_TYPE_BIO: UserDataType
USER_DATA_TYPE_DISPLAY: UserDataType
USER_DATA_TYPE_FNAME: UserDataType
USER_DATA_TYPE_NONE: UserDataType
USER_DATA_TYPE_PFP: UserDataType
USER_DATA_TYPE_URL: UserDataType

class CastAddBody(_message.Message):
    __slots__ = ["embeds", "embeds_deprecated", "mentions", "mentions_positions", "parent_cast_id", "parent_url", "text"]
    EMBEDS_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    EMBEDS_FIELD_NUMBER: _ClassVar[int]
    MENTIONS_FIELD_NUMBER: _ClassVar[int]
    MENTIONS_POSITIONS_FIELD_NUMBER: _ClassVar[int]
    PARENT_CAST_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_URL_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    embeds: _containers.RepeatedCompositeFieldContainer[Embed]
    embeds_deprecated: _containers.RepeatedScalarFieldContainer[str]
    mentions: _containers.RepeatedScalarFieldContainer[int]
    mentions_positions: _containers.RepeatedScalarFieldContainer[int]
    parent_cast_id: CastId
    parent_url: str
    text: str
    def __init__(self, embeds_deprecated: _Optional[_Iterable[str]] = ..., mentions: _Optional[_Iterable[int]] = ..., parent_cast_id: _Optional[_Union[CastId, _Mapping]] = ..., parent_url: _Optional[str] = ..., text: _Optional[str] = ..., mentions_positions: _Optional[_Iterable[int]] = ..., embeds: _Optional[_Iterable[_Union[Embed, _Mapping]]] = ...) -> None: ...

class CastId(_message.Message):
    __slots__ = ["fid", "hash"]
    FID_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    fid: int
    hash: bytes
    def __init__(self, fid: _Optional[int] = ..., hash: _Optional[bytes] = ...) -> None: ...

class CastRemoveBody(_message.Message):
    __slots__ = ["target_hash"]
    TARGET_HASH_FIELD_NUMBER: _ClassVar[int]
    target_hash: bytes
    def __init__(self, target_hash: _Optional[bytes] = ...) -> None: ...

class Embed(_message.Message):
    __slots__ = ["cast_id", "url"]
    CAST_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    cast_id: CastId
    url: str
    def __init__(self, url: _Optional[str] = ..., cast_id: _Optional[_Union[CastId, _Mapping]] = ...) -> None: ...

class LinkBody(_message.Message):
    __slots__ = ["displayTimestamp", "target_fid", "type"]
    DISPLAYTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TARGET_FID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    displayTimestamp: int
    target_fid: int
    type: str
    def __init__(self, type: _Optional[str] = ..., displayTimestamp: _Optional[int] = ..., target_fid: _Optional[int] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ["data", "hash", "hash_scheme", "signature", "signature_scheme", "signer"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    HASH_SCHEME_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_SCHEME_FIELD_NUMBER: _ClassVar[int]
    SIGNER_FIELD_NUMBER: _ClassVar[int]
    data: MessageData
    hash: bytes
    hash_scheme: HashScheme
    signature: bytes
    signature_scheme: SignatureScheme
    signer: bytes
    def __init__(self, data: _Optional[_Union[MessageData, _Mapping]] = ..., hash: _Optional[bytes] = ..., hash_scheme: _Optional[_Union[HashScheme, str]] = ..., signature: _Optional[bytes] = ..., signature_scheme: _Optional[_Union[SignatureScheme, str]] = ..., signer: _Optional[bytes] = ...) -> None: ...

class MessageData(_message.Message):
    __slots__ = ["cast_add_body", "cast_remove_body", "fid", "link_body", "network", "reaction_body", "signer_add_body", "signer_remove_body", "timestamp", "type", "user_data_body", "verification_add_eth_address_body", "verification_remove_body"]
    CAST_ADD_BODY_FIELD_NUMBER: _ClassVar[int]
    CAST_REMOVE_BODY_FIELD_NUMBER: _ClassVar[int]
    FID_FIELD_NUMBER: _ClassVar[int]
    LINK_BODY_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    REACTION_BODY_FIELD_NUMBER: _ClassVar[int]
    SIGNER_ADD_BODY_FIELD_NUMBER: _ClassVar[int]
    SIGNER_REMOVE_BODY_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_DATA_BODY_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_ADD_ETH_ADDRESS_BODY_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_REMOVE_BODY_FIELD_NUMBER: _ClassVar[int]
    cast_add_body: CastAddBody
    cast_remove_body: CastRemoveBody
    fid: int
    link_body: LinkBody
    network: FarcasterNetwork
    reaction_body: ReactionBody
    signer_add_body: SignerAddBody
    signer_remove_body: SignerRemoveBody
    timestamp: int
    type: MessageType
    user_data_body: UserDataBody
    verification_add_eth_address_body: VerificationAddEthAddressBody
    verification_remove_body: VerificationRemoveBody
    def __init__(self, type: _Optional[_Union[MessageType, str]] = ..., fid: _Optional[int] = ..., timestamp: _Optional[int] = ..., network: _Optional[_Union[FarcasterNetwork, str]] = ..., cast_add_body: _Optional[_Union[CastAddBody, _Mapping]] = ..., cast_remove_body: _Optional[_Union[CastRemoveBody, _Mapping]] = ..., reaction_body: _Optional[_Union[ReactionBody, _Mapping]] = ..., verification_add_eth_address_body: _Optional[_Union[VerificationAddEthAddressBody, _Mapping]] = ..., verification_remove_body: _Optional[_Union[VerificationRemoveBody, _Mapping]] = ..., signer_add_body: _Optional[_Union[SignerAddBody, _Mapping]] = ..., user_data_body: _Optional[_Union[UserDataBody, _Mapping]] = ..., signer_remove_body: _Optional[_Union[SignerRemoveBody, _Mapping]] = ..., link_body: _Optional[_Union[LinkBody, _Mapping]] = ...) -> None: ...

class ReactionBody(_message.Message):
    __slots__ = ["target_cast_id", "target_url", "type"]
    TARGET_CAST_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_URL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    target_cast_id: CastId
    target_url: str
    type: ReactionType
    def __init__(self, type: _Optional[_Union[ReactionType, str]] = ..., target_cast_id: _Optional[_Union[CastId, _Mapping]] = ..., target_url: _Optional[str] = ...) -> None: ...

class SignerAddBody(_message.Message):
    __slots__ = ["name", "signer"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIGNER_FIELD_NUMBER: _ClassVar[int]
    name: str
    signer: bytes
    def __init__(self, signer: _Optional[bytes] = ..., name: _Optional[str] = ...) -> None: ...

class SignerRemoveBody(_message.Message):
    __slots__ = ["signer"]
    SIGNER_FIELD_NUMBER: _ClassVar[int]
    signer: bytes
    def __init__(self, signer: _Optional[bytes] = ...) -> None: ...

class UserDataBody(_message.Message):
    __slots__ = ["type", "value"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: UserDataType
    value: str
    def __init__(self, type: _Optional[_Union[UserDataType, str]] = ..., value: _Optional[str] = ...) -> None: ...

class VerificationAddEthAddressBody(_message.Message):
    __slots__ = ["address", "block_hash", "eth_signature"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_HASH_FIELD_NUMBER: _ClassVar[int]
    ETH_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    address: bytes
    block_hash: bytes
    eth_signature: bytes
    def __init__(self, address: _Optional[bytes] = ..., eth_signature: _Optional[bytes] = ..., block_hash: _Optional[bytes] = ...) -> None: ...

class VerificationRemoveBody(_message.Message):
    __slots__ = ["address"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: bytes
    def __init__(self, address: _Optional[bytes] = ...) -> None: ...

class HashScheme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class SignatureScheme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class MessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class FarcasterNetwork(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class UserDataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ReactionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
