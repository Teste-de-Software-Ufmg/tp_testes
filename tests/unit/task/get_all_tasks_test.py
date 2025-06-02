import unittest
from fastapi import HTTPException
from src.controllers import TaskController
from src.models import TaskBody
from src.database import Base, engine
from datetime import date

Base.metadata.create_all(bind=engine)

class TestGetAllTask(unittest.TestCase):

    def test_getall_tasks(self):
        result = TaskController().get_all()        
        self.assertIsInstance(result, list)
