# @@@SNIPSTART python-project-template-activities
from temporalio import activity


@activity.defn
async def generateSubtitle(lang: str) -> str:
    return f"1. Worker Subtitle: generate subtitle in  {lang}  \n"

# @@@SNIPEND
