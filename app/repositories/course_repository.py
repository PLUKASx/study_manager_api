from sqlalchemy.orm import Session
from app.models.entities import Course

class CourseRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Course).all()

    def get_by_id(self, course_id: int):
        return self.db.query(Course).filter(Course.id == course_id).first()

    def create(self, course_data: dict):
        new_course = Course(**course_data)
        self.db.add(new_course)
        self.db.commit()
        self.db.refresh(new_course)
        return new_course

    def update(self, course: Course, update_data: dict):
        for key, value in update_data.items():
            if value is not None:
                setattr(course, key, value)
        self.db.commit()
        self.db.refresh(course)
        return course

    def delete(self, course: Course):
        self.db.delete(course)
        self.db.commit()