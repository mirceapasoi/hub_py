import message_pb2 as _message_pb2
import id_registry_event_pb2 as _id_registry_event_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
GOSSIP_VERSION_V1: GossipVersion

class ContactInfoContent(_message.Message):
    __slots__ = ["count", "excluded_hashes", "gossip_address", "hub_version", "network", "rpc_address"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_HASHES_FIELD_NUMBER: _ClassVar[int]
    GOSSIP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    HUB_VERSION_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    RPC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    count: int
    excluded_hashes: _containers.RepeatedScalarFieldContainer[str]
    gossip_address: GossipAddressInfo
    hub_version: str
    network: _message_pb2.FarcasterNetwork
    rpc_address: GossipAddressInfo
    def __init__(self, gossip_address: _Optional[_Union[GossipAddressInfo, _Mapping]] = ..., rpc_address: _Optional[_Union[GossipAddressInfo, _Mapping]] = ..., excluded_hashes: _Optional[_Iterable[str]] = ..., count: _Optional[int] = ..., hub_version: _Optional[str] = ..., network: _Optional[_Union[_message_pb2.FarcasterNetwork, str]] = ...) -> None: ...

class GossipAddressInfo(_message.Message):
    __slots__ = ["address", "dns_name", "family", "port"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DNS_NAME_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    address: str
    dns_name: str
    family: int
    port: int
    def __init__(self, address: _Optional[str] = ..., family: _Optional[int] = ..., port: _Optional[int] = ..., dns_name: _Optional[str] = ...) -> None: ...

class GossipMessage(_message.Message):
    __slots__ = ["contact_info_content", "id_registry_event", "message", "peer_id", "topics", "version"]
    CONTACT_INFO_CONTENT_FIELD_NUMBER: _ClassVar[int]
    ID_REGISTRY_EVENT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PEER_ID_FIELD_NUMBER: _ClassVar[int]
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    contact_info_content: ContactInfoContent
    id_registry_event: _id_registry_event_pb2.IdRegistryEvent
    message: _message_pb2.Message
    peer_id: bytes
    topics: _containers.RepeatedScalarFieldContainer[str]
    version: GossipVersion
    def __init__(self, message: _Optional[_Union[_message_pb2.Message, _Mapping]] = ..., id_registry_event: _Optional[_Union[_id_registry_event_pb2.IdRegistryEvent, _Mapping]] = ..., contact_info_content: _Optional[_Union[ContactInfoContent, _Mapping]] = ..., topics: _Optional[_Iterable[str]] = ..., peer_id: _Optional[bytes] = ..., version: _Optional[_Union[GossipVersion, str]] = ...) -> None: ...

class GossipVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
