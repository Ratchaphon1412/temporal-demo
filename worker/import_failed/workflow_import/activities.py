# @@@SNIPSTART python-project-template-activities
from temporalio import activity
from typing import TypedDict
class VideoTaskInput(TypedDict):
    url: str
    text: str


@activity.defn
async def check_existing_file(url: str) -> str:
    return f"1. check existing video from Url, {url}! \n"


@activity.defn
async def download_video(payload:VideoTaskInput) -> str:
    raise Exception(f"Failed to download {payload['url']} \n")

@activity.defn
async def save_video_local(payload:VideoTaskInput) -> str:
    return payload["text"] + f"3. save video from Url, {payload['url']}! \n"

@activity.defn
async def upload_video_cloud(payload:VideoTaskInput) -> str:
    return payload["text"]  + f"4. upload video from Url, byteark storage! \n"

# @@@SNIPEND
