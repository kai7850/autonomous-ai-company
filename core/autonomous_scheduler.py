import uuid
from agents.ceo_agent import CEOAgent
from agents.research_agent import ResearchAgent
from agents.content_agent import ContentAgent
from agents.execute_agent import ExecuteAgent
class AutonomousScheduler:
    def __init__(self):
        self.ceo=CEOAgent(); self.research=ResearchAgent(); self.content=ContentAgent(); self.execute=ExecuteAgent()
    async def start(self, goal):
        task_id = str(uuid.uuid4())
        plan = await self.ceo.run(task_id, goal)
        await self.research.run(task_id, plan)
        await self.content.run(task_id, plan)
        await self.execute.run(task_id, plan)
        return task_id
