import unittest
import requests

class TestPersonEndpointsIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Gera token de autenticação
        cls.token = requests.post(
            "http://localhost:8000/token",
            data={"username": "user", "password": "password"}
        ).json()["access_token"]
        cls.headers = {"Authorization": f"Bearer {cls.token}"}

        # Cria uma pessoa auxiliar
        person_data = {
            "name": "Test User",
            "email": "testuser@example.com",
            "phone": "123456789"
        }
        response = requests.post("http://localhost:8000/person/create", json=person_data, headers=cls.headers)
        cls.person_id = response.json()["id"]

    def test_get_person_by_id(self):
        response = requests.get(f"http://localhost:8000/person/{self.person_id}", headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Test User")

    def test_update_person(self):
        updated_data = {
            "name": "Updated User",
            "email": "updateduser@example.com",
            "phone": "987654321"
        }
        response = requests.post(f"http://localhost:8000/person/update/{self.person_id}", json=updated_data, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Pessoa atualizada com sucesso", response.json()["message"])

    def test_create_person_with_invalid_data(self):
        # Email como número, que deve gerar erro de validação
        invalid_data = {
            "name": "Invalid Person",
            "email": 123,
            "phone": "123456789"
        }
        response = requests.post("http://localhost:8000/person/create", json=invalid_data, headers=self.headers)
        self.assertEqual(response.status_code, 422)

    def test_get_nonexistent_person(self):
        response = requests.get("http://localhost:8000/person/99999", headers=self.headers)
        self.assertEqual(response.status_code, 404)
        self.assertIn("Pessoa não encontrada", response.json()["detail"])

    def test_delete_person(self):
        # Cria uma nova pessoa só para deletar
        temp_data = {
            "name": "Temp Person",
            "email": "temp@example.com",
            "phone": "000000000"
        }
        create_resp = requests.post("http://localhost:8000/person/create", json=temp_data, headers=self.headers)
        temp_id = create_resp.json()["id"]

        delete_resp = requests.delete(f"http://localhost:8000/person/delete/{temp_id}", headers=self.headers)
        self.assertEqual(delete_resp.status_code, 200)
        self.assertIn("Pessoa deletada com sucesso", delete_resp.json()["message"])
