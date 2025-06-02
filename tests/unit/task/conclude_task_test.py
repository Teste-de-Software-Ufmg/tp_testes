import unittest
from fastapi import HTTPException
from src.controllers import TaskController
from src.models import TaskBody
from src.database import Base, engine
from datetime import date

Base.metadata.create_all(bind=engine)

class TestConcludeTask(unittest.TestCase):

    def test_conclude_task_with_valid_data(self):
        task_data = TaskBody(
            title="New Task", description="test",
            status="pending", priority="high", deadline=str(date.today()),
            id_person=0
        )

        result = TaskController().create(task_data)
        
        id = result['id']
        result = TaskController().conclude(id)

        self.assertEqual(result['message'], "Tarefa concluída com sucesso")

        result = TaskController().get(id)

        self.assertEqual(result['status'], "done")

    def test_conclude_task_with_invalid_id(self):
        person_data = TaskBody(
            title="New Task", description="test",
            status="pending", priority="high", deadline=str(date.today()),
            id_person=0
        )

        try:
            _ = TaskController().conclude(-10)
        
        except HTTPException as e:
            self.assertEqual(e.__str__(), "404: Tarefa não encontrada.")
        
        except Exception:
            self.fail("HTTPException not raised")
