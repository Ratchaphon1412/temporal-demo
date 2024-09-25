# @@@SNIPSTART python-project-template-workflows
from datetime import timedelta
from temporalio import workflow

# Import activity, passing it through the sandbox without reloading the module
with workflow.unsafe.imports_passed_through():
    from .activities_subtitle import  generateSubtitle
    
from .workflows_prof import ProfFlow

@workflow.defn
class SubtitleFlow:
    @workflow.run
    async def run(self, lang: str) -> str:
        sub:str = await workflow.execute_activity(
            generateSubtitle, lang, start_to_close_timeout=timedelta(seconds=5)
        )
        approve:str = await workflow.execute_child_workflow(
            ProfFlow, sub, id="sub-prof-thai-lang"
        )
        return approve
# @@@SNIPEND
