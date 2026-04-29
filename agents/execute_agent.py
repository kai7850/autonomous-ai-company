from core.base_agent import BaseAgent
from core.state_manager import state_manager
class ExecuteAgent(BaseAgent):
    def __init__(self): super().__init__("EXECUTE_AGENT")
    async def run(self, task_id, payload):
        content = await state_manager.get(task_id, "content")
        print("SIMULATED EXECUTION:", content[:100])
        await self.log(task_id, "execution complete")
        return "done"
