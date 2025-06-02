from pydantic import BaseModel, Field, field_validator
from datetime import date

class TaskBody(BaseModel):
    title: str = Field(..., title="Task title", min_length=1, max_length=255)
    description: str = Field(..., title="Task description", min_length=1)
    deadline: date = Field(..., title="Task deadline")
    priority: str = Field(..., title="Task priority", min_length=1, max_length=100)
    status: str = Field(..., title="Task status", min_length=1, max_length=100)
    id_person: int | None = Field(..., title="Person id")

    @field_validator('deadline')
    def validate_deadline(cls, value):
        if value < date.today():
            raise ValueError("A data deve ser no futuro.")
        return value
    
    @field_validator('priority')
    def validate_priority(cls, value):
        if value not in ['low', 'medium', 'high']:
            raise ValueError("A prioridade deve ser low, medium ou high.")
        return value
    
    @field_validator('status')
    def validate_status(cls, value):
        if value not in ['pending', 'inProgress', 'done']:
            raise ValueError("O status deve ser pending, inProgress ou done.")
        return value
