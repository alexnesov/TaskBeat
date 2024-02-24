from celery import Celery
import time
import logging


# Initialize Celery
celery_app = Celery(
    'tasks',
    broker='amqp://guest:guest@rabbitmq:5672',
    # broker='amqp://guest:guest@localhost:5672',
    backend='redis://redis:6379/0'
    # backend='redis://localhost:6379/0',
    # loglevel='INFO',  
    # worker_hijack_root_logger=False,  
    # stdout=True, 
    # stderr=True,
)

@celery_app.task(bind=True)
def process_task(self, task_id: int, task_data: dict):
    numbers_list = []  
    for i in range(30):
        numbers_list.append(i)  
        print(f"List with new number appended: {numbers_list}")
        time.sleep(1) 

    task_result = {'status': 'completed', 'task_id': task_id, 'data': task_data}
    logging.info(f"Task result {task_result}")
    return task_result