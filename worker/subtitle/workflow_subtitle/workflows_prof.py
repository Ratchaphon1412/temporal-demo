# @@@SNIPSTART python-project-template-workflows
from datetime import timedelta
from temporalio import workflow

# Import activity, passing it through the sandbox without reloading the module
with workflow.unsafe.imports_passed_through():
    from .activities_prof import profSubtitle
@workflow.defn
class ProfFlow:
    @workflow.run
    async def run(self, sub: str) -> str:
        approve:str = await workflow.execute_activity(
            profSubtitle, sub, start_to_close_timeout=timedelta(seconds=5)
        )
        return approve
# @@@SNIPEND
