from typing import List, Optional
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    
class User(BaseModel):
    id: Optional[UUID]
    first_name: str
    last_name: str
    gender: Gender
    roles: List[Role]

class UpdateUser(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    roles: Optional[List[Role]]