# Scheduling System API

RESTful API for managing professional appointments, designed for small businesses such as clinics, aesthetic centers, and consulting services.

This project focuses on **domain modeling**, **business rules**, and **clean backend architecture**, aiming to simulate a real-world scheduling system.

---

## 🚀 Features

- Client management
- Professional management
- Service management
- Appointment creation and management
- Automatic time conflict validation
- Appointment status control
- Basic reports

---

## 🎯 Technical Goals

This project was built to practice and demonstrate:

- Layered architecture
- Clear separation of responsibilities
- Isolated business rules
- Data persistence using ORM
- Automated testing of critical rules

---

## 🧠 Core Business Rules

- A professional cannot have overlapping appointments
- Appointment end time is calculated automatically based on service duration
- Appointments cannot be scheduled in the past
- Only active clients, professionals, and services can be used
- Appointment status must be valid
- Cancellations keep historical data
- Rescheduling creates a new appointment and cancels the previous one

---

## 🧱 Tech Stack

- Python 3.11+
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Pytest
- Uvicorn

---

## 🏗️ Project Architecture

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

### Responsibilities

- `models/` → database entities
- `schemas/` → data validation and serialization
- `repositories/` → database access
- `services/` → business rules
- `routers/` → API endpoints
- `validators/` → auxiliary validations
- `tests/` → automated tests

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

Tests focus on:

- Time conflict validation
- Automatic duration calculation
- Past date validation
- Status validation
- Valid appointment creation

---

## 📌 Project Scope

### Included

- Functional API
- Automated tests
- Clean architecture
- Complete documentation
- Swagger UI

### Out of Scope

- Authentication (JWT)
- User management
- Deployment
- Frontend
- Email notifications
- Docker

---

## 📂 Purpose

This project was created as a **portfolio project** to consolidate backend development skills using Python and FastAPI, focusing on real business rules and professional code organization.
