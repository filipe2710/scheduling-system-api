# Scheduling System API

RESTful API for managing professional appointments, designed for small businesses such as clinics, aesthetic centers, and consulting services.

This project focuses on **domain modeling**, **business rule enforcement**, and **clean backend architecture**, simulating a real-world scheduling system with realistic constraints and validation scenarios.

---

## 🚀 Features

- Client management (CRUD)
- Professional management (CRUD)
- Service management (CRUD)
- Appointment creation and management
- Automatic time conflict validation
- Automatic end-time calculation based on service duration
- Appointment status control
- Business rule enforcement
- Automated tests for critical scenarios

---

## 🎯 Technical Goals

This project was built to practice and demonstrate:

- Layered architecture
- Clear separation of responsibilities
- Isolation of business rules from HTTP layer
- Validation and serialization with Pydantic
- Automated testing using Pytest
- Clean and maintainable project structure

---

## 🧠 Core Business Rules

- A professional cannot have overlapping appointments
- Appointment end time is calculated automatically based on service duration
- Appointments cannot be scheduled in the past
- Only active clients, professionals, and services can be used
- Appointment status must be valid
- Cancellations preserve historical data
- Rescheduling creates a new appointment and cancels the previous one

---

## 🧱 Tech Stack

- Python 3.11+
- FastAPI
- Pydantic
- Pytest
- Uvicorn

> Database integration (SQLAlchemy + SQLite) planned for the next phase.

---

## 🏗️ Project Architecture

```
app/
├── main.py
├── core/
├── database/
├── models/
├── schemas/
├── repositories/
├── services/
├── routers/
├── validators/
└── tests/
```

### Responsibilities

- `models/` → Database entities (future ORM layer)
- `schemas/` → Data validation and serialization
- `repositories/` → Database access abstraction (planned)
- `services/` → Business rules and domain logic
- `routers/` → API endpoints (HTTP layer)
- `validators/` → Auxiliary validation logic
- `tests/` → Automated test suite

---

## 🌐 Main Endpoints

### Clients

- POST `/clients`
- GET `/clients`
- GET `/clients/{id}`
- PUT `/clients/{id}`
- DELETE `/clients/{id}`

### Professionals

- Full CRUD

### Services

- Full CRUD

### Appointments

- POST `/appointments`
- GET `/appointments`
- GET `/appointments/{id}`
- PUT `/appointments/{id}`
- PATCH `/appointments/{id}/cancel`
- GET `/appointments/day/{date}`
- GET `/appointments/professional/{id}`

---

## 🧪 Testing

Tests focus on critical business validations:

- Time conflict detection
- Automatic duration calculation
- Past date validation
- Status validation
- Valid appointment creation flow

Run tests with:

```
pytest
```

---

## ▶ How to Run

### 1. Clone the repository

```
git clone <your-repository-url>
cd scheduling-system-api
```

### 2. Create virtual environment

```
python -m venv venv
```

### 3. Activate virtual environment

**Windows:**

```
venv\Scripts\activate
```

**Linux / macOS:**

```
source venv/bin/activate
```

### 4. Install dependencies

```
pip install -r requirements.txt
```

### 5. Run the application

```
uvicorn app.main:app --reload
```

API will be available at:

```
http://localhost:8000
```

Swagger documentation:

```
http://localhost:8000/docs
```

ReDoc documentation:

```
http://localhost:8000/redoc
```

---

## 🧩 Design Decisions

- Layered architecture to separate HTTP, business logic, and data access
- Services contain all domain rules
- Routers handle only HTTP concerns
- Validation logic is isolated for maintainability
- Clear folder structure to simulate scalable backend projects

---

## 🚧 Project Status

In active development.

- Client module completed
- Appointment module under refinement
- Database persistence layer planned

---

## 📌 Project Scope

### Included

- Functional REST API
- Clean architecture
- Business rule enforcement
- Automated tests
- Swagger documentation

### Out of Scope

- Authentication (JWT)
- User management
- Deployment
- Frontend
- Email notifications
- Docker

---

## 📂 Purpose

This project was created as a **portfolio project** to consolidate backend development skills using Python and FastAPI, focusing on realistic business rules and professional backend structure.
