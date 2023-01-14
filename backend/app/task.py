from flask import Flask, request

from app.database import task


app = Flask (_name_)


@app.get('/')
@app.get('/ping')
def index():
    out = {
        "status": "ok",
        "message": "success"
    }
    return out

    #CRUD endpoints

@app.get("/tasks")
def get_all_tasks():
    out = {}
    out["tasks"] = task.scan()
    return out 

@app.post("/tasks")
def create_task():
    task_data = request.json
    task.insert(task_data)
    return "", 204

@app.get("/tasks/<int:pk>")
def get_task_by_id(pk):
    out = {}
    out["task"] = task.select_by_id(pk)
    return out 

@app.get("/task/<int:pk>")
def update_task_by_id(pk):
    task_data  = request.json
    task.update(task_data, pk) 
    return "", 204

@app.delete("/tasks/<int:pk>")
def delete_task_by_id(pk):
    task.delete(pk)
    return"", 204