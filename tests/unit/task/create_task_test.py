import unittest
from src.controllers import TaskController
from src.models import TaskBody
from datetime import date
from src.database import Base, engine

Base.metadata.create_all(bind=engine)

class TestCreateTask(unittest.TestCase):

    def test_create_task_with_valid_data(self):
        task_data = TaskBody(title="New Task", description="Task description", deadline=date.today(), priority="low", status="pending", id_person=0)

        result = TaskController().create(task_data)
        self.assertEqual(result['title'], 'New Task')
        self.assertEqual(result['description'], 'Task description')
        self.assertEqual(result['deadline'], date.today().strftime('%Y-%m-%d'))
        self.assertEqual(result['priority'], 'low')
        self.assertEqual(result['status'], 'pending')
        self.assertIn('id', result)

    def test_create_task_with_validation_error(self):
        try:
            task_data = TaskBody(description=12, deadline="2020-01-01", priority="bla", status="bla")
        except ValueError as e:
            error = str(e).split("\n")
            self.assertEqual(error[0], "6 validation errors for TaskBody")
        else:
            self.fail("ValueError not raised")
            
    def test_create_task_with_priority_error(self):
        try:
            task_data = TaskBody(title="New Task", description="Task description", deadline=date.today(), priority="bla", status="pending", id_person=0)
        except ValueError as e:
            error = str(e).split("\n")
            self.assertEqual(error[0], "1 validation error for TaskBody")
            self.assertIn("A prioridade deve ser low, medium ou high", error[2])
            
    def test_create_task_with_status_error(self):
        try:
            task_data = TaskBody(title="New Task", description="Task description", deadline=date.today(), priority="low", status="bla", id_person=0)
        except ValueError as e:
            error = str(e).split("\n")
            self.assertEqual(error[0], "1 validation error for TaskBody")
            self.assertIn("O status deve ser pending, inProgress ou done", error[2])
    
    def test_create_task_with_past_deadline_error(self):
        try:
            task_data = TaskBody(title="New Task", description="Task description", deadline="2021-01-01", priority="low", status="pending", id_person=0)
        except ValueError as e:
            error = str(e).split("\n")
            self.assertEqual(error[0], "1 validation error for TaskBody")
            self.assertIn("A data deve ser no futuro", error[2])