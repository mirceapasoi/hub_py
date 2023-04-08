from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HubState(_message.Message):
    __slots__ = ["last_eth_block"]
    LAST_ETH_BLOCK_FIELD_NUMBER: _ClassVar[int]
    last_eth_block: int
    def __init__(self, last_eth_block: _Optional[int] = ...) -> None: ...
