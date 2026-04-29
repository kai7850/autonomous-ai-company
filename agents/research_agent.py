from core.base_agent import BaseAgent
from core.llm_gateway import llm_gateway
from core.state_manager import state_manager
class ResearchAgent(BaseAgent):
    def __init__(self): super().__init__("RESEARCH_AGENT")
    async def run(self, task_id, payload):
        result = await llm_gateway.ask_gpt(f"根据这个计划做市场调研与热点分析：{payload}")
        await state_manager.set(task_id, "research", result); await self.log(task_id, result); return result
