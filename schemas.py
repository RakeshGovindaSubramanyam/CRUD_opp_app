from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class User(BaseModel):
    id: int
    email: str
    is_active: bool

    class Config:
        orm_mode = True

class TaskCreate(BaseModel):
    title: str
    description: str

class Task(BaseModel):
    id: int
    title: str
    description: str
    owner_id: int

    class Config:
        orm_mode = True