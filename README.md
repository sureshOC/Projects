# 🔐 FastAPI Authentication System

A production-style backend project implementing **User Authentication, JWT-based authorization, Role-Based Access Control (RBAC), and PostgreSQL integration**.

---

## 🚀 Features

* User Registration & Login
* Password Hashing using bcrypt
* JWT Authentication (Access Token)
* Role-Based Access Control (Admin/User)
* Protected Routes using FastAPI dependencies
* PostgreSQL + SQLAlchemy ORM
* Clean project structure (routes, schemas, dependencies)

---

## 🛠 Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Passlib (bcrypt)
* Python-JOSE (JWT)

---

## 📂 Project Structure

```
app/
 ├── routes/
 │    ├── auth.py
 │    └── users.py
 ├── auth.py
 ├── database.py
 ├── dependencies.py
 ├── models.py
 ├── schemas.py
 └── main.py
```

---

## ⚙️ Setup Instructions

### 1. Clone repo

```
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Create virtual env

```
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Setup environment variables

Create `.env`:

```
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

### 5. Run server

```
uvicorn app.main:app --reload
```

---

## 🔑 API Endpoints

### Auth

* `POST /auth/register`
* `POST /auth/login`

### User

* `GET /users/me` (Protected)

### Admin

* `GET /users/admin` (Admin only)

---

## 🔐 Authentication Flow

1. User registers → password hashed
2. User logs in → JWT token generated
3. Token passed in header:

   ```
   Authorization: Bearer <token>
   ```
4. Backend verifies token
5. Role checked for protected routes

---

## 📌 Future Improvements

* Refresh Tokens
* Docker deployment
* Logging & monitoring
* Unit tests

---

## 💡 Author

Suresh – Backend Developer (in progress 🚀)
