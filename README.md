

## README.md 

```
# User Management System – Refactored

This is a refactored version of a basic user management API using Flask and SQLite.

The project includes endpoints to:
- Create a user
- Get all users
- Get a user by ID
- Update a user
- Delete a user
- Search users by name
- Login using email and password

All passwords are now securely hashed. The code has been cleaned up, modularized, and made secure by preventing SQL injection and validating inputs.

---

## How to Run

1. Clone this project or download it
2. Open terminal and navigate to the project folder

3. Create virtual environment:
```

python -m venv venv
venv\Scripts\activate   (for Windows)

```

4. Install dependencies:
```

pip install -r requirements.txt

```

5. Initialize database:
```

python init\_db.py

```

6. Start the Flask server:
```

python app.py

```

Now open your browser or Postman at:
```

[http://localhost:5009](http://localhost:5009)

```

---

## Sample Login

Use this to test login:
- Email: john@example.com
- Password: password123

---

## Tech Used

- Python 3
- Flask
- SQLite
- Werkzeug (for password hashing)

---

## Author

Buthuru Venkat Reddy  

