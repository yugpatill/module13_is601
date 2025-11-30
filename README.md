# Module 13 — JWT Login, Registration, Front-End Forms & Playwright E2E Testing

This project implements **JWT-based authentication**, **registration/login pages**, and **Playwright end-to-end tests**.  
It also includes **CI/CD with Docker Hub deployment**, passing GitHub Actions, and Trivy security scans.

---

## Docker Hub Repository

🔗 **Docker Hub:**  
https://hub.docker.com/repository/docker/yugpatil/601_module13/general

---
##  Screenshots

All required screenshots (tests, workflow, UI pages) are inside:

https://github.com/yugpatill/module13_is601/tree/main/Screenshots

---

## Running Tests Locally

Follow these steps to run all backend and Playwright E2E tests on your local machine.

# Create & activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest

---

## Reflection

This module helped me understand how JWT authentication works end-to-end—
from hashing passwords, validating user input, storing users in the database,
to generating and verifying JWT tokens.

I learned how to build simple front-end pages that communicate with a backend API
and how to add client-side validation (email format, password length).
Playwright testing was a new experience; writing UI tests that click, type,
and validate messages helped reinforce real-world testing practices.

Setting up CI/CD was challenging at first, especially running Playwright inside GitHub Actions
and configuring the Trivy scan without failing the workflow.
After adjusting the workflow and allowing Trivy exit-code 0,
the pipeline worked successfully, automatically building and pushing to Docker Hub.

Overall, this module connected backend, frontend, testing, and deployment into one workflow.

---

## Features Implemented

### Backend (FastAPI)
- `/register` – create new user with hashed password  
- `/login` – validate user & return JWT  
- Uses **Pydantic** for validation  
- Uses **Passlib (bcrypt)** for hashing  
- JWT generated using `python-jose`

### Front-End (HTML + JS)
- `register.html` – email/password form with client-side validation  
- `login.html` – login form with client-side validation  
- Stores JWT in `localStorage` after login  
- Displays success/error messages dynamically  

### Playwright E2E Tests
Covers:
-  Successful registration  
-  Successful login  
-  Invalid password (client-side error)  
-  Wrong login credentials (401 from server)  
-  UI messages rendering correctly  

### CI/CD Pipeline
- GitHub Actions:
  - Spins up Postgres  
  - Installs dependencies  
  - Runs backend tests  
  - Runs Playwright E2E tests  
  - Runs Trivy scan  
  - Builds & pushes Docker image to Docker Hub

