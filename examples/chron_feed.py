import asyncio
import re

from hub_py.generated.message_pb2 import UserDataType, CastId, Message, ReactionType
from hub_py.generated.request_response_pb2 import (
    UserDataRequest,
    FidRequest,
    ReactionsByTargetRequest,
    MessagesResponse,
)
from hub_py.time import datetime_from_farcaster_time
from .utils import get_env_client


async def main() -> None:
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

    async def get_casts(fid: int) -> MessagesResponse:
        # TODO: Pagination
        return await client.GetCastsByFid(
            FidRequest(fid=fid, page_size=10, reverse=True)
        )

    casts = await asyncio.gather(*[get_casts(fid) for fid in fid_to_fname.keys()])

    async def get_reactions_by_cast_id(
        m: Message,
    ) -> tuple[int, bytes, int, int]:
        # TODO: Pagination
        response = await client.GetReactionsByCast(
            ReactionsByTargetRequest(target_cast_id=CastId(fid=m.data.fid, hash=m.hash))
        )
        likes, recasts = 0, 0
        for r in response.messages:
            if r.data.reaction_body.type == ReactionType.REACTION_TYPE_LIKE:
                likes += 1
            elif r.data.reaction_body.type == ReactionType.REACTION_TYPE_RECAST:
                recasts += 1
        return m.data.fid, m.hash, likes, recasts

    reactions = await asyncio.gather(
        *[get_reactions_by_cast_id(m) for r in casts for m in r.messages]
    )
    reaction_counts = {
        (fid, hash): (likes, recasts) for fid, hash, likes, recasts in reactions
    }

    merged_casts = [m for r in casts for m in r.messages]
    sorted_casts = sorted(merged_casts, key=lambda m: m.data.timestamp)
    for cast in sorted_casts:
        fname = fid_to_fname[cast.data.fid]
        likes, recasts = reaction_counts.get((cast.data.fid, cast.hash), (0, 0))
        timestamp = datetime_from_farcaster_time(cast.data.timestamp)
        text_no_line_breaks = re.sub(r"(\r\n|\n|\r)", " ", cast.data.cast_add_body.text)
        print(
            f"@{fname}: {text_no_line_breaks}\n{timestamp}\t{likes} likes\t{recasts} recasts"
        )


if __name__ == "__main__":
    asyncio.run(main())
