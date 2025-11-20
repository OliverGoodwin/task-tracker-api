from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    name: str
    done: bool

@app.get("/")
def home():
    return {"message": "API is running!"}

tasks = []
next_id = 1

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: dict):
    global next_id
    task_dict = task.dict()
    task_dict['id'] = next_id
    next_id += 1
    tasks.append(task_dict)
    return task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: dict):
    for task in tasks:
        if task['id'] == task_id:
            task.update(updated_task.dict())
            return task
    return {"error": "Task not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}
    return {"error": "Task not found"}