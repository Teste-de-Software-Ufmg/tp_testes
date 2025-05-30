from src.repositories import PersonRepository
from src.models import PersonBody
from fastapi import HTTPException

class PersonService:
    def __init__(self) -> None:
        self.__repository = PersonRepository()

    def create(self, person_data: PersonBody) -> dict:
        return self.__repository.create(person_data)
    
    def get(self, person_data: PersonBody) -> dict:
        person = self.__repository.get(person_data)
        if not person:
            raise HTTPException(status_code=404, detail="Pessoa não encontrada.")
        return person
    
    def delete(self, id: int) -> dict:
        person = self.__repository.get(id)
        if not person:
            raise HTTPException(status_code=404, detail="Pessoa não encontrada.")
        return self.__repository.delete(id)
    
    def update(self, id: int, person_data: PersonBody) -> dict:
        person = self.__repository.get(id)
        if not person:
            raise HTTPException(status_code=404, detail="Pessoa não encontrada.")
        return self.__repository.update(id, person_data)