import unittest
from datetime import date
import requests


class TestCreateTaskIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.token = requests\
            .post("http://localhost:8000/token", data={"username": "user", "password": "password"})\
            .json()\
            .get("access_token")

        return super().setUpClass()

    def test_integration_create_task_with_valid_data(self):
        task_data = {
            "title": "Task Title",
            "description": "Task description",
            "deadline": date.today().strftime('%Y-%m-%d'),
            "priority": "low",
            "status": "pending",
            "id_person": 0
        }

        result = requests\
            .post("http://localhost:8000/task/create", json=task_data, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json().get("title"), "Task Title")
        self.assertEqual(result.json().get("description"), "Task description")
        self.assertEqual(result.json().get("deadline"),
                         date.today().strftime('%Y-%m-%d'))
        self.assertEqual(result.json().get("priority"), "low")
        self.assertEqual(result.json().get("status"), "pending")
        self.assertIn('id', result.json())

    def test_integration_create_task_with_validation_error(self):
        task_data = {
            "description": 12,
            "deadline": "2020-01-01",
            "priority": "invalid",
            "status": "invalid_status"
        }

        result = requests\
            .post("http://localhost:8000/task/create", json=task_data, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(result.status_code, 422)

    def test_integration_create_task_with_priority_error(self):
        task_data = {
            "title": "Task Title",
            "description": "Task description",
            "deadline": date.today().strftime('%Y-%m-%d'),
            "priority": "invalid",
            "status": "pending",
            "id_person": 0
        }

        result = requests\
            .post("http://localhost:8000/task/create", json=task_data, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(result.status_code, 422)
        self.assertIn("A prioridade deve ser low, medium ou high",
                      result.json()["detail"][0]["msg"])
    
    def test_integration_create_task_with_status_error(self):
        task_data = {
            "title": "Task Title",
            "description": "Task description",
            "deadline": date.today().strftime('%Y-%m-%d'),
            "priority": "low",
            "status": "invalid_status",
            "id_person": 0
        }

        result = requests\
            .post("http://localhost:8000/task/create", json=task_data, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(result.status_code, 422)
        self.assertIn("O status deve ser pending, inProgress ou done",
                      result.json()["detail"][0]["msg"])

    def test_integration_create_task_with_past_deadline_error(self):
        task_data = {
            "title": "Task Title",
            "description": "Task description",
            "deadline": "2021-01-01",
            "priority": "low",
            "status": "pending",
            "id_person": 0
        }

        result = requests\
            .post("http://localhost:8000/task/create", json=task_data, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(result.status_code, 422)
        self.assertIn("A data deve ser no futuro",
                      result.json()["detail"][0]["msg"])
