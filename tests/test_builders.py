import pytest
from hub_py.time import get_farcaster_time
from hub_py.signers import Ed25519Signer, EIP712Signer
from hub_py.generated.message_pb2 import (
    Message,
    MessageData,
    HashScheme,
    MessageType,
    UserDataBody,
    CastAddBody,
)
from hub_py.builders import (
    _make_message,
    make_signer_add,
    make_user_data_add,
    make_cast_add,
)


@pytest.fixture
def example_signer() -> Ed25519Signer:
    return Ed25519Signer.generate()


@pytest.fixture
def example_message_data() -> MessageData:
    return MessageData(type=MessageType.MESSAGE_TYPE_CAST_ADD)


def test_make_message(example_signer: Ed25519Signer, example_message_data: MessageData):
    message = _make_message(example_message_data, example_signer)
    assert isinstance(message, Message)
    assert message.data.type == example_message_data.type
    assert message.data.timestamp is not None
    assert message.hash_scheme == HashScheme.HASH_SCHEME_BLAKE3
    assert message.signature_scheme == example_signer.signature_scheme()
    assert message.signer == example_signer.public_key()


def test_make_signer_add(
    example_signer: Ed25519Signer, example_message_data: MessageData
):
    signer = EIP712Signer.generate()
    message = make_signer_add(example_message_data, signer, example_signer)
    assert message.data.type == MessageType.MESSAGE_TYPE_SIGNER_ADD
    assert message.data.signer_add_body.signer == example_signer.public_key()


def test_make_user_data_add(
    example_signer: Ed25519Signer, example_message_data: MessageData
):
    user_data = UserDataBody(value="https://i.imgur.com/yed5Zfk.gif")
    message = make_user_data_add(example_message_data, example_signer, user_data)
    assert message.data.type == MessageType.MESSAGE_TYPE_USER_DATA_ADD
    assert message.data.user_data_body == user_data


def test_make_cast_add(
    example_signer: Ed25519Signer, example_message_data: MessageData
):
    cast_add = CastAddBody(text="test_cast")
    message = make_cast_add(example_message_data, example_signer, cast_add)
    assert message.data.type == MessageType.MESSAGE_TYPE_CAST_ADD
    assert message.data.cast_add_body == cast_add
