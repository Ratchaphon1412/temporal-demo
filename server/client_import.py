# @@@SNIPSTART python-project-template-run-workflow-hello-world
import asyncio


from temporalio.client import Client


async def main():
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233")

    # Execute a workflow
    result = await client.execute_workflow(
        "ImportFlow", "https://www.youtube.com/watch?v=nKFZJU7bvaw", id="import-video-youtube", task_queue="import-queue"
    )

    print(f"Result: import workflow \n {result}")


if __name__ == "__main__":
    asyncio.run(main())
# @@@SNIPEND
