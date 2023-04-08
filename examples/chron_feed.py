import asyncio

from hub_py.generated.message_pb2 import UserDataType, MessageData
from hub_py.generated.request_response_pb2 import (
    UserDataRequest,
    FidRequest,
)
from hub_py.time import datetime_from_farcaster_time
from .utils import get_env_client


async def main():
    client = get_env_client(use_async=True)

    fid_to_fname = {}
    result = await asyncio.gather(
        *[
            client.GetUserData(
                UserDataRequest(
                    fid=fid, user_data_type=UserDataType.USER_DATA_TYPE_FNAME
                )
            )
            for fid in range(1, 10)
        ]
    )
    fid_to_fname = {r.data.fid: r.data.user_data_body.value for r in result}
    print(fid_to_fname)

    casts = await asyncio.gather(
        *[
            client.GetCastsByFid(FidRequest(fid=fid, page_size=10, reverse=True))
            for fid in fid_to_fname.keys()
        ]
    )
    merged_casts = [m.data for r in casts for m in r.messages]
    sorted_casts = sorted(merged_casts, key=lambda x: x.timestamp)
    for cast in sorted_casts:
        fname = fid_to_fname[cast.fid]
        timestamp = datetime_from_farcaster_time(cast.timestamp)
        print(f"{fname}: {cast.cast_add_body.text}\n{timestamp}")


if __name__ == "__main__":
    asyncio.run(main())
