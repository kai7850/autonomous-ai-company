from core.base_agent import BaseAgent
from core.llm_gateway import llm_gateway
from core.state_manager import state_manager
class ContentAgent(BaseAgent):
    def __init__(self): super().__init__("CONTENT_AGENT")
    async def run(self, task_id, payload):
        research = await state_manager.get(task_id, "research")
        result = await llm_gateway.ask_gpt(f"根据调研生成TikTok文案、商品文案、SEO标题：{research}")
        await state_manager.set(task_id, "content", result); await self.log(task_id, result); return result
