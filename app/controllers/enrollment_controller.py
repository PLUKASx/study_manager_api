from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.schemas.schemas import EnrollmentCreate, StandardResponse
from app.services.enrollment_service import EnrollmentService

router = APIRouter(prefix="/enrollments", tags=["Matrículas"])

@router.post("", response_model=StandardResponse)
def create_enrollment(enrollment: EnrollmentCreate, db: Session = Depends(get_db)):
    service = EnrollmentService(db)
    result = service.create_enrollment(enrollment)
    return StandardResponse(success=True, message="Enrollment successful", data={"id": result.id})