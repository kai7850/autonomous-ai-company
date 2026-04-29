import uuid
from core.logger import log_event
class BaseAgent:
    def __init__(self, name):
        self.name = name
        self.agent_id = str(uuid.uuid4())
    async def log(self, task_id, content):
        await log_event(task_id, self.name, content)
    async def run(self, task_id, payload):
        raise NotImplementedError
