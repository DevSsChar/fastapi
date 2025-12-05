# FastAPI Blog API - Complete Tutorial Project

<div align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3.12+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

A comprehensive FastAPI project demonstrating RESTful API development with authentication, database relationships, and best practices.

</div>

---

## 📚 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Development Journey](#-development-journey)
- [API Endpoints](#-api-endpoints)
- [Database Models](#-database-models)
- [Authentication](#-authentication)
- [Credits](#-credits)
- [License](#-license)

---

## 🎯 Overview

This project is a complete blog API built with **FastAPI**, showcasing modern Python web development practices. It includes user authentication, CRUD operations, database relationships, password hashing, and JWT token-based security.

**Original Course:** This project is based on the excellent [FastAPI Course by Bitfumes](https://github.com/bitfumes/fastapi-course), extended with improvements, bug fixes, and enhanced documentation.

---

## ✨ Features

- ✅ RESTful API with FastAPI
- ✅ SQLAlchemy ORM with SQLite
- ✅ User Authentication & Authorization
- ✅ JWT Token-based Security
- ✅ Password Hashing (Argon2)
- ✅ Database Relationships (One-to-Many)
- ✅ Request/Response Models with Pydantic
- ✅ Repository Pattern for Clean Architecture
- ✅ Router-based Modular Design
- ✅ Automatic API Documentation (Swagger UI)
- ✅ Input Validation & Error Handling

---

## 📁 Project Structure

```
fastapi/
├── blog/
│   ├── __init__.py
│   ├── main.py                 # Main application entry point
│   ├── database.py             # Database connection & session
│   ├── models.py               # SQLAlchemy ORM models
│   ├── schemas.py              # Pydantic schemas
│   ├── hashing.py              # Password hashing utilities
│   ├── JWTtoken.py             # JWT token generation
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── blog.py             # Blog endpoints
│   │   ├── user.py             # User endpoints
│   │   └── authentication.py  # Login endpoint
│   └── repository/
│       ├── blog.py             # Blog business logic
│       └── user.py             # User business logic
├── blog.db                     # SQLite database
├── requirements.txt            # Python dependencies
└── readme.md                   # This file
```

---

## 🚀 Installation

### Prerequisites

- Python 3.12+
- pip (Python package manager)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/DevSsChar/fastapi.git
   cd fastapi
   ```

2. **Create virtual environment**
   ```bash
   python -m venv fastapi-env
   ```

3. **Activate virtual environment**
   - **Windows:** 
     ```bash
     fastapi-env\Scripts\activate
     ```
   - **Linux/Mac:**
     ```bash
     source fastapi-env/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   # Make sure you're in the parent directory (not inside blog/)
   uvicorn blog.main:app --reload --host 127.0.0.1 --port 8001
   ```

6. **Access the API**
   - API: http://127.0.0.1:8001
   - Swagger Docs: http://127.0.0.1:8001/docs
   - ReDoc: http://127.0.0.1:8001/redoc

---

## 📖 Development Journey

This section documents the step-by-step development process with commit checkpoints.

### Checkpoint 1: Initial Setup (`14082e8`)
**Commit:** `Initial Information`

**What was done:**
- Project initialization
- Basic FastAPI application setup
- First endpoint created

**Files Created:**
- `main.py` - Initial FastAPI app

**Code:**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"message": "Hello World"}
```

**Theory:**
FastAPI is a modern, fast web framework for building APIs with Python 3.7+ based on standard Python type hints. It's built on Starlette for web parts and Pydantic for data validation.

---

### Checkpoint 2: Dynamic Endpoints (`0983b8c`)
**Commit:** `For dynamic endpointwise`

**What was done:**
- Path parameters implementation
- Dynamic route handling

**Code Example:**
```python
@app.get('/blog/{id}')
def show(id: int):
    return {"data": id}
```

**Theory:**
Path parameters allow you to capture values from the URL path. FastAPI automatically validates and converts the types (e.g., `id: int`).

---

### Checkpoint 3: Query Parameters (`5e7bcd9`)
**Commit:** `Query Parameters`

**What was done:**
- Query parameter handling
- Optional parameters with defaults

**Code Example:**
```python
@app.get('/blog')
def index(limit: int = 10, published: bool = True):
    if published:
        return {"data": f"{limit} published blogs"}
    return {"data": f"{limit} blogs"}
```

**Theory:**
Query parameters are optional key-value pairs that appear after `?` in URLs. They're commonly used for filtering, pagination, and search.

---

### Checkpoint 4: Request Body (`84552f0`)
**Commit:** `Rqeust body`

**What was done:**
- Pydantic models for request validation
- POST endpoint creation

**Files:**
- `schemas.py`

**Code:**
```python
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str

@app.post('/blog')
def create(request: Blog):
    return {"data": f"Blog created with title: {request.title}"}
```

**Theory:**
Pydantic models provide automatic request validation, serialization, and documentation. FastAPI uses these to validate incoming JSON data.

---

### Checkpoint 5: Database Connection (`edf702c`)
**Commit:** `Database connection done`

**What was done:**
- SQLAlchemy setup
- Database engine configuration
- Session management

**Files:**
- `database.py`
- `models.py`

**Code (`database.py`):**
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

**Code (`models.py`):**
```python
from sqlalchemy import Column, Integer, String
from .database import Base

class Blog(Base):
    __tablename__ = "blogs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
```

**Theory:**
- **SQLAlchemy:** Python SQL toolkit and ORM
- **Engine:** Manages database connections
- **Session:** Handles database transactions
- **Base:** Declarative base class for models

---

### Checkpoint 6: CRUD Operations (`ab0c6fb`, `e8b09d6`)
**Commits:** `Read and Create operations done`, `CRUD Operations done`

**What was done:**
- Create (POST) - Add new blogs
- Read (GET) - Retrieve blogs
- Update (PUT) - Modify existing blogs
- Delete (DELETE) - Remove blogs

**Code Examples:**
```python
# Create
@app.post('/blog')
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# Read All
@app.get('/blog')
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

# Read One
@app.get('/blog/{id}')
def show(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

# Update
@app.put('/blog/{id}')
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=404, detail="Blog not found")
    blog.update({'title': request.title, 'body': request.body})
    db.commit()
    return {"detail": "Blog updated"}

# Delete
@app.delete('/blog/{id}')
def destroy(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=404, detail="Blog not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail": "Blog deleted"}
```

**Theory:**
- **CRUD:** Create, Read, Update, Delete - fundamental database operations
- **Depends:** FastAPI dependency injection for database sessions
- **HTTPException:** Proper error handling with status codes

---

### Checkpoint 7: Response Models (`69cc4cc`)
**Commit:** `Response models`

**What was done:**
- Pydantic response models for data serialization
- API response standardization

**Code (`schemas.py`):**
```python
class ShowBlog(BaseModel):
    title: str
    body: str
    
    class Config:
        from_attributes = True  # Allows ORM model conversion

@app.get('/blog/{id}', response_model=ShowBlog)
def show(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog
```

**Theory:**
Response models ensure that only specified fields are returned to clients. The `from_attributes = True` (formerly `orm_mode = True`) allows Pydantic to work with SQLAlchemy ORM models.

---

### Checkpoint 8: User Creation (`3b23708`)
**Commit:** `User Creation`

**What was done:**
- User model creation
- User registration endpoint

**Code (`models.py`):**
```python
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
```

**Code (`main.py`):**
```python
@app.post('/user')
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=request.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
```

---

### Checkpoint 9: Password Hashing (`81edf5d`)
**Commit:** `Password hashing`

**What was done:**
- Password hashing with Argon2
- Secure password storage

**Files:**
- `hashing.py`

**Code:**
```python
from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["argon2"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)
    
    def verify(hashed_password: str, plain_password: str):
        return pwd_cxt.verify(plain_password, hashed_password)
```

**Usage:**
```python
@app.post('/user')
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    hashed_password = Hash.bcrypt(request.password)
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
```

**Theory:**
- **Argon2:** Modern password hashing algorithm, more secure than bcrypt
- **Why hash?** Never store plain text passwords - if database is compromised, user passwords remain safe
- **One-way function:** You can't reverse a hash back to the original password

---

### Checkpoint 10: Database Relationships (`b877bd2`)
**Commit:** `Relationships done`

**What was done:**
- One-to-Many relationship between User and Blog
- Foreign key implementation

**Code (`models.py`):**
```python
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = "blogs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    user = relationship("User", back_populates="blogs")

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    
    blogs = relationship("Blog", back_populates="user")
```

**Code (`schemas.py`):**
```python
class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []
    
    class Config:
        from_attributes = True

class ShowBlog(Blog):
    user: Optional[ShowUser] = None
    
    class Config:
        from_attributes = True
```

**Theory:**
- **Relationships:** SQLAlchemy relationships define how tables are connected
- **Foreign Key:** `user_id` references the `users.id` column
- **back_populates:** Creates bidirectional relationship - access blogs from user and user from blog
- **One-to-Many:** One user can have many blogs

---

### Checkpoint 11: Routers & Refactoring (`e124f07`)
**Commit:** `Created routers and added tags and refactored main.py`

**What was done:**
- Code organization with APIRouter
- Separation of concerns
- Tagged endpoints for documentation

**Files:**
- `routers/blog.py`
- `routers/user.py`

**Code (`routers/blog.py`):**
```python
from fastapi import APIRouter

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"],
)

@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.post('/')
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
```

**Code (`main.py`):**
```python
from .routers import blog, user, authentication

app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)
```

**Theory:**
- **APIRouter:** Allows grouping related endpoints
- **Prefix:** Applies URL prefix to all routes in the router
- **Tags:** Organizes endpoints in Swagger documentation
- **Modularity:** Separates code by domain (blogs, users, auth)

---

### Checkpoint 12: Repository Pattern (`e1482ff`)
**Commit:** `Repositories to store functions for user and blog`

**What was done:**
- Business logic separation
- Repository pattern implementation
- Cleaner router code

**Files:**
- `repository/blog.py`
- `repository/user.py`

**Code (`repository/blog.py`):**
```python
from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status

def all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Blog with id {id} not found'
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail": "Blog deleted"}

def update(id, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Blog with id {id} not found'
        )
    blog.update({'title': request.title, 'body': request.body})
    db.commit()
    return {"detail": "Blog updated"}

def show(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Blog with id {id} not found'
        )
    return blog
```

**Usage (`routers/blog.py`):**
```python
from ..repository import blog

@router.get('/')
def all(db: Session = Depends(database.get_db)):
    return blog.all(db)

@router.post('/')
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create(request, db)
```

**Theory:**
- **Repository Pattern:** Separates data access logic from business logic
- **Benefits:** 
  - Easier testing
  - Code reusability
  - Cleaner routers
  - Single responsibility principle

---

### Checkpoint 13: Authentication (`be8a3af`)
**Commit:** `Authentication done, JWT generation left`

**What was done:**
- Login endpoint creation
- Password verification

**Files:**
- `routers/authentication.py`
- `schemas.py` (added Login schema)

**Code (`schemas.py`):**
```python
class Login(BaseModel):
    email: str
    password: str
```

**Code (`routers/authentication.py`):**
```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, database, models
from ..hashing import Hash

router = APIRouter(tags=["Authentication"])

@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid Credentials"
        )
    
    if not Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid Credentials"
        )
    
    return {"message": "Login successful"}
```

**Theory:**
- **Authentication:** Verifying user identity
- **Process:**
  1. User sends email & password
  2. Find user by email
  3. Verify password hash
  4. Return success/failure

---

### Checkpoint 14: JWT Authentication (`bf72220`)
**Commit:** `JWT Auth done`

**What was done:**
- JWT token generation
- Complete authentication system

**Files:**
- `JWTtoken.py`
- Updated `routers/authentication.py`

**Code (`JWTtoken.py`):**
```python
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt

SECRET_KEY = "b4e1a0c9c3e54f71a4f8d8f74c52c1f603f2a5bc8cdd4e61b2f283f54d7e92af"
algorithm = "HS256"
access_token_expire_minutes = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=access_token_expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=algorithm)
    return encoded_jwt
```

**Code (`routers/authentication.py`):**
```python
from ..JWTtoken import create_access_token

@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid Credentials"
        )
    
    if not Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid Credentials"
        )
    
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
```

**Code (`schemas.py`):**
```python
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None
```

**Theory:**
- **JWT (JSON Web Token):** Self-contained token containing user information
- **Structure:** Header.Payload.Signature
- **Benefits:**
  - Stateless authentication
  - No server-side session storage
  - Can be verified without database lookup
- **Security:**
  - Token is signed with SECRET_KEY
  - Includes expiration time
  - Cannot be tampered with

**How it works:**
1. User logs in with email/password
2. Server verifies credentials
3. Server generates JWT with user email
4. Token returned to client
5. Client includes token in subsequent requests
6. Server verifies token to authenticate user

---

## 🔌 API Endpoints

### Authentication
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/login` | Login and get JWT token | No |

### Users
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/user` | Create new user | No |
| GET | `/user/{id}` | Get user by ID | No |

### Blogs
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/blog` | Get all blogs | No |
| POST | `/blog` | Create new blog | No |
| GET | `/blog/{id}` | Get blog by ID | No |
| PUT | `/blog/{id}` | Update blog | No |
| DELETE | `/blog/{id}` | Delete blog | No |

---

## 🗄️ Database Models

### User Model
```python
{
    "id": int,          # Primary key
    "name": str,        # User's name
    "email": str,       # User's email (unique)
    "password": str,    # Hashed password
    "blogs": []         # Related blogs (relationship)
}
```

### Blog Model
```python
{
    "id": int,          # Primary key
    "title": str,       # Blog title
    "body": str,        # Blog content
    "user_id": int,     # Foreign key to users
    "user": {}          # Related user (relationship)
}
```

---

## 🔐 Authentication

### Password Hashing
- **Algorithm:** Argon2
- **Library:** passlib
- Passwords are hashed before storage
- Plain text passwords never stored

### JWT Tokens
- **Algorithm:** HS256
- **Expiration:** 30 minutes
- **Library:** python-jose

### Example Login Flow

**Request:**
```json
POST /login
{
    "email": "user@example.com",
    "password": "mypassword"
}
```

**Response:**
```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer"
}
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| FastAPI | Web framework |
| SQLAlchemy | ORM |
| SQLite | Database |
| Pydantic | Data validation |
| Passlib | Password hashing |
| Python-JOSE | JWT tokens |
| Uvicorn | ASGI server |
| Argon2 | Password hashing algorithm |

---

## 📦 Dependencies

```txt
fastapi==0.123.9
uvicorn==0.36.3
sqlalchemy==2.0.36
passlib==1.7.4
python-jose==3.3.0
argon2-cffi==25.1.0
pydantic==2.12.5
```

---

## 🧪 Testing the API

### Using Swagger UI
1. Navigate to http://127.0.0.1:8001/docs
2. Try out endpoints interactively
3. View request/response schemas

### Using cURL

**Create User:**
```bash
curl -X POST "http://127.0.0.1:8001/user" \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com", "password": "secret123"}'
```

**Login:**
```bash
curl -X POST "http://127.0.0.1:8001/login" \
  -H "Content-Type: application/json" \
  -d '{"email": "john@example.com", "password": "secret123"}'
```

**Create Blog:**
```bash
curl -X POST "http://127.0.0.1:8001/blog" \
  -H "Content-Type: application/json" \
  -d '{"title": "My First Blog", "body": "This is the content"}'
```

**Get All Blogs:**
```bash
curl -X GET "http://127.0.0.1:8001/blog"
```

---

## 🎓 Key Learnings

1. **FastAPI Fundamentals**
   - Path parameters & query parameters
   - Request body validation with Pydantic
   - Dependency injection
   - Response models

2. **Database Management**
   - SQLAlchemy ORM setup
   - Model relationships (One-to-Many)
   - Session management
   - Database migrations

3. **Security**
   - Password hashing with Argon2
   - JWT token authentication
   - Secure credential handling

4. **Code Architecture**
   - Repository pattern
   - Router-based organization
   - Separation of concerns
   - Clean code principles

---

## 🐛 Common Issues & Solutions

### Issue: `ImportError: attempted relative import with no known parent package`
**Solution:** Run uvicorn from the parent directory:
```bash
cd d:\py\fastapi
uvicorn blog.main:app --reload
```

### Issue: `ValueError: password cannot be longer than 72 bytes`
**Solution:** Use Argon2 instead of bcrypt:
```python
pwd_cxt = CryptContext(schemes=["argon2"], deprecated="auto")
```

### Issue: `Field required: 'creator'`
**Solution:** Ensure schema field names match model relationship names (use `user` not `creator`)

### Issue: Database not updating
**Solution:** Delete `blog.db` and restart server to recreate tables

---

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [JWT.io](https://jwt.io/) - JWT debugger

---

## 🙏 Credits

### Original Course
This project is based on the **[FastAPI Course by Bitfumes](https://github.com/bitfumes/fastapi-course)**.

Special thanks to **Bitfumes** for creating an excellent FastAPI tutorial that forms the foundation of this project.

### Enhancements Made
- ✅ Upgraded to Pydantic v2 (`from_attributes` instead of `orm_mode`)
- ✅ Switched from bcrypt to Argon2 for better security
- ✅ Fixed import issues and module structure
- ✅ Added comprehensive documentation
- ✅ Improved error handling
- ✅ Enhanced code organization
- ✅ Added detailed commit-by-commit explanations
- ✅ Included troubleshooting guide

---

## 📄 License

This project is for educational purposes. Please refer to the original repository for licensing information.

---

## 👤 Author

**DevSsChar**
- GitHub: [@DevSsChar](https://github.com/DevSsChar)

---

## 🌟 Show Your Support

If you found this project helpful, please give it a ⭐️!

---

<div align="center">

**Built with ❤️ using FastAPI**

</div>
