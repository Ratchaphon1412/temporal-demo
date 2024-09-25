# @@@SNIPSTART python-project-template-workflows
from datetime import timedelta
from temporalio import workflow

# Import activity, passing it through the sandbox without reloading the module
with workflow.unsafe.imports_passed_through():
    from .activities import check_existing_file,download_video,save_video_local,upload_video_cloud

@workflow.defn
class ImportFlow:
    @workflow.run
    async def run(self, url: str) -> str:
        check:str = await workflow.execute_activity(
            check_existing_file, url, start_to_close_timeout=timedelta(seconds=5)
        )
        download:str = await workflow.execute_activity(
            download_video, {"url":url,"text":check}, start_to_close_timeout=timedelta(seconds=5)
        )
        save:str = await workflow.execute_activity(
            save_video_local, {"url":url,"text":download}, start_to_close_timeout=timedelta(seconds=5)
        )
        upload:str = await workflow.execute_activity(
            upload_video_cloud, {"url":url,"text":save}, start_to_close_timeout=timedelta(seconds=5)
        )
        return upload
# @@@SNIPEND
