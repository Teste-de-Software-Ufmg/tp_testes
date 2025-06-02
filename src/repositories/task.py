from src.database import SessionLocal
from src.models import TaskBody
from src.database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from datetime import date


class TaskRepository(Base):
    __tablename__ = "task"
    db = SessionLocal()

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(String, nullable=False)
    priority = Column(String, nullable=False)
    deadline = Column(String, nullable=False)
    created_at = Column(String, nullable=False)
    updated_at = Column(String, nullable=False)
    id_person = Column(Integer, ForeignKey("person.id"), nullable=True)

    def create(self, task_data: TaskBody) -> int:
        task = TaskRepository(**task_data.__dict__)
        task.created_at = date.today()
        task.updated_at = date.today()

        self.db.add(task)
        self.db.commit()

        return self.db.query(TaskRepository).order_by(TaskRepository.id.desc()).first().__dict__

    def get(self, id: int) -> dict:
        result = self.db.query(TaskRepository).filter(
            TaskRepository.id == id).first()
        if result:
            return result.__dict__
        return None
    
    def get_all(self) -> list:
        return [task.__dict__ for task in self.db.query(TaskRepository).all()]

    def delete(self, id: int) -> dict:
        task = self.db.query(TaskRepository).filter(
            TaskRepository.id == id).first()
        self.db.delete(task)
        self.db.commit()
        return {"message": "Tarefa deletada com sucesso"}

    def update(self, id: int, task_data: TaskBody) -> dict:
        task = self.db.query(TaskRepository).filter(TaskRepository.id == id).first()

        if task:
            task.title = task_data.title
            task.description = task_data.description
            task.status = task_data.status
            task.priority = task_data.priority
            task.deadline = task_data.deadline
            task.updated_at = date.today()
            self.db.commit()
            return {"message": "Tarefa atualizada com sucesso"}

        return None
    
    def vinculate(self, id: int, person_id: int) -> dict:
        task = self.db.query(TaskRepository).filter(TaskRepository.id == id).first()
        task.id_person = person_id
        self.db.commit()
        return {"message": "Tarefa vinculada com sucesso"}
    
    def conclude(self, id: int) -> dict:
        task = self.db.query(TaskRepository).filter(TaskRepository.id == id).first()
        task.status = "done"
        self.db.commit()
        return {"message": "Tarefa concluída com sucesso"}
