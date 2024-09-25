# @@@SNIPSTART python-project-template-run-workflow-hello-world
import asyncio


from temporalio.client import Client


async def main():
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233")

    # Execute a workflow
    result = await client.execute_workflow(
        "SubtitleFlow", "thai", id="sub-generate-thai-lang", task_queue="subtitle-queue"
    )

    print(f"Result: import workflow \n {result}")


if __name__ == "__main__":
    asyncio.run(main())
# @@@SNIPEND
