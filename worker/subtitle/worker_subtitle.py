# @@@SNIPSTART python-project-template-run-worker
import asyncio

from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.worker import Worker

from workflow_subtitle.activities_subtitle import generateSubtitle
from workflow_subtitle.workflows_subtitle import SubtitleFlow


async def main():
    client = await Client.connect("localhost:7233", namespace="default")
    # Run the worker
    worker = Worker(
        client, task_queue="subtitle-queue", workflows=[SubtitleFlow], activities=[generateSubtitle]
    ) 
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
# @@@SNIPEND
