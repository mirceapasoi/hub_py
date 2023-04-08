import grpc
from dotenv import load_dotenv

from hub_py.builders import make_signer_add, make_user_data_add
from hub_py.generated.message_pb2 import (
    MessageData,
    UserDataBody,
    UserDataType,
)

from .utils import (
    get_env_client,
    get_env_network,
    get_env_signer,
    get_env_fid,
    get_env_mnemonic_signer,
)


def main():
    load_dotenv()

    fid = get_env_fid()
    mnemonic_signer = get_env_mnemonic_signer()
    add_signer = get_env_signer()

    client = get_env_client()
    message_data = MessageData(
        fid=fid,
        network=get_env_network(),
    )

    message = make_signer_add(
        message_data,
        mnemonic_signer,
        add_signer,
    )
    try:
        client.SubmitMessage(message)
        print(f"SIGNER_ADD was published successfully")
    except grpc.RpcError as e:
        print(e.details())

    message = make_user_data_add(
        message_data,
        add_signer,
        UserDataBody(
            type=UserDataType.USER_DATA_TYPE_PFP,
            value="https://i.imgur.com/yed5Zfk.gif",
        ),
    )
    try:
        client.SubmitMessage(message)
        print("USER_DATA_ADD was published successfully")
    except grpc.RpcError as e:
        print(e.details())


if __name__ == "__main__":
    main()
