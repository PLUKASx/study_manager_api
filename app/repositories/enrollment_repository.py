from sqlalchemy.orm import Session
from app.models.entities import Enrollment

class EnrollmentRepository:
    def __init__(self, db: Session):
        self.db = db

    def check_duplicate(self, user_id: int, course_id: int):
        return self.db.query(Enrollment).filter(
            Enrollment.user_id == user_id, 
            Enrollment.course_id == course_id
        ).first()

    def create(self, user_id: int, course_id: int):
        new_enrollment = Enrollment(user_id=user_id, course_id=course_id)
        self.db.add(new_enrollment)
        self.db.commit()
        self.db.refresh(new_enrollment)
        return new_enrollment