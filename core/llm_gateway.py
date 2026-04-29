from openai import AsyncOpenAI
from config import settings
class LLMGateway:
    def __init__(self):
        self.gpt = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
    async def ask_gpt(self, prompt):
        res = await self.gpt.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role":"user","content":prompt}]
        )
        return res.choices[0].message.content
llm_gateway = LLMGateway()
