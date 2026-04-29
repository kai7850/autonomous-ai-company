from celery import Celery
celery_app = Celery("autonomous_ai_company", broker="redis://redis:6379/0", backend="redis://redis:6379/1")
