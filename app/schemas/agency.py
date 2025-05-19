from uuid import uuid4

from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

from utils.enums import Plans, Status

class AgencyBase(BaseModel):
    nome: str = Field(..., title="Nome fantasia da agência")
    cnpj: str = Field(..., title="CNPJ da agência")
    email: EmailStr
    telefone: str
    plano: str = Plans.FREE
    status: str = Status.ACTIVE

class AgencyCreate(AgencyBase):
    pass

class AgencyInDB(AgencyBase):
    id: str = Field(default_factory=lambda: str(uuid4()), title="ID da agência")
    data_criacao: datetime = Field(default_factory=datetime.utcnow, title="Data de criação da agência")

    class Config:
        orm_mode = True
