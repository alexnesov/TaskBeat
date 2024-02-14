from fastapi import FastAPI, BackgroundTasks
from app.celery_worker import celery_app
from app.models import TaskData, TaskResponse

app = FastAPI()

# FastAPI endpoint for submitting tasks
@app.post("/submit-task/", response_model=TaskResponse)
async def submit_task(background_tasks: BackgroundTasks, task_data: TaskData):
    # Generate a unique task ID
    task_id = hash(str(task_data))
    # Execute the Celery task asynchronously
    background_tasks.add_task(celery_app.send_task, 'app.celery_worker.process_task', args=[task_id, task_data.dict()])
    return {"task_id": task_id, "status": "submitted", "result": {}}

# FastAPI endpoint for checking task status
@app.get("/task-status/{task_id}", response_model=TaskResponse)
async def task_status(task_id: int):
    # Check Celery task status
    result = celery_app.AsyncResult(task_id)
    if result.ready():
        return {"task_id": task_id, "status": "completed", "result": result.result}
    else:
        return {"task_id": task_id, "status": "pending", "result": {}}
