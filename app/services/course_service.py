from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.course_repository import CourseRepository
from app.schemas.schemas import CourseCreate, CourseUpdate

class CourseService:
    def __init__(self, db: Session):
        self.repo = CourseRepository(db)

    def create_course(self, data: CourseCreate):
        return self.repo.create(data.model_dump())

    def get_all_courses(self):
        return self.repo.get_all()

    def get_course_by_id(self, course_id: int):
        course = self.repo.get_by_id(course_id)
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")
        return course

    def update_course(self, course_id: int, data: CourseUpdate):
        course = self.get_course_by_id(course_id)
        return self.repo.update(course, data.model_dump(exclude_unset=True))

    def delete_course(self, course_id: int):
        course = self.get_course_by_id(course_id)
        self.repo.delete(course)