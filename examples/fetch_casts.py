from .utils import get_env_client, get_env_fid

from hub_py.generated import request_response_pb2


def main() -> None:
    client = get_env_client()

    request = request_response_pb2.FidRequest(fid=get_env_fid())
    response = client.GetCastsByFid(request)
    for cast in response.messages:
        print(cast.data.cast_add_body.text)


if __name__ == "__main__":
    main()
