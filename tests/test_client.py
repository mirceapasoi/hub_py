import pytest
import grpc
from pytest_mock import MockFixture
from unittest.mock import Mock

from hub_py.generated.rpc_pb2_grpc import HubServiceStub
from hub_py.client import get_insecure_client, get_ssl_client


# Mock grpc Channels and Stubs
@pytest.fixture
def mock_insecure_channel(mocker: MockFixture) -> Mock:
    return mocker.Mock(spec=grpc.Channel)


@pytest.fixture
def mock_aio_insecure_channel(mocker: MockFixture) -> Mock:
    return mocker.Mock(spec=grpc.aio.Channel)


@pytest.fixture
def mock_secure_channel(mocker: MockFixture) -> Mock:
    return mocker.Mock(spec=grpc.Channel)


@pytest.fixture
def mock_aio_secure_channel(mocker: MockFixture) -> Mock:
    return mocker.Mock(spec=grpc.aio.Channel)


@pytest.fixture
def mock_ssl_channel_credentials(mocker: MockFixture) -> Mock:
    return mocker.Mock(spec=grpc.ChannelCredentials)


def test_get_insecure_client(mocker: MockFixture, mock_insecure_channel: Mock):
    address = "localhost:50051"
    mocker.patch("grpc.insecure_channel", return_value=mock_insecure_channel)
    client = get_insecure_client(address)
    assert isinstance(client, HubServiceStub)
    grpc.insecure_channel.assert_called_once_with(address)


def test_get_insecure_client_async(
    mocker: MockFixture, mock_aio_insecure_channel: Mock
):
    address = "localhost:50051"
    mocker.patch("grpc.aio.insecure_channel", return_value=mock_aio_insecure_channel)
    client = get_insecure_client(address, use_async=True)
    assert isinstance(client, HubServiceStub)
    grpc.aio.insecure_channel.assert_called_once_with(address)


def test_get_ssl_client(
    mocker: MockFixture, mock_secure_channel: Mock, mock_ssl_channel_credentials: Mock
):
    address = "localhost:50051"
    mocker.patch("grpc.secure_channel", return_value=mock_secure_channel)
    mocker.patch(
        "grpc.ssl_channel_credentials", return_value=mock_ssl_channel_credentials
    )
    client = get_ssl_client(address)
    assert isinstance(client, HubServiceStub)
    grpc.secure_channel.assert_called_once_with(
        address, credentials=mock_ssl_channel_credentials
    )


def test_get_ssl_client_async(
    mocker: MockFixture,
    mock_aio_secure_channel: Mock,
    mock_ssl_channel_credentials: Mock,
):
    address = "localhost:50051"
    mocker.patch("grpc.aio.secure_channel", return_value=mock_aio_secure_channel)
    mocker.patch(
        "grpc.ssl_channel_credentials", return_value=mock_ssl_channel_credentials
    )
    client = get_ssl_client(address, use_async=True)
    assert isinstance(client, HubServiceStub)
    grpc.aio.secure_channel.assert_called_once_with(
        address, credentials=mock_ssl_channel_credentials
    )
