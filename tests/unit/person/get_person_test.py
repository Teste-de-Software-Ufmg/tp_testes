import unittest
from fastapi import HTTPException
from src.controllers import PersonController
from src.database import Base, engine

Base.metadata.create_all(bind=engine)

class TestGetPerson(unittest.TestCase):

    def test_get_person(self):
        try:
            _ = PersonController().get(0)        
        except HTTPException as e:
            self.assertEqual(e.__str__(), "404: Pessoa não encontrada.")