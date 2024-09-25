# @@@SNIPSTART python-project-template-run-worker
import asyncio

from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.worker import Worker

from workflow_import.activities import check_existing_file, download_video, save_video_local, upload_video_cloud
from workflow_import.workflows import ImportFlow

async def main():
    client = await Client.connect("localhost:7233", namespace="default")
    # Run the worker
    worker = Worker(
        client, task_queue="import-queue", workflows=[ImportFlow], activities=[check_existing_file,download_video,save_video_local,upload_video_cloud]
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
# @@@SNIPEND
