from fastapi import APIRouter
from sse_starlette.sse import EventSourceResponse
import asyncio

router = APIRouter()


@router.get("/progress")
async def progress_stream():

    async def event_generator():

        yield {
            "data": "10%"
        }

        await asyncio.sleep(2)

        yield {
            "data": "30%"
        }

        await asyncio.sleep(2)

        yield {
            "data": "60%"
        }

        await asyncio.sleep(2)

        yield {
            "data": "100%"
        }

    return EventSourceResponse(
        event_generator()
    )