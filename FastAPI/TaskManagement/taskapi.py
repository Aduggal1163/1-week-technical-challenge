from fastapi import FastAPI,HTTPException,status
from taskmodel import Task
app = FastAPI()
import uvicorn

Tasks = [
    Task(
        id=1,
        name="Build FastAPI Backend",
        description="Create REST API for task management system",
        completed=False,
        priority="high"
    ),
    Task(
        id=2,
        name="Write Documentation",
        description="Prepare README file for GitHub repository",
        completed=False,
        priority="medium"
    ),
    Task(
        id=3,
        name="Fix Bug in Validation",
        description="Resolve priority validation issue",
        completed=True,
        priority="low"
    ),
    Task(
        id=4,
        name='write fastapis',
        description="Write fastapis in beautiful way",
        completed=True,
        priority="high"
    )
]

@app.post("/create",status_code=status.HTTP_201_CREATED)
def create_app(task : Task):
    for existing_task in Tasks:
        if existing_task.id == task.id:
            raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='task with this id already exists'
            )

    Tasks.append(task)
    return Tasks
    
@app.get("/all")
def getAll():
    if(len(Tasks) == 0):
        raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='tasks not exists'
                )
        
    return Tasks

@app.get('/task/{id}')
def getTaskById(id : int):
    for existing_task in Tasks:
        if existing_task.id == id:
            return existing_task
    raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Task with this id not found'
        
    )

@app.post('/update/{id}')
def updateApp(id: int, task : Task):
    for existing_task in Tasks:
        if(existing_task.id == id):
            if(task.name is not None):
                existing_task.name=task.name
            if(task.description is not None):
                existing_task.description = task.description
            if(task.priority != existing_task.priority):
                existing_task.priority = task.priority
            return {
                'message':"The task has been successfully updated",
                'task':existing_task
            }
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task not found'
    )

@app.delete("/delete/{id}")
def deleteTask(id: int):
    for existing_task in Tasks:
        if(existing_task.id == id):
            Tasks.remove(existing_task)
            return {
                'message':"The task has been removed successfully",
                'task':Tasks
            }
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='task not found'
        
    )

@app.patch('/tasks/{id}/complete')
def completeTask(id: int):
    for existing_task in Tasks:
        if existing_task.id == id:
            if existing_task.completed == True:
                raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail='task already completed'
                )
            existing_task.completed = True
            return {
                'message':"The task has been completed successfully",
                'task':existing_task
            }
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
    )

@app.get('/tasks/priority/{priority}')
def getPriorTasks(priority : str):
    filtered_tasks=[]
    for existingTasks in Tasks:
        if(existingTasks.priority == priority.lower()):
            filtered_tasks.append(existingTasks)
    return {
        'message':"Here are the filtered tasks",
        'task':filtered_tasks
    }

@app.on_event('startup')
def start_app():
    print("The server is running on port 8000")

if __name__=="__main__":
    uvicorn.run(app,host='localhost',port=8000)
