from pydantic import BaseModel

# Pydantic model for task data
class TaskData(BaseModel):
    title: str
    description: str

# Pydantic model for response data
class TaskResponse(BaseModel):
    task_id: int
    status: str
    result: dict
