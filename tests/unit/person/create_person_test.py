import unittest
from src.controllers import PersonController
from src.models import PersonBody
from src.database import Base, engine

Base.metadata.create_all(bind=engine)

class TestCreatePerson(unittest.TestCase):
    def test_create_person_with_valid_data(self):
        person_data = PersonBody(
            name="New Person", email="teste@teste.com", phone="12345678901"
        )

        result = PersonController().create(person_data)
        self.assertEqual(result['name'], "New Person")
        self.assertEqual(result['email'], "teste@teste.com")
        self.assertEqual(result['phone'], "12345678901")
        self.assertIn('id', result)

    def test_create_person_with_phone_error(self):
        try:
            _ = PersonBody(
                name="New Person", email="teste@teste.com", phone="fd")
        except ValueError as e:
            error = str(e).split("\n")
            self.assertEqual(error[0], "1 validation error for PersonBody")
            self.assertIn("Telefone inválido", error[2])
    
    def test_create_person_with_invalid_phone_value_error(self):
        try:
            _ = PersonBody(
                name="New Person", email="teste@teste.com", phone="fffffffffff")
        except ValueError as e:
            error = str(e).split("\n")
            self.assertEqual(error[0], "1 validation error for PersonBody")
            self.assertIn("Telefone inválido", error[2])

    def test_create_person_with_email_error(self):
        try:
            _ = PersonBody(
                name="New Person", email="teste", phone="12345678901"
            )
        except ValueError as e:
            error = str(e).split("\n")
            self.assertEqual(error[0], "1 validation error for PersonBody")
            self.assertIn("Email inválido", error[2])
    
    def test_create_person_with_email_sintax_error(self):
        try:
            _ = PersonBody(
                name="New Person", email="teste@", phone="12345678901"
            )
        except ValueError as e:
            error = str(e).split("\n")
            self.assertEqual(error[0], "1 validation error for PersonBody")
            self.assertIn("Email inválido", error[2])

    
    def test_create_person_with_name_empty_error(self):
        try:
            _ = PersonBody(
                name=" ", email="teste@teste.com", phone="12345678901"
            )
        except ValueError as e:
            error = str(e).split("\n")
            self.assertEqual(error[0], "1 validation error for PersonBody")
            self.assertIn("Nome não pode ser vazio.", error[2])
    
    def test_create_person_with_email_empty_error(self):
        try:
            _ = PersonBody(
                name="New Person", email=" ", phone="12345678901"
            )
        except ValueError as e:
            error = str(e).split("\n")
            self.assertEqual(error[0], "1 validation error for PersonBody")
            self.assertIn("Email não pode ser vazio.", error[2])
    
    def test_create_person_with_phone_empty_error(self):
        try:
            _ = PersonBody(
                name="New Person", email="teste@teste.com", phone=" "
            )
        except ValueError as e:
            error = str(e).split("\n")
            self.assertEqual(error[0], "1 validation error for PersonBody")
            self.assertIn("Telefone não pode ser vazio.", error[2])
