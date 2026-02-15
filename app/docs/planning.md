# Scheduling System – Initial Planning

## Domain Entities

### User

- Represents a client who schedules appointments

### Professional

- Represents the service provider

### Appointment

- Represents a scheduled meeting between user and professional

## Initial Thoughts

- No authentication in first version
- Focus on scheduling

## Services (Business Logic)

### SchedulingService

- Responsible for appointment rules
- Validates time conflicts
- Checks professional availability
- Centralizes scheduling logic

### UserService

- Handles user-related rules
- Prevents duplicate users (future)

### ProfessionalService

- Handles professional availability
- Manages working hours (future)

## Scope – Version 1

- Create users
- Create professionals
- Create appointments
- Prevent time conflicts

## Out of Scope (for now)

- Authentication and authorization
- Payments
- Notifications
- External integrations

### SchedulingService

- Owns all appointment validation rules
- No business rules in controllers
