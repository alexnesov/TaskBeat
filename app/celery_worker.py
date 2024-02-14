from celery import Celery

# Initialize Celery
celery_app = Celery(
    'tasks',
    broker='amqp://guest:guest@rabbitmq:5672',
    backend='redis://redis:6379/0'
)

# Celery task
@celery_app.task(bind=True)
def process_task(self, task_id: int, task_data: dict):
    # Simulate processing the task
    task_result = {'status': 'completed', 'task_id': task_id, 'data': task_data}
    return task_result
