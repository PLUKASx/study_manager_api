from pydantic import BaseModel, EmailStr
from typing import Optional, Any


class StandardResponse(BaseModel):
    success: bool
    message: str
    data: Optional[Any] = None

# Usuários
class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None

# Cursos
class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None
    workload: int

class CourseCreate(CourseBase):
    pass

class CourseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    workload: Optional[int] = None

# Matrículas
class EnrollmentCreate(BaseModel):
    user_id: int
    course_id: int