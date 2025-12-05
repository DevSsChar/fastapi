# FastAPI Blog API - Complete Tutorial Project

<div align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3.12+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

A comprehensive FastAPI project demonstrating RESTful API development with authentication, database relationships, and best practices.

### 🚀 [Live Demo Available](https://fastapi-agrf.onrender.com/docs) - Try it out!

[![Live Demo](https://img.shields.io/badge/Live_Demo-Render-46E3B7?style=for-the-badge&logo=render)](https://fastapi-agrf.onrender.com/docs)

</div>

---

## 📚 Table of Contents

- [Overview](#-overview)
- [Live Demo](#-live-demo)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Development Journey](#-development-journey)
- [API Endpoints](#-api-endpoints)
- [Database Models](#-database-models)
- [Authentication](#-authentication)
- [Deployment to Render](#-deployment-to-render)
- [Credits](#-credits)
- [License](#-license)

---

## 🎯 Overview

This project is a complete blog API built with **FastAPI**, showcasing modern Python web development practices. It includes user authentication, CRUD operations, database relationships, password hashing, and JWT token-based security.

**Original Course:** This project is based on the excellent [FastAPI Course by Bitfumes](https://github.com/bitfumes/fastapi-course), extended with improvements, bug fixes, and enhanced documentation.

---

## 🌐 Live Demo

**🎉 A live version of this API is deployed and ready to use!**

🔗 **[https://fastapi-agrf.onrender.com/docs](https://fastapi-agrf.onrender.com/docs)**

You can explore the API interactively using the Swagger UI documentation:
- Create users and blogs
- Test authentication flow
- Try all CRUD operations
- No local setup required!

> **Note:** The free tier on Render may take 30-60 seconds to wake up if it hasn't been accessed recently.

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
│   ├── JWTtoken.py             # JWT token generation & verification
│   ├── oauth2.py               # OAuth2 scheme & authentication
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── blog.py             # Blog endpoints (protected)
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
- JWT token generation and verification
- Complete authentication system with OAuth2
- Protected endpoints requiring authentication

**Files:**
- `JWTtoken.py` - Token creation and verification
- `oauth2.py` - OAuth2 scheme and user authentication
- Updated `routers/authentication.py` - Login with token generation
- Updated `routers/blog.py` - Protected blog endpoints

**Code (`JWTtoken.py`):**
```python
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from blog import schemas

SECRET_KEY = "b4e1a0c9c3e54f71a4f8d8f74c52c1f603f2a5bc8cdd4e61b2f283f54d7e92af"
algorithm = "HS256"
access_token_expire_minutes = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=access_token_expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=algorithm)
    return encoded_jwt

def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[algorithm])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
        return token_data
    except JWTError:
        raise credentials_exception
```

**Code (`oauth2.py`):**
```python
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from . import JWTtoken

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(data: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}, 
    )
    return JWTtoken.verify_access_token(data, credentials_exception)
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

**Code (`routers/blog.py` - Protected endpoints):**
```python
from .. import oauth2

@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db), 
        current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.all(db)

@router.post('/')
def create(request: schemas.Blog, 
           db: Session = Depends(database.get_db),
           current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)
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
- **OAuth2PasswordBearer:** FastAPI's OAuth2 implementation with password flow
- **Benefits:**
  - Stateless authentication
  - No server-side session storage
  - Can be verified without database lookup
  - Protected endpoints require valid tokens
- **Security:**
  - Token is signed with SECRET_KEY
  - Includes expiration time (30 minutes)
  - Cannot be tampered with
  - Tokens must be included in Authorization header

**How it works:**
1. User logs in with email/password
2. Server verifies credentials
3. Server generates JWT with user email
4. Token returned to client
5. Client includes token in Authorization header: `Bearer <token>`
6. Protected endpoints verify token via `get_current_user` dependency
7. Invalid/expired tokens receive 401 Unauthorized

**Protected Endpoints:**
All blog endpoints now require authentication. Users must:
1. Login to receive access token
2. Include token in requests: `Authorization: Bearer <your_token>`
3. Token is automatically validated before endpoint execution

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
| GET | `/blog` | Get all blogs | ✅ Yes |
| POST | `/blog` | Create new blog | ✅ Yes |
| GET | `/blog/{id}` | Get blog by ID | ✅ Yes |
| PUT | `/blog/{id}` | Update blog | ✅ Yes |
| DELETE | `/blog/{id}` | Delete blog | ✅ Yes |

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

**1. Login to get token:**
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

**2. Use token to access protected endpoints:**

**In Swagger UI:**
1. Click the "Authorize" 🔓 button at the top
2. Enter your access token in the value field
3. Click "Authorize"
4. All subsequent requests will include the token

**With cURL:**
```bash
curl -X GET "http://127.0.0.1:8001/blog" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**With Postman/Thunder Client:**
- Authorization tab → Type: Bearer Token
- Paste your token in the Token field

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

**Login (Get Token):**
```bash
curl -X POST "http://127.0.0.1:8001/login" \
  -H "Content-Type: application/json" \
  -d '{"email": "john@example.com", "password": "secret123"}'
```

**Create Blog (with token):**
```bash
curl -X POST "http://127.0.0.1:8001/blog" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -d '{"title": "My First Blog", "body": "This is the content"}'
```

**Get All Blogs (with token):**
```bash
curl -X GET "http://127.0.0.1:8001/blog" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
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

### Issue: `401 Unauthorized` when accessing blog endpoints
**Solution:** All blog endpoints now require authentication. You must:
1. Create a user account first
2. Login to get an access token
3. Include the token in your requests: `Authorization: Bearer <token>`
4. In Swagger UI, click the "Authorize" button and paste your token

---

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [JWT.io](https://jwt.io/) - JWT debugger

---

## 🚀 Deployment to Render

This application is deployed on **[Render.com](https://render.com/)** with a free tier. Here's a complete step-by-step guide to deploy your own instance.

### Why Render?

- ✅ **Free Tier Available** - Perfect for learning and demo projects
- ✅ **Automatic Deployments** - Deploys on every git push
- ✅ **Built-in CI/CD** - No extra configuration needed
- ✅ **Easy Setup** - Deploy in minutes
- ✅ **HTTPS by Default** - Automatic SSL certificates

---

### 📋 Prerequisites

1. **GitHub Account** - Your code must be in a GitHub repository
2. **Render Account** - Sign up at [render.com](https://render.com/) (free)
3. **Working FastAPI Project** - Ensure your app runs locally

---

### 🛠️ Step-by-Step Deployment Guide

#### **Step 1: Prepare Your Project**

Ensure your `requirements.txt` has all dependencies with specific versions:

```txt
fastapi==0.123.9
uvicorn[standard]==0.38.0
sqlalchemy==2.0.36
passlib==1.7.4
python-jose==3.3.0
argon2-cffi==25.1.0
pydantic==2.12.5
python-multipart==0.0.20
```

**Key Requirements:**
- `uvicorn[standard]` - ASGI server with performance extras
- `python-multipart` - Required for OAuth2 form data (login)
- Specific versions prevent deployment errors

---

#### **Step 2: Push Code to GitHub**

```bash
# Initialize git (if not already done)
git init
git add .
git commit -m "Initial commit"

# Create a repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

---

#### **Step 3: Create Web Service on Render**

1. **Go to Render Dashboard**
   - Visit [dashboard.render.com](https://dashboard.render.com/)
   - Click **"New +"** → **"Web Service"**

2. **Connect GitHub Repository**
   - Click **"Connect account"** if not already connected
   - Authorize Render to access your repositories
   - Select your FastAPI repository

3. **Configure Service Settings**
   
   | Setting | Value |
   |---------|-------|
   | **Name** | `fastapi-blog-api` (or your preferred name) |
   | **Region** | Choose closest to you |
   | **Branch** | `main` |
   | **Root Directory** | Leave empty (unless app is in subdirectory) |
   | **Runtime** | `Python 3` |
   | **Build Command** | `pip install -r requirements.txt` |
   | **Start Command** | `uvicorn blog.main:app --host 0.0.0.0 --port $PORT` |

4. **Select Instance Type**
   - Choose **"Free"** plan
   - ⚠️ Note: Free tier spins down after 15 minutes of inactivity

5. **Advanced Settings (Optional)**
   - **Auto-Deploy:** Keep enabled (deploys on every push)
   - **Environment Variables:** Add if needed (see below)

6. **Click "Create Web Service"**

---

#### **Step 4: Understanding the Build Process**

Render will now:

1. **Clone your repository**
2. **Install Python 3.12** (or latest stable)
3. **Run build command:** `pip install -r requirements.txt`
4. **Start your app:** `uvicorn blog.main:app --host 0.0.0.0 --port $PORT`

You can watch the logs in real-time:
```
==> Installing dependencies...
==> Collecting fastapi==0.123.9
==> Successfully installed fastapi-0.123.9 uvicorn-0.38.0...
==> Starting service...
==> INFO:     Started server process [1]
==> INFO:     Uvicorn running on http://0.0.0.0:10000
```

---

#### **Step 5: Access Your Deployed API**

Once deployment succeeds:

- **API URL:** `https://your-service-name.onrender.com`
- **Swagger Docs:** `https://your-service-name.onrender.com/docs`
- **ReDoc:** `https://your-service-name.onrender.com/redoc`

**Live Demo:** [https://fastapi-agrf.onrender.com/docs](https://fastapi-agrf.onrender.com/docs)

---

### 🔧 Important Configuration Details

#### **Start Command Explained**

```bash
uvicorn blog.main:app --host 0.0.0.0 --port $PORT
```

- `blog.main:app` - Path to your FastAPI app instance
- `--host 0.0.0.0` - Listen on all network interfaces (required for Render)
- `--port $PORT` - Use Render's dynamically assigned port (critical!)
- `--reload` - ❌ Do NOT use in production (only for local development)

#### **Why `$PORT` is Important**

Render assigns a random port via the `$PORT` environment variable. Using `--port 8001` or hardcoded ports will cause deployment to fail.

---

### 🔐 Environment Variables (Optional)

For production, you should use environment variables for sensitive data:

**In Render Dashboard:**
1. Go to your service → **"Environment"** tab
2. Add environment variables:

```
SECRET_KEY=your-super-secret-key-here-generate-a-new-one
DATABASE_URL=sqlite:///./blog.db
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

**Update `JWTtoken.py` to use environment variables:**

```python
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key")
algorithm = os.getenv("ALGORITHM", "HS256")
access_token_expire_minutes = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
```

**Add to `requirements.txt`:**
```txt
python-dotenv==1.0.0
```

---

### 🗄️ Database Considerations

#### **SQLite (Current Setup)**

- ✅ Simple, no extra setup
- ❌ **Data is lost on every redeploy** (free tier limitation)
- ❌ Ephemeral storage - file system is not persistent

#### **PostgreSQL (Recommended for Production)**

**On Render:**
1. Create a **PostgreSQL database** (also has free tier)
2. Copy the **Internal Database URL**
3. Add to environment variables:
   ```
   DATABASE_URL=postgresql://user:password@host:5432/database
   ```

4. Update `requirements.txt`:
   ```txt
   psycopg2-binary==2.9.9
   ```

5. Update `database.py`:
   ```python
   import os
   
   SQLALCHEMY_DATABASE_URL = os.getenv(
       "DATABASE_URL",
       "sqlite:///./blog.db"  # Fallback for local development
   )
   
   # Handle Render's postgres:// URL format
   if SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
       SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace(
           "postgres://", "postgresql://", 1
       )
   ```

---

### 🔄 Automatic Deployments

Render automatically redeploys on every push to your connected branch:

```bash
# Make changes
git add .
git commit -m "Update feature"
git push origin main

# Render detects push and redeploys automatically!
```

**Watch deployment logs:**
- Go to Render Dashboard → Your Service → **"Logs"** tab
- See real-time build and deployment progress

---

### 🐛 Common Deployment Issues & Solutions

#### **Issue 1: Application Failed to Start**

**Error:**
```
ERROR: Could not find a version that satisfies the requirement uvicorn==0.36.3
```

**Solution:**
Update `requirements.txt` with correct package versions:
```txt
uvicorn[standard]==0.38.0
```

---

#### **Issue 2: Login Endpoint Returns 500 Error**

**Error:**
```
RuntimeError: Form data requires "python-multipart" to be installed
```

**Solution:**
Add to `requirements.txt`:
```txt
python-multipart==0.0.20
```

---

#### **Issue 3: Service Unavailable / Slow First Load**

**Cause:** Free tier services spin down after 15 minutes of inactivity.

**Solution:**
- First request may take 30-60 seconds to wake up
- Consider upgrading to paid tier for always-on service
- Use a monitoring service to ping your API periodically (e.g., UptimeRobot)

---

#### **Issue 4: Database Resets on Every Deploy**

**Cause:** SQLite data is not persistent on free tier.

**Solution:**
- Use Render's PostgreSQL database (free tier available)
- Or upgrade to paid tier for persistent disk storage

---

#### **Issue 5: CORS Errors from Frontend**

**Error:**
```
Access to fetch at 'https://your-api.onrender.com' from origin 'http://localhost:3000' has been blocked by CORS policy
```

**Solution:**
Add CORS middleware in `blog/main.py`:

```python
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

### 📊 Monitoring Your Deployment

**Render Dashboard provides:**
- **Logs:** Real-time application logs
- **Metrics:** CPU, Memory, Request stats (paid tiers)
- **Events:** Deployment history
- **Shell Access:** Debug via web terminal (paid tiers)

**View Logs:**
```bash
# In Render dashboard
Logs → Live Logs
```

---

### 💰 Free Tier Limitations

| Feature | Free Tier | Paid Tier |
|---------|-----------|------------|
| **Sleep after inactivity** | ✅ Yes (15 min) | ❌ No |
| **Build minutes** | 500 min/month | Unlimited |
| **Bandwidth** | 100 GB/month | Unlimited |
| **Custom domains** | ✅ Yes | ✅ Yes |
| **Persistent disk** | ❌ No | ✅ Yes |
| **Autoscaling** | ❌ No | ✅ Yes |
| **Price** | Free | From $7/month |

---

### 🎯 Deployment Checklist

- [x] `requirements.txt` with all dependencies
- [x] `uvicorn[standard]` and `python-multipart` included
- [x] Code pushed to GitHub
- [x] Render account created
- [x] Web service configured
- [x] Start command: `uvicorn blog.main:app --host 0.0.0.0 --port $PORT`
- [x] Deployment successful
- [x] API accessible at Render URL
- [x] Swagger docs working
- [ ] Environment variables configured (optional)
- [ ] PostgreSQL database connected (optional)
- [ ] CORS configured if using frontend (optional)

---

### 🔗 Alternative Deployment Platforms

If Render doesn't meet your needs:

- **[Railway](https://railway.app/)** - Similar to Render, $5/month credit
- **[Fly.io](https://fly.io/)** - Global edge deployment, generous free tier
- **[DigitalOcean App Platform](https://www.digitalocean.com/products/app-platform)** - $5/month minimum
- **[AWS Lambda](https://aws.amazon.com/lambda/)** - Serverless (requires Mangum adapter)
- **[Vercel](https://vercel.com/)** - Serverless (requires API routes setup)
- **[PythonAnywhere](https://www.pythonanywhere.com/)** - Beginner-friendly, limited free tier

---

### 📚 Additional Resources

- [Render Documentation](https://render.com/docs)
- [FastAPI Deployment Guide](https://fastapi.tiangolo.com/deployment/)
- [Uvicorn Deployment](https://www.uvicorn.org/deployment/)

---

## 🙏 Credits

### Original Course
This project is based on the **[FastAPI Course by Bitfumes](https://github.com/bitfumes/fastapi-course)**.

Special thanks to **Bitfumes** for creating an excellent FastAPI tutorial that forms the foundation of this project.

### Enhancements Made
- ✅ Upgraded to Pydantic v2 (`from_attributes` instead of `orm_mode`)
- ✅ Switched from bcrypt to Argon2 for better security
- ✅ Implemented OAuth2 with JWT token verification
- ✅ Protected all blog endpoints with authentication
- ✅ Added `oauth2.py` module for authentication middleware
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
