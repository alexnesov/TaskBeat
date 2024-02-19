from celery import Celery
import time

# Initialize Celery
celery_app = Celery(
    'tasks',
    # broker='amqp://guest:guest@rabbitmq:5672',
    broker='amqp://guest:guest@localhost:5672',
    # backend='redis://redis:6379/0'
    backend='redis://localhost:6379/0'
)

@celery_app.task(bind=True)
def process_task(self, task_id: int, task_data: dict):
    numbers_list = []  # Initialize an empty list
    for i in range(30):  # Change 10 to the desired number of iterations
        numbers_list.append(i)  # Append a number to the list
        print(f"List with new number appended: {numbers_list}")
        time.sleep(1)  # Pause for 1 second

    task_result = {'status': 'completed', 'task_id': task_id, 'data': task_data}
    return task_result