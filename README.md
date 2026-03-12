# Bank and Branch Management API

## Overview

This project is a RESTful API built using **FastAPI** to manage banks and their branches.
The API allows users to create banks, add branches, and retrieve branch information associated with specific banks.

The application follows a modular backend architecture with separate layers for routers, services (business logic), models, and database configuration.

---

## Technologies Used

* Python 3.13
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* Pytest
* Docker
* Uvicorn

---

## Project Structure

```
Bank_API
│
├── app
│   ├── routers
│   │   ├── banks.py
│   │   └── branches.py
│   │
│   ├── services
│   │   ├── bank_service.py
│   │   └── branch_service.py
│   │
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── config.py
│   └── main.py
│
├── tests
│   ├── conftest.py
│   ├── test_banks.py
│   └── test_branches.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Features

* Create a bank
* Retrieve all banks
* Retrieve a bank by ID
* Create a branch
* Retrieve a branch by ID
* Retrieve all branches belonging to a specific bank
* Automated API tests using pytest
* Dockerized application
* Deployed cloud API

---

## API Endpoints

### Banks

Create Bank

POST /banks

Example Request

```
{
  "name": "State Bank"
}
```

Retrieve All Banks

GET /banks

Retrieve Bank by ID

GET /banks/{bank_id}

---

### Branches

Create Branch

POST /branches

Example Request

```
{
  "name": "Hyderabad Branch",
  "bank_id": 1
}
```

Retrieve Branch by ID

GET /branches/{branch_id}

Retrieve All Branches for a Bank

GET /banks/{bank_id}/branches

---

## Running the Project Locally

1. Clone the repository

```
git clone https://github.com/yourusername/bank-api-fastapi.git
```

2. Navigate into the project

```
cd bank-api-fastapi
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Run the application

```
uvicorn app.main:app --reload
```

5. Access API documentation

```
http://localhost:8000/docs
```

---

## Running with Docker

Build and run containers

```
docker compose up --build
```

The API will be available at

```
http://localhost:8000
```

---

## Testing

The project includes automated tests using **pytest**.

To run the tests:

```
pytest
```

Test coverage includes:

* Bank creation
* Bank retrieval
* Branch creation
* Branch retrieval
* Retrieving branches belonging to a bank

---

## Deployment

The API is deployed on a cloud platform and can be accessed at:

```
https://bank-api-tyml.onrender.com
```

Interactive API documentation:

```
https://bank-api-tyml.onrender.com/docs
```

---

## Design Approach

The API follows a layered backend architecture:

Router Layer
Handles incoming HTTP requests and responses.

Service Layer
Contains business logic and database operations.

Model Layer
Defines database tables using SQLAlchemy ORM.

Schema Layer
Defines request and response validation using Pydantic.

Database Layer
Handles database connection and session management.

Service Layer

The services layer contains the business logic of the application.

bank_service.py
Handles operations related to banks such as creating banks, retrieving banks, and retrieving branches for a specific bank.

branch_service.py
Handles branch-related operations such as creating branches and retrieving branch details.

Separating business logic from routers improves code organization, testability, and maintainability.

This structure keeps the code modular, maintainable, and scalable.

---

## Time Taken

The assignment was completed over **three days**.
This time included:

* Designing the API structure
* Implementing the bank and branch endpoints
* Creating the service layer for business logic
* Writing automated tests using pytest
* Containerizing the application with Docker
* Deploying the API and testing the endpoints


