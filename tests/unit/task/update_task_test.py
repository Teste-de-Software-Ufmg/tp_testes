import unittest
from fastapi import HTTPException
from src.controllers import TaskController
from src.repositories import TaskRepository
from src.models import TaskBody
from src.database import Base, engine
from datetime import date

Base.metadata.create_all(bind=engine)

class TestUpdateTask(unittest.TestCase):

    def test_update_task_with_valid_data(self):
        task_data = TaskBody(
            title="New Task", description="test",
            status="pending", priority="high", deadline=str(date.today()),
            id_person=0
        )

        result = TaskController().create(task_data)

        task_data = TaskBody(
            title="New Task 1", description="test 1", 
            status="done", priority="low", deadline=str(date.today()),
            id_person=0
        )

        id = result['id']
        result = TaskController().update(id, task_data)

        self.assertEqual(result['message'], "Tarefa atualizada com sucesso")

        result2 = TaskController().get(id)

        self.assertEqual(result2['title'], "New Task 1")
        self.assertEqual(result2['description'], "test 1")
        self.assertEqual(result2['status'], "done")
        self.assertEqual(result2['priority'], "low")
        self.assertEqual(result2['deadline'], str(date.today()))
        self.assertEqual(result2['updated_at'], str(date.today()))

    def test_update_task_with_invalid_id(self):
        task_data = TaskBody(
            title="New Task", description="test",
            status="pending", priority="high", deadline=str(date.today()),
            id_person=0
        )

        try:
            _ = TaskController().update(-10, task_data)
        
        except HTTPException as e:
            self.assertEqual(e.__str__(), "404: Tarefa não encontrada.")
        
    def test_with_not_inserted_id(self):
        task_data = TaskBody(
            title="New Task", description="test",
            status="pending", priority="high", deadline=str(date.today()),
            id_person=0
        )

        res = TaskRepository().update(1000, task_data)
        self.assertIsNone(res)
