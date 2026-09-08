from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.schemas.schemas import UserCreate, UserUpdate, StandardResponse
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("", response_model=StandardResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    result = service.create_user(user)
    return StandardResponse(success=True, message="User created", data={"id": result.id, "name": result.name})

@router.get("", response_model=StandardResponse)
def get_users(db: Session = Depends(get_db)):
    service = UserService(db)
    result = service.get_all_users()
    return StandardResponse(success=True, message="Users retrieved", data=result)

@router.get("/{id}", response_model=StandardResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    result = service.get_user_by_id(id)
    return StandardResponse(success=True, message="User retrieved", data=result)

@router.put("/{id}", response_model=StandardResponse)
def update_user(id: int, user: UserUpdate, db: Session = Depends(get_db)):
    service = UserService(db)
    result = service.update_user(id, user)
    return StandardResponse(success=True, message="User updated", data={"id": result.id})

@router.delete("/{id}", response_model=StandardResponse)
def delete_user(id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    service.delete_user(id)
    return StandardResponse(success=True, message="User deleted")

# Endpoint Relacional
@router.get("/{id}/courses", response_model=StandardResponse)
def get_user_courses(id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    result = service.get_user_courses(id)
    return StandardResponse(success=True, message="User courses retrieved", data=result)