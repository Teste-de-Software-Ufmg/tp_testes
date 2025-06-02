import unittest
from fastapi import HTTPException
from src.controllers import TaskController, PersonController
from src.models import TaskBody, PersonBody
from src.database import Base, engine
from datetime import date

Base.metadata.create_all(bind=engine)

class TestVinculateTask(unittest.TestCase):

    def setUp(self):
        self.task_data = TaskBody(
            title="New Task", description="test",
            status="pending", priority="high", deadline=str(date.today()),
            id_person=0
        )

        self.person_data = PersonBody(
            name="Person", email="teste@gmail.com", phone="11988888888"
        )

        self.task_ids: list = []
        self.person_ids: list = []

    def test_vinculate_task_with_valid_data(self):
        task = TaskController().create(self.task_data)
        person = PersonController().create(self.person_data)

        result = TaskController().vinculate(task['id'], person['id'])
        result = TaskController().get(task['id'])

        self.assertEqual(result['id_person'], person['id'])

        self.task_ids.append(task['id'])
        self.person_ids.append(person['id'])

    def test_update_task_with_invalid_person_id(self):
        task = TaskController().create(self.task_data)

        try:
            _ = TaskController().vinculate(task['id'], -10)

        except HTTPException as e:
            self.assertEqual(e.__str__(), "404: Pessoa não encontrada.")
        
        except Exception:
            self.fail("HTTPException not raised")

    def test_update_task_with_invalid_task_id(self):
        person = PersonController().create(self.person_data)

        try:
            _ = TaskController().vinculate(-10, person['id'])

        except HTTPException as e:
            self.assertEqual(e.__str__(), "404: Tarefa não encontrada.")
        
        except Exception:
            self.fail("HTTPException not raised")

    def tearDown(self):
        for task_id in self.task_ids:
            TaskController().delete(task_id)

        for person_id in self.person_ids:
            PersonController().delete(person_id)
