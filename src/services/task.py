from src.repositories import TaskRepository
from src.repositories import PersonRepository
from src.models import TaskBody
from fastapi import HTTPException

class TaskService:
    def __init__(self) -> None:
        self.__repository = TaskRepository()

    def create(self, task_data: TaskBody) -> dict:
        return self.__repository.create(task_data)
    
    def get(self, id: int) -> dict:
        task = self.__repository.get(id)
        if not task:
            raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
        return task
    
    def get_all(self) -> dict:
        return self.__repository.get_all()
    
    def update(self, id: int, task_data: TaskBody) -> dict:
        task = self.__repository.get(id)
        if not task:
            raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
        return self.__repository.update(id, task_data)

    def delete(self, id: int) -> dict:
        task = self.__repository.get(id)
        if not task:
            raise HTTPException(status_code=404, detail="Tarefa não Encontrada.")
        return self.__repository.delete(id)
    
    def vinculate(self, id: int, person_id: int) -> dict:
        task = self.__repository.get(id)
        person = PersonRepository().get(person_id)
        
        if not task:
            raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
        if not person:
            raise HTTPException(status_code=404, detail="Pessoa não encontrada.")
        
        return self.__repository.vinculate(id, person_id)
    
    def conclude(self, id: int) -> dict:
        task = self.__repository.get(id)
        if not task:
            raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
        return self.__repository.conclude(id)
