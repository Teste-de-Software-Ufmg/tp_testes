import unittest
from fastapi import HTTPException
from src.controllers import TaskController
from src.models import TaskBody
from src.database import Base, engine
from datetime import date

Base.metadata.create_all(bind=engine)

class TestGetTask(unittest.TestCase):

    def test_get_task(self):
        try:
            _ = TaskController().get(0)        
        except HTTPException as e:
            self.assertEqual(e.__str__(), "404: Tarefa não encontrada.")