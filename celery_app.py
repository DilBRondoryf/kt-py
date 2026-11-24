from celery import Celery
import time
import os

CELERY_BROKER = os.getenv("CELERY_BROKER")

celery_app = Celery(
    "tasks", broker=CELERY_BROKER, backend=CELERY_BROKER
)

@celery_app.task
def send_welcome_email(email):
    time.sleep(5)
    print(f"письмо отпрвили {email}")
    return {
        "result": "ok"
    }