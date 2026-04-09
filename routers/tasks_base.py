import logging
from uuid import uuid4

from fastapi import APIRouter
from models import Task, CreateTaskRequest
from store import tasks

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/tasks", response_model=list[Task])
def get_tasks():
    task_list = list(tasks.values())
    logger.info(f"Numero di task: {len(task_list)}")
    return task_list


@router.post("/tasks", response_model=Task, status_code=201)
def create_task(request: CreateTaskRequest):
    task = Task(
        id=str(uuid4()),
        title=request.title,
        description=request.description,
        status=request.status,
    )
    tasks[task.id] = task
    logger.info(f"Task creato - ID: {task.id}, Titolo: '{task.title}'")
    return task