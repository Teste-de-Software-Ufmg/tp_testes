import unittest
from src.controllers import TaskController
from src.models import TaskBody
from src.database import Base, engine
from datetime import date
from fastapi import HTTPException

Base.metadata.create_all(bind=engine)

class TestDeleteTask(unittest.TestCase):
    def test_delete_task_with_valid_id(self):
        task_data = TaskBody(title="New Task", description="Task description",
                             deadline=date.today(), priority="low", status="pending", id_person=0)
        task = TaskController().create(task_data)
        result = TaskController().delete(task['id'])

        self.assertEqual(result, {"message": "Tarefa deletada com sucesso"})

    def test_delete_task_with_invalid_id(self):
        try:
            TaskController().delete(0)
        except HTTPException as e:
            result = e.detail
            status_code = e.status_code
            
            self.assertEqual(result, "Tarefa não Encontrada.")
            self.assertEqual(status_code, 404)
