from pydantic import BaseModel
from typing import List, Optional

class Skill(BaseModel):
    id: Optional[int]
    skill: str

class Project(BaseModel):
    id: Optional[int]
    title: str
    description: str
    link: str

class Work(BaseModel):
    id: Optional[int]
    company: str
    role: str
    start_date: str
    end_date: str
    description: str

class Link(BaseModel):
    id: Optional[int]
    type: str
    url: str

class Profile(BaseModel):
    id: Optional[int]
    name: str
    email: str
    education: str
    mobile: str
    address: str
