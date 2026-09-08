from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.user_repository import UserRepository
from app.schemas.schemas import UserCreate, UserUpdate

class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def create_user(self, data: UserCreate):
        if self.repo.get_by_email(data.email):
            raise HTTPException(status_code=400, detail="Email already exists")
        return self.repo.create(data.model_dump())

    def get_all_users(self):
        return self.repo.get_all()

    def get_user_by_id(self, user_id: int):
        user = self.repo.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def update_user(self, user_id: int, data: UserUpdate):
        user = self.get_user_by_id(user_id)
        if data.email and data.email != user.email:
            if self.repo.get_by_email(data.email):
                raise HTTPException(status_code=400, detail="Email already in use")
        return self.repo.update(user, data.model_dump(exclude_unset=True))

    def delete_user(self, user_id: int):
        user = self.get_user_by_id(user_id)
        self.repo.delete(user)

    # Consulta Relacional
    def get_user_courses(self, user_id: int):
        user = self.get_user_by_id(user_id)
        courses = [enrollment.course for enrollment in user.enrollments]
        return {
            "user": {"id": user.id, "name": user.name, "email": user.email},
            "courses": [{"id": c.id, "title": c.title, "workload": c.workload} for c in courses]
        }