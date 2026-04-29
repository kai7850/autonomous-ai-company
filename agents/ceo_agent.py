from core.base_agent import BaseAgent
from core.llm_gateway import llm_gateway
from core.state_manager import state_manager
class CEOAgent(BaseAgent):
    def __init__(self): super().__init__("CEO_AGENT")
    async def run(self, task_id, payload):
        result = await llm_gateway.ask_gpt(f"拆解这个运营目标为调研、内容、执行步骤：{payload}")
        await state_manager.set(task_id, "master_plan", result); await self.log(task_id, result); return result
