import unittest
import requests


class TestPersonIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.token = requests\
            .post("http://localhost:8000/token", data={"username": "user", "password": "password"})\
            .json()\
            .get("access_token")

        cls.headers = {"Authorization": f"Bearer {cls.token}"}

        # Cria uma pessoa para os testes
        person_data = {
            "name": "João da Silva",
            "email": "joao@example.com",
            "phone": "11999999999"
        }

        response = requests\
            .post("http://localhost:8000/person/create", json=person_data, headers=cls.headers)

        if response.status_code != 200:
            raise Exception(f"Falha ao criar pessoa para testes. Status: {response.status_code}, body: {response.text}")

        cls.person_id = response.json()["id"]

    def test_integration_get_person_by_id(self):
        result = requests.get(
            f"http://localhost:8000/person/{self.person_id}",
            headers=self.headers
        )
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json().get("id"), self.person_id)

    def test_integration_update_person(self):
        updated_data = {
            "name": "João Atualizado",
            "email": "joaoatualizado@example.com",
            "phone": "11888888888"
        }

        result = requests.post(
            f"http://localhost:8000/person/update/{self.person_id}",
            json=updated_data,
            headers=self.headers
        )

        self.assertEqual(result.status_code, 200)
        self.assertIn("Pessoa atualizada com sucesso", result.json()["message"])

    def test_integration_get_person_not_found(self):
        result = requests.get("http://localhost:8000/person/999999", headers=self.headers)
        self.assertEqual(result.status_code, 404)
        self.assertIn("Pessoa não encontrada", result.json()["detail"])

    def test_integration_delete_person(self):
        # Cria pessoa temporária para teste de exclusão
        temp_data = {
            "name": "Pessoa Para Deletar",
            "email": "delete_test@example.com",
            "phone": "11988887777"
        }

        response = requests.post(
            "http://localhost:8000/person/create",
            json=temp_data,
            headers=self.headers
        )

        self.assertEqual(response.status_code, 200, f"Falha ao criar pessoa: {response.text}")
        temp_id = response.json()["id"]

        delete_resp = requests.delete(
            f"http://localhost:8000/person/delete/{temp_id}",
            headers=self.headers
        )

        self.assertEqual(delete_resp.status_code, 200, f"Erro ao deletar pessoa: {delete_resp.text}")
        self.assertIn("Pessoa deletada com sucesso", delete_resp.json()["message"])

    def test_integration_create_person_with_invalid_email(self):
        invalid_data = {
            "name": "Nome Inválido",
            "email": 12345,  # email inválido
            "phone": "11999999999"
        }

        response = requests.post(
            "http://localhost:8000/person/create",
            json=invalid_data,
            headers=self.headers
        )

        self.assertEqual(response.status_code, 422)
