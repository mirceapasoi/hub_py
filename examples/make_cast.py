import grpc

import hub_py.protobuf_patch as _
from hub_py.builders import make_cast_add
from hub_py.generated.message_pb2 import (
    MessageData,
    CastAddBody,
)

from .utils import get_env_signer, get_env_fid, get_env_client, get_env_network


def main():
    client = get_env_client()
    message_data = MessageData(
        fid=get_env_fid(),
        network=get_env_network(),
    )
    signer = get_env_signer()
    casts = [
        # Example 1: A cast with no mentions
        CastAddBody(
            text="This is a cast with no mentions",
            embeds=[],
            mentions=[],
            mentions_positions=[],
        ),
        # Example 2: A cast with mentions
        CastAddBody(
            text=" and  are big fans of ",
            embeds=[],
            mentions=[3, 2, 1],
            mentions_positions=[0, 5, 22],
        ),
        # Example 3: A cast with mentions and an attachment
        CastAddBody(
            text="Hey , check this out!",
            embeds=["https://farcaster.xyz"],
            mentions=[3],
            mentions_positions=[4],
        ),
        # Example 4: A cast with mentions and an attachment, and a link in the text
        CastAddBody(
            text="Hey , check out https://farcaster.xyz!",
            embeds=["https://farcaster.xyz"],
            mentions=[3],
            mentions_positions=[4],
        ),
        # Example 5: A cast with multiple mentions
        CastAddBody(
            text="You can mention  multiple times:   ",
            embeds=[],
            mentions=[2, 2, 2, 2],
            mentions_positions=[16, 33, 34, 35],
        ),
        # Example 6: A cast with emoji and mentions
        CastAddBody(
            text="🤓 can mention immediately after emoji",
            embeds=[],
            mentions=[1],
            mentions_positions=[4],
        ),
        # Example 7: A cast with emoji and a link in the text and an attachment
        CastAddBody(
            text="🤓https://url-after-unicode.com can include URL immediately after emoji!!s",
            embeds=["https://url-after-unicode.com"],
            mentions=[],
            mentions_positions=[],
        ),
    ]

    for cast in casts:
        try:
            result = client.SubmitMessage(
                make_cast_add(
                    message_data,
                    signer,
                    cast,
                )
            )
            print(result.data.cast_add_body)
        except grpc.RpcError as e:
            print(e.details())


if __name__ == "__main__":
    main()
