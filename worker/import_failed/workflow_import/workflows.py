# @@@SNIPSTART python-project-template-workflows
from datetime import timedelta
from temporalio import workflow
from temporalio.common import RetryPolicy

# Import activity, passing it through the sandbox without reloading the module
with workflow.unsafe.imports_passed_through():
    from .activities import check_existing_file,download_video,save_video_local,upload_video_cloud

retry_policy = RetryPolicy(
        maximum_attempts=10,
        maximum_interval=timedelta(seconds=10),
    )

@workflow.defn
class ImportFlow:
    @workflow.run
    async def run(self, url: str) -> str:
        check:str = await workflow.execute_activity(
            check_existing_file, url, start_to_close_timeout=timedelta(seconds=5), retry_policy=retry_policy
        )
        download:str = await workflow.execute_activity(
            download_video, {"url":url,"text":check}, start_to_close_timeout=timedelta(seconds=5), retry_policy=retry_policy
        )
        save:str = await workflow.execute_activity(
            save_video_local, {"url":url,"text":download}, start_to_close_timeout=timedelta(seconds=5), retry_policy=retry_policy
        )
        upload:str = await workflow.execute_activity(
            upload_video_cloud, {"url":url,"text":save}, start_to_close_timeout=timedelta(seconds=5) , retry_policy=retry_policy
        )
        return upload
# @@@SNIPEND
