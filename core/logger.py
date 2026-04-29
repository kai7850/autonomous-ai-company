from db.session import SessionLocal
from db.models import AgentLogs
async def log_event(task_id, agent_name, content):
    db = SessionLocal()
    db.add(AgentLogs(task_id=task_id, agent_name=agent_name, content=str(content)))
    db.commit()
    db.close()
