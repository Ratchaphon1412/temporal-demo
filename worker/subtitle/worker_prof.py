# @@@SNIPSTART python-project-template-run-worker
import asyncio

from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.worker import Worker

from workflow_subtitle.activities_prof import profSubtitle
from workflow_subtitle.workflows_prof import ProfFlow


async def main():
    client = await Client.connect("localhost:7233", namespace="default")
    # Run the worker
    worker = Worker(
        client, task_queue="prof-queue", workflows=[ProfFlow], activities=[profSubtitle]
    ) 
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
# @@@SNIPEND
