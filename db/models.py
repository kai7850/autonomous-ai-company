from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime
import datetime
Base = declarative_base()
class AgentLogs(Base):
    __tablename__ = "agent_logs"
    id = Column(Integer, primary_key=True)
    task_id = Column(String(255))
    agent_name = Column(String(255))
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
