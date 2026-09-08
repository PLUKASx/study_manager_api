# StudyManager API
# PEDRO LUCAS DE SIQUEIRA ALEXANDRIA, 2411558.

Uma API RESTful desenvolvida para o gerenciamento de Usuários, Cursos e Matrículas, aplicando os princípios de **Clean Architecture** e **Clean Code**. 

Este projeto foi construído com **FastAPI** e **SQLAlchemy** (ORM), utilizando **SQLite** como banco de dados.

# Justificativa da Arquitetura (Clean Architecture)

A estrutura do projeto foi organizada visando a separação clara de responsabilidades e o isolamento das regras de negócio. A camada de **controllers** lida exclusivamente com o tráfego HTTP e roteamento. O núcleo da aplicação reside na camada de **services** (Use Cases), que orquestra as regras de negócio de forma agnóstica ao banco de dados. O acesso aos dados é abstraído pela camada de **repositories**, que é a única responsável por interagir com os **models** do SQLAlchemy e a **infrastructure**. Essa organização facilita testes, manutenção e a evolução do código, garantindo que controladores não contenham lógica de negócio e que os dados trafeguem validados pelos **schemas** (DTOs).

# Bibliotecas Python Utilizadas:
**fastapi:** Framework web moderno e de altíssimo desempenho para a construção da API.

**uvicorn:** Servidor ASGI ultrarrápido utilizado para rodar a aplicação FastAPI.

**sqlalchemy:** ORM (Object Relational Mapper) utilizado para modelar e interagir com o banco de dados relacional.

**pydantic:** Utilizado para validação rigorosa de dados (Schemas/DTOs) de entrada e saída.

**email-validator:** Dependência exigida pelo Pydantic para a validação precisa e confiável do tipo EmailStr.

# Extensões Recomendadas (VS Code)
Python + SQLite Viewer