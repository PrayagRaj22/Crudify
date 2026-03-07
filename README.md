<div align='center'>

# CRUDIFY

</div>

# Simple CRUD API

## v1.0.2-alpha

A lightweight RESTful API that implements basic **Create, Read, Update, Delete (CRUD)** operations.
Built to demonstrate clean architecture, API design fundamentals, and scalable backend patterns.

---

## Features

- Create new records
- Retrieve single or multiple records
- Update existing records
- Delete records
- RESTful routing conventions
- Structured error handling
- Input validation
- Environment-based configuration

---

## Tech Stack

- Backend: FastAPI
- Database: MongoDB
- ORM/ODM: Mongoose
- API Testing: Postman
- CI/CD: GitHub Actions

---

## Installation

```bash
# Clone repository
git clone https://github.com/dsrathore1/Crudify.git

# Navigate to project
cd Crudify

# Install dependencies
pip install --no-cache-dir -r requirements.txt

# Run the server
uvicorn main:app --reload

# Server run on:
http://localhost:8080
```

# Future Improvements

- Pagination & filtering
- Rate limiting
- Caching layer
- Unit & integration testing
- Dockerization
- CI/CD pipeline
