# CHANGES.md – Refactoring Summary

##  Major Issues Identified in Legacy Code

1. All code was in a single file (`app.py`) – hard to maintain
2. No password hashing – stored passwords in plain text
3. Vulnerable to SQL injection – used f-strings directly in queries
4. No input validation – could break with missing/invalid data
5. Inconsistent responses – used plain strings instead of JSON
6. Repeated database logic – not reusable
7. No separation of concerns – routes, logic, and DB mixed together

---

## Improvements Made

### 1. Code Structure
- Split code into folders: `routes/`, `controllers/`, `models/`, and `utils/`
- Used Flask Blueprints to organize routes

### 2. Security
- Implemented password hashing using `werkzeug.security`
- Replaced raw SQL strings with parameterized queries to prevent SQL injection

### 3. Validation
- Added input checks for required fields like `name`, `email`, and `password`
- Created a `validators.py` helper function

### 4. Best Practices
- Proper JSON responses and HTTP status codes
- Clear error messages
- Reusable controller functions

### 5. Testing
- Tested all endpoints using Postman
- Verified GET, POST, PUT, DELETE, and login functionality

---

## Assumptions

- Emails are not unique (original DB allowed duplicates)
- No session/token-based login needed (kept basic login for now)
- SQLite is used for simplicity; production may require PostgreSQL or MySQL

---

## If I Had More Time

- Add JWT authentication or session-based login
- Add email uniqueness constraint
- Write more unit tests
- Add pagination for `/users` and `/search`
- Dockerize the app for easier deployment

---

## AI Tools Used

- ChatGPT was used to guide the refactoring process
- All code was tested, edited, and validated manually before submission
