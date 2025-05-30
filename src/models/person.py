from pydantic import BaseModel, Field, field_validator

class PersonBody(BaseModel):
    name: str = Field(..., title="Person name", min_length=1, max_length=255)
    email: str = Field(..., title="Person email", min_length=1, max_length=255)
    phone: str = Field(..., title="Person phone", min_length=1, max_length=255)
    
    @field_validator('email')
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError("Email inválido.")
        if "." not in value:
            raise ValueError("Email inválido.")
        return value
    
    @field_validator('phone')
    def validate_phone(cls, value):
        if len(value) != 11:
            raise ValueError("Telefone inválido.")
        if not value.isdigit():
            raise ValueError("Telefone inválido.")
        return value