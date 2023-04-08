import grpc

from hub_py.generated.rpc_pb2_grpc import HubServiceStub


def get_insecure_client(address: str, use_async: bool = False) -> HubServiceStub:
    channel = (
        grpc.aio.insecure_channel(address)
        if use_async
        else grpc.insecure_channel(address)
    )
    return HubServiceStub(channel)


def get_ssl_client(address: str, use_async: bool = False) -> HubServiceStub:
    credentials = grpc.ssl_channel_credentials()
    channel = (
        grpc.aio.secure_channel(address, credentials=credentials)
        if use_async
        else grpc.secure_channel(address, credentials=credentials)
    )
    return HubServiceStub(channel)
