import unittest
from src.controllers import PersonController
from src.models import PersonBody
from src.database import Base, engine
from fastapi import HTTPException

Base.metadata.create_all(bind=engine)

class TestDeletePerson(unittest.TestCase):
    def test_delete_person_with_valid_id(self):
        person_data = PersonBody(
            name="New Person", email="teste@teste.com", phone="12345678901")
        person = PersonController().create(person_data)
        result = PersonController().delete(person['id'])

        self.assertEqual(result, {"message": "Pessoa deletada com sucesso"})

    def test_delete_person_with_invalid_id(self):
        try:
            PersonController().delete(0)
        except HTTPException as e:
            result = e.detail
            status_code = e.status_code

            self.assertEqual(result, "Pessoa não encontrada.")
            self.assertEqual(status_code, 404)