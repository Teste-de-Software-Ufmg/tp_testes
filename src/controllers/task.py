from src.services import TaskService
from src.models import TaskBody

class TaskController:
    def __init__(self):
        self.task_service = TaskService()

    def create(self, task_data: TaskBody) -> dict:
        return self.task_service.create(task_data)
    
    def get(self, id: int) -> dict:
        return self.task_service.get(id)
    
    def get_all(self) -> dict:
        return self.task_service.get_all()

    def update(self, id: int, task_data: TaskBody) -> dict:
        return self.task_service.update(id, task_data)
    
    def delete(self, id: int) -> dict:
        return self.task_service.delete(id)
    
    def vinculate(self, id: int, person_id: int) -> dict:
        return self.task_service.vinculate(id, person_id)
    
    def conclude(self, id: int) -> dict:
        return self.task_service.conclude(id)
