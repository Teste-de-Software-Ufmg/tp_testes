import unittest
from fastapi import HTTPException
from src.controllers import PersonController
from src.models import PersonBody
from src.database import Base, engine

Base.metadata.create_all(bind=engine)

class TestUpdatePerson(unittest.TestCase):

    def test_update_person_with_valid_data(self):
        person_data = PersonBody(
            name="New Person", email="teste@teste.com", phone="12345678901"
        )

        result = PersonController().create(person_data)

        person_data = PersonBody(
            name="New Person 1", email="teste1@teste.com", phone="92345678901"
        )

        id = result['id']
        result = PersonController().update(id, person_data)

        self.assertEqual(result['message'], "Pessoa atualizada com sucesso")

        result2 = PersonController().get(id)

        self.assertEqual(result2['name'], "New Person 1")
        self.assertEqual(result2['email'], "teste1@teste.com")
        self.assertEqual(result2['phone'], "92345678901")

    def test_update_person_with_invalid_id(self):
        try:
            result = PersonController().update(-10, PersonBody(
                name="New Person 1", email="teste@gmail.com", phone="12345678901"
            ))

        except HTTPException as e:
            self.assertEqual(e.__str__(), "404: Pessoa não encontrada.")

        except Exception:
            self.fail("HTTPException not raised")