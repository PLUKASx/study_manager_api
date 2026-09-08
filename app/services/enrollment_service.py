from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.enrollment_repository import EnrollmentRepository
from app.repositories.user_repository import UserRepository
from app.repositories.course_repository import CourseRepository
from app.schemas.schemas import EnrollmentCreate

class EnrollmentService:
    def __init__(self, db: Session):
        self.repo = EnrollmentRepository(db)
        self.user_repo = UserRepository(db)
        self.course_repo = CourseRepository(db)

    def create_enrollment(self, data: EnrollmentCreate):
        # Valida se usuário existe
        if not self.user_repo.get_by_id(data.user_id):
            raise HTTPException(status_code=404, detail="User not found")
            
        # Valida se curso existe
        if not self.course_repo.get_by_id(data.course_id):
            raise HTTPException(status_code=404, detail="Course not found")
            
        # Valida matrícula duplicada
        if self.repo.check_duplicate(data.user_id, data.course_id):
            raise HTTPException(status_code=400, detail="User is already enrolled in this course")

        return self.repo.create(data.user_id, data.course_id)