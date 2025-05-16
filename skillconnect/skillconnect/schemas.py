from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

class ServiceCreate(BaseModel):
    title: str
    description: str
    provider_id: int

class ServiceOut(BaseModel):
    id: int
    title: str
    description: str
    provider_id: int

    class Config:
        orm_mode = True