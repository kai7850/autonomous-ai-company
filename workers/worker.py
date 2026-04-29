from core.task_queue import celery_app
from core.autonomous_scheduler import AutonomousScheduler
import asyncio
@celery_app.task
def run_company(goal):
    scheduler = AutonomousScheduler()
    asyncio.run(scheduler.start(goal))
