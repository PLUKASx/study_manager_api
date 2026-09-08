from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from sqlalchemy.exc import IntegrityError

from app.infrastructure.database import engine, Base
from app.controllers import user_controller, course_controller, enrollment_controller

# Cria o banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI(title="StudyManager API")


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"success": False, "message": str(exc.detail), "data": None}
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"success": False, "message": "Validation Error: Verifique os dados enviados.", "data": exc.errors()}
    )


@app.exception_handler(IntegrityError)
async def integrity_exception_handler(request: Request, exc: IntegrityError):
    return JSONResponse(
        status_code=400,
        content={"success": False, "message": "Erro de integridade: Registro já existe ou é inválido.", "data": None}
    )


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"success": False, "message": f"Erro interno do servidor: {str(exc)}", "data": None}
    )


@app.get("/", tags=["Home"])
def read_root():
    return {"message": "Bem-vindo à StudyManager API! Acesse /docs para ver a documentação."}


app.include_router(user_controller.router)
app.include_router(course_controller.router)
app.include_router(enrollment_controller.router)