from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.schemas.schemas import CourseCreate, CourseUpdate, StandardResponse
from app.services.course_service import CourseService

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.post("", response_model=StandardResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    service = CourseService(db)
    result = service.create_course(course)
    return StandardResponse(success=True, message="Course created", data={"id": result.id, "title": result.title})

@router.get("", response_model=StandardResponse)
def get_courses(db: Session = Depends(get_db)):
    service = CourseService(db)
    result = service.get_all_courses()
    return StandardResponse(success=True, message="Courses retrieved", data=result)

@router.get("/{id}", response_model=StandardResponse)
def get_course(id: int, db: Session = Depends(get_db)):
    service = CourseService(db)
    result = service.get_course_by_id(id)
    return StandardResponse(success=True, message="Course retrieved", data=result)

@router.put("/{id}", response_model=StandardResponse)
def update_course(id: int, course: CourseUpdate, db: Session = Depends(get_db)):
    service = CourseService(db)
    result = service.update_course(id, course)
    return StandardResponse(success=True, message="Course updated", data={"id": result.id})

@router.delete("/{id}", response_model=StandardResponse)
def delete_course(id: int, db: Session = Depends(get_db)):
    service = CourseService(db)
    service.delete_course(id)
    return StandardResponse(success=True, message="Course deleted")