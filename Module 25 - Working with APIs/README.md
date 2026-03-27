# **Context**

- [**Context**](#context)
- [**Day 29 - Flask API**](#day-29---flask-api)
  - [**Flask and Postman Setup**](#flask-and-postman-setup)
  - [**Flask Usages**](#flask-usages)
  - [**Flask Implementation**](#flask-implementation)
  - [**Project Structure of Flask**](#project-structure-of-flask)
- [**Day 30 - FastAPI**](#day-30---fastapi)
  - [**FastAPI Setup**](#fastapi-setup)
  - [**FastAPI Usages**](#fastapi-usages)
  - [**FastAPI Implementation**](#fastapi-implementation)
  - [**Project Structure of FastAPI**](#project-structure-of-fastapi)

# [**Day 29 - Flask API**](./Day%2029%20-%20Flask%20API/)

## **Flask and Postman Setup**

- Create [venv](../Module%2010%20-%20Virtual%20Environment%20&%20Requirements/)
- Install [Flask](https://pypi.org/project/Flask/)
- Download and install [Postman](https://www.postman.com/downloads/)

[⬆️ Go to Context](#context)

## **Flask Usages**

- Core Usages

  - Building RESTful APIs
  - Creating backend services for web & mobile apps
  - Developing lightweight microservices
  - Backend for small to medium web apps
  - Rapid prototyping & MVPs
  - Internal tools & admin dashboards

- API Development

  - CRUD APIs (Create, Read, Update, Delete)
  - Request handling using decorators & routes
  - Manual or schema-based validation (Marshmallow, Pydantic)
  - JSON request & response handling
  - Blueprint-based API versioning

- Performance & Architecture

  - Synchronous by default (WSGI-based)
  - Async possible via extensions or ASGI wrappers
  - Suitable for low to medium traffic APIs
  - Extremely flexible and minimal
  - Requires more decisions from the developer

- Authentication & Security

  - Session-based authentication
  - JWT authentication (Flask-JWT-Extended)
  - OAuth support (Flask-Login, Flask-OAuthlib)
  - Role-based access control via custom decorators
  - CSRF protection for form-based apps

- Database Integration

  - SQL databases (PostgreSQL, MySQL, SQLite)
  - ORM support (SQLAlchemy, Flask-SQLAlchemy)
  - Migration support (Flask-Migrate)
  - NoSQL databases (MongoDB via PyMongo)
  - Mostly synchronous DB operations

- Documentation & Testing

  - No built-in API docs
  - Swagger/OpenAPI via extensions (Flask-RESTX, Flasgger)
  - Manual schema definition
  - Strong pytest integration
  - Flask test client for unit & integration tests

- Microservices & DevOps

  - Container-friendly (Docker)
  - Easy deployment on AWS, GCP, Azure
  - Commonly used behind Nginx/Gunicorn
  - Works with Kubernetes
  - Requires extra setup for health checks

- Background & Advanced Tasks

  - Background jobs via Celery or RQ
  - Middleware via WSGI
  - Custom error handling
  - App lifecycle hooks
  - Limited native real-time support (WebSockets via extensions)

- Machine Learning & Data APIs

  - Popular for serving ML models
  - Simple inference endpoints
  - Data processing APIs
  - Widely used in research & data science teams
  - Very low learning curve for ML engineers

- When to Use Flask

  - Need full control over architecture
  - Building small to medium APIs
  - Rapid prototyping & experiments
  - ML model serving with minimal overhead
  - Prefer simplicity over automation

- When NOT to Use Flask

  - High-concurrency async workloads
  - Large teams needing strict structure
  - APIs requiring automatic validation & docs
  - Complex microservice ecosystems (FastAPI fits better)

[⬆️ Go to Context](#context)

## **Flask Implementation**

- App Setup & Initialization

  ```py
  from flask import Flask

  app = Flask(__name__)

  if __name__ == "__main__":
      app.run(debug=True)
  ```

- Basic Routing

  ```py
  @app.route("/")
  def home():
      return "Hello, Flask!"
  ```

  ```py
  @app.route("/about")
  def about():
      return "About Page"
  ```

- Routing with HTTP Methods

  ```py
  from flask import request

  @app.route("/login", methods=["GET", "POST"])
  def login():
      if request.method == "POST":
          return "POST request"
      return "GET request"
  ```

- URL Parameters (Dynamic Routes)

  ```py
  @app.route("/user/<username>")
  def user_profile(username):
      return f"User: {username}"
  ```

  ```py
  @app.route("/post/<int:post_id>")
  def show_post(post_id):
      return f"Post ID: {post_id}"
  ```

- Query Parameters

  ```py
  @app.route("/search")
  def search():
      keyword = request.args.get("q")
      return f"Search for: {keyword}"
  ```

- JSON Response (API)

  ```py
  from flask import jsonify

  @app.route("/api/status")
  def status():
      return jsonify({
          "status": "ok",
          "service": "flask"
      })
  ```

- Request Data (Form & JSON)

  ```py
  @app.route("/submit", methods=["POST"])
  def submit():
      name = request.form.get("name")
      return f"Name: {name}"
  ```

  ```py
  @app.route("/submit-json", methods=["POST"])
  def submit_json():
      data = request.get_json()
      return jsonify(data)
  ```

- Templates (Jinja2)

  ```py
  from flask import render_template

  @app.route("/profile")
  def profile():
      return render_template(
          "profile.html",
          username="TT",
          age=20
      )
  ```

- Static Files (CSS / JS)

  ```py
  # Folder structure:
  # /static/style.css
  # /templates/index.html
  ```

  ```html
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
  ```

- Redirects & URL Building

  ```py
  from flask import redirect, url_for

  @app.route("/old")
  def old():
      return redirect(url_for("home"))
  ```

- Error Handling

  ```py
  @app.errorhandler(404)
  def not_found(e):
      return "Page not found", 404
  ```

  ```py
  @app.errorhandler(500)
  def server_error(e):
      return "Server error", 500
  ```

- Blueprints (Project Structure)

  ```py
  from flask import Blueprint

  auth = Blueprint("auth", __name__)

  @auth.route("/login")
  def login():
      return "Login Page"
  ```

  ```py
  app.register_blueprint(auth, url_prefix="/auth")
  ```

- Configuration & Environment Variables

  ```py
  import os

  app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
  app.config["DEBUG"] = True
  ```

- Middleware (Before & After Request)

  ```py
  @app.before_request
  def before_request():
      print("Before request")

  @app.after_request
  def after_request(response):
      return response
  ```

- Database Integration (Flask + MySQ)

  ```py
  import mysql.connector

  def get_db():
      return mysql.connector.connect(
          host="HOST",
          user="USER",
          password="PASSWORD",
          database="DB_NAME"
      )
  ```

[⬆️ Go to Context](#context)

## **Project Structure of Flask**

- Minimal Flask App Structure

  ```txt
  flask_app/
  ├─ app.py
  ├─ requirements.txt
  └─ README.md
  ```

- Standard Structure

  ```txt
  flask_app/
  ├─ app/
  │  ├─ __init__.py          # create_app(), app config
  │  ├─ routes.py            # main routes
  │  ├─ models.py            # database models
  │  ├─ extensions.py        # db, login_manager, etc.
  │  ├─ config.py            # configuration classes
  │  │
  │  ├─ templates/
  │  │  ├─ base.html
  │  │  ├─ index.html
  │  │  └─ auth/
  │  │     └─ login.html
  │  │
  │  └─ static/
  │     ├─ css/
  │     │  └─ style.css
  │     ├─ js/
  │     │  └─ main.js
  │     └─ images/
  │
  ├─ migrations/             # Flask-Migrate (Alembic)
  │
  ├─ tests/
  │  ├─ __init__.py
  │  └─ test_routes.py
  │
  ├─ .env
  ├─ .gitignore
  ├─ requirements.txt
  └─ run.py                  # entry point
  ```

- Large / Scalable Structure (Production-style)

  ```txt
  flask_app/
  ├─ app/
  │  ├─ __init__.py
  │  ├─ auth/
  │  │  ├─ __init__.py
  │  │  ├─ routes.py
  │  │  ├─ forms.py
  │  │  └─ models.py
  │  │
  │  ├─ blog/
  │  │  ├─ __init__.py
  │  │  ├─ routes.py
  │  │  └─ models.py
  │  │
  │  ├─ templates/
  │  │  ├─ base.html
  │  │  ├─ auth/
  │  │  └─ blog/
  │  │
  │  ├─ static/
  │  │
  │  └─ extensions.py
  │
  ├─ migrations/
  ├─ tests/
  ├─ .env
  ├─ requirements.txt
  └─ run.py
  ```

[⬆️ Go to Context](#context)

# [**Day 30 - FastAPI**](./Day%2030%20-%20FastAPI/)

- FastAPI is a modern, high-performance Python web framework used to build APIs quickly with automatic documentation and strong type safety.

[⬆️ Go to Context](#context)

## **FastAPI Setup**

- Create [venv](../Module%2010%20-%20Virtual%20Environment%20&%20Requirements/)
- Install [fastapi](https://pypi.org/project/fastapi/), [uvicorn](https://pypi.org/project/uvicorn/), [pydantic](https://pypi.org/project/pydantic/)

[⬆️ Go to Context](#context)

## **FastAPI Usages**

- Core Usages
  - Building RESTful APIs
  - Creating backend services for web & mobile apps
  - Developing microservices
  - Serving machine learning models
  - Backend for SPAs (React / Next.js / Vue)
  - Internal tools & automation services

- API Development
  - CRUD APIs (Create, Read, Update, Delete)
  - Request validation using Pydantic models
  - Automatic request parsing (JSON, query params, path params)
  - Automatic response serialization
  - API versioning

- Performance & Architecture
  - Asynchronous APIs using async/await
  - High performance with Starlette & Uvicorn
  - Suitable for I/O-bound and concurrent workloads
  - Lightweight alternative to Django REST Framework

- Authentication & Security
  - JWT-based authentication
  - OAuth2 (Password, Authorization Code)
  - API key authentication
  - Role-based access control (RBAC)
  - Dependency-based security checks

- Database Integration
  - SQL databases (PostgreSQL, MySQL, SQLite)
  - ORM support (SQLAlchemy, SQLModel)
  - Async DB access (asyncpg, databases)
  - NoSQL databases (MongoDB with Motor)

- Documentation & Testing
  - Auto-generated Swagger UI (/docs)
  - ReDoc documentation (/redoc)
  - Type hints act as documentation
  - Easy integration with pytest
  - TestClient for API testing

- Microservices & DevOps
  - Container-friendly (Docker)
  - Easy deployment with AWS, GCP, Azure
  - Works well with Kubernetes
  - Used behind API gateways
  - Health-check endpoints

- Background & Advanced Tasks
  - Background tasks (email, logging, cleanup jobs)
  - Middleware support
  - Custom exception handling
  - Event hooks (startup & shutdown)
  - WebSocket support (real-time apps)

- Machine Learning & Data APIs
  - Serving trained ML/DL models
  - Model inference APIs
  - Data preprocessing endpoints
  - Lightweight alternative to Flask for ML serving

- When to Use FastAPI
  - Need high-speed APIs
  - Prefer strong typing & validation
  - Building scalable microservices
  - Want automatic API docs

- When NOT to Use FastAPI
  - Full monolithic apps with heavy admin panels
  - CMS-like applications (Django is better)

[⬆️ Go to Context](#context)

## **FastAPI Implementation**

- **App Setup & Initialization**

  ```py
  # main.py
  from fastapi import FastAPI

  app = FastAPI(title="My API", version="0.1.0")

  @app.get("/")
  def read_root():
      return {"hello": "world"}
  ```

- Development run:

  ```sh
  python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
  ```

- **Routing basics (path & query params)**

  ```py
  from fastapi import FastAPI, Path, Query

  app = FastAPI()

  @app.get("/items/{item_id}")
  def get_item(item_id: int = Path(..., title="ID of item"), q: str | None = Query(None, max_length=50)):
      return {"item_id": item_id, "q": q}
  ```

  - `Path` and `Query` allow metadata & validation (min/max, regex, description).
  - Path params are required. Query params optional by default.

- **Request body & Pydantic models**

  ```py
  from pydantic import BaseModel, Field
  from typing import List, Optional

  class Item(BaseModel):
      name: str = Field(..., min_length=1, max_length=100)
      description: Optional[str] = None
      price: float = Field(..., gt=0)
      tags: List[str] = []

  @app.post("/items", response_model=Item, status_code=201)
  def create_item(item: Item):
      # item is validated and typed
      return item
  ```

  - Use `response_model` to validate & shape output.
  - Pydantic `Field(...)` for constraints and examples.

- **Response types & classes**

  ```py
  from fastapi.responses import JSONResponse, HTMLResponse, PlainTextResponse, FileResponse, StreamingResponse

  @app.get("/html", response_class=HTMLResponse)
  def get_html():
      return "<html><body><h1>Hello</h1></body></html>"

  @app.get("/file")
  def get_file():
      return FileResponse("path/to/file.pdf", media_type="application/pdf", filename="report.pdf")
  ```

  - `StreamingResponse` for large streams (video, large JSON, generator).
  - Set appropriate `status_code` and headers as needed.

- **Advanced response control**

  ```py
  from fastapi import Response

  @app.get("/custom")
  def custom():
      content = {"hello": "world"}
      return JSONResponse(content=content, status_code=202, headers={"X-App": "MyApp"})
  ```

  - Use `response_model_include` / `exclude` and `response_model_exclude_unset` to control fields.

- **Dependencies (DI) — basic & yield cleanup**

  ```py
  from fastapi import Depends

  def common_parameters(q: str | None = None, limit: int = 10):
      return {"q": q, "limit": limit}

  @app.get("/search")
  def search(params: dict = Depends(common_parameters)):
      return params
  ```

  - `Depends` supports callables, classes (`__call__`), async dependencies.
  - Use `yield` in dependencies for setup/teardown (e.g., DB session):

  ```py
  from contextlib import contextmanager

  async def get_db():
      db = create_session()
      try:
          yield db
      finally:
          db.close()
  ```

- **APIRouter & modularization**

  ```py
  from fastapi import APIRouter

  router = APIRouter(prefix="/users", tags=["users"])

  @router.get("/")
  def list_users():
      return [{"id": 1, "name": "Alice"}]

  # main.py
  app.include_router(router)
  ```

  - Create routers per domain (users, auth, items) and include in main app.
  - Supports prefix, tags, dependencies for groups.

- **Middleware & CORS**

  ```py
  from fastapi.middleware.cors import CORSMiddleware

  app.add_middleware(
      CORSMiddleware,
      allow_origins=["https://myfrontend.com"],
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
  )
  ```

- Custom middleware example:

  ```py
  from starlette.middleware.base import BaseHTTPMiddleware
  from starlette.requests import Request
  from starlette.responses import Response

  class LoggingMiddleware(BaseHTTPMiddleware):
      async def dispatch(self, request: Request, call_next):
          print("request:", request.method, request.url)
          response: Response = await call_next(request)
          print("response status:", response.status_code)
          return response

  app.add_middleware(LoggingMiddleware)
  ```

- **Startup & Shutdown events**

  ```py
  @app.on_event("startup")
  async def startup_event():
      # create connection pool, initialize cache, etc.
      pass

  @app.on_event("shutdown")
  async def shutdown_event():
      # cleanup
      pass
  ```

  - Use for global resources (DB pool, message brokers).

- **Background tasks**

  ```py
  from fastapi import BackgroundTasks

  def write_log(message: str):
      with open("log.txt", "a") as f:
          f.write(message + "\n")

  @app.post("/notify")
  def notify(background_tasks: BackgroundTasks, msg: str):
      background_tasks.add_task(write_log, msg)
      return {"status": "accepted"}
  ```

  - Good for non-critical tasks (emails, logs) — not for long-running workers (use Celery/RQ).

- **File uploads & forms**

  ```py
  from fastapi import File, UploadFile, Form

  @app.post("/upload")
  async def upload(file: UploadFile = File(...), desc: str = Form(...)):
      contents = await file.read()
      # save or process
      return {"filename": file.filename, "content_length": len(contents)}
  ```

  - `UploadFile` is async-friendly and efficient.

- **WebSockets**

  ```py
  from fastapi import WebSocket

  @app.websocket("/ws")
  async def websocket_endpoint(ws: WebSocket):
      await ws.accept()
      while True:
          data = await ws.receive_text()
          await ws.send_text(f"echo: {data}")
  ```

  - Use for realtime features. When running behind proxy, ensure proper websocket support.

- **Server-Sent Events (SSE) / streaming**

  ```py
  from fastapi.responses import StreamingResponse
  import asyncio

  async def event_generator():
      for i in range(5):
          yield f"data: ping {i}\n\n"
          await asyncio.sleep(1)

  @app.get("/sse")
  async def sse():
      return StreamingResponse(event_generator(), media_type="text/event-stream")
  ```

- **Security: OAuth2 password flow & JWT (example)**

  ```py
  from fastapi import Depends, HTTPException, status
  from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
  from datetime import datetime, timedelta
  import jwt  # use PyJWT or jose

  oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

  SECRET = "super-secret"
  ALGORITHM = "HS256"

  def create_access_token(data: dict, expires_delta: timedelta | None = None):
      to_encode = data.copy()
      expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
      to_encode.update({"exp": expire})
      return jwt.encode(to_encode, SECRET, algorithm=ALGORITHM)

  @app.post("/token")
  def login(form_data: OAuth2PasswordRequestForm = Depends()):
      # validate user credentials (check DB)
      if form_data.username != "bob" or form_data.password != "pass":
          raise HTTPException(status_code=401, detail="Invalid credentials")
      token = create_access_token({"sub": form_data.username})
      return {"access_token": token, "token_type": "bearer"}

  def get_current_user(token: str = Depends(oauth2_scheme)):
      try:
          payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
          username = payload.get("sub")
          if username is None:
              raise HTTPException(status_code=401)
          return {"username": username}
      except jwt.PyJWTError:
          raise HTTPException(status_code=401)
  ```

  - Use well-tested libs (`python-jose`, `PyJWT`) and rotate secrets.
  - Implement refresh tokens and scopes for production.

- **Async vs Sync functions**

  - Use `async def` when you perform IO-bound async ops (db async drivers, httpx async). Use sync for CPU-bound or sync libs.
  - If a sync blocking function must run in an async endpoint, use `run_in_threadpool`:

    ```py
    from starlette.concurrency import run_in_threadpool
    result = await run_in_threadpool(sync_blocking_func, arg)
    ```

- **Databases: sync (SQLAlchemy) & async (SQLModel / async SQLAlchemy)**

- Sync SQLAlchemy + session dependency:

  ```py
  # db.py (sync)
  from sqlalchemy import create_engine
  from sqlalchemy.orm import sessionmaker

  engine = create_engine("postgresql://user:passwd@localhost/dbname")
  SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

  def get_db():
      db = SessionLocal()
      try:
          yield db
      finally:
          db.close()
  ```

  ```py
  @app.get("/users/{user_id}")
  def get_user(user_id: int, db = Depends(get_db)):
      return db.query(User).filter(User.id == user_id).first()
  ```

- Async example with SQLModel / AsyncEngine:

  ```py
  # async_db.py
  from sqlmodel import SQLModel, create_engine, AsyncSession
  from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

  engine = create_async_engine("postgresql+asyncpg://user:pass@localhost/db")
  async_session = async_sessionmaker(engine, expire_on_commit=False)

  async def get_session():
      async with async_session() as session:
          yield session
  ```

- Migrations with Alembic (sync SQLAlchemy): commands (WSL/Linux / Windows):

  - WSL/Linux:

    ```bash
    pip install alembic
    alembic init alembic
    # edit alembic.ini and env.py to point to SQLALCHEMY DB URL
    alembic revision --autogenerate -m "create users"
    alembic upgrade head
    ```

  - Windows PowerShell (similar):

    ```sh
    .\.venv\Scripts\Activate.ps1
    pip install alembic
    alembic init alembic
    # run revisions and upgrades similarly
    ```

- For async migrations, use tools that support async dialects (recent Alembic versions can be configured).

- **Testing (TestClient & pytest)**

  ```py
  from fastapi.testclient import TestClient
  import pytest

  client = TestClient(app)

  def test_read_root():
      resp = client.get("/")
      assert resp.status_code == 200
      assert resp.json() == {"hello": "world"}

  # override dependencies
  def test_with_fake_db():
      def fake_get_db():
          yield FakeDB()
      app.dependency_overrides[get_db] = fake_get_db
      resp = client.get("/users/1")
      assert resp.status_code == 200
  ```

   Use `app.dependency_overrides` to inject test doubles.

- **OpenAPI / docs customization**

  ```py
  app = FastAPI(
      title="My API",
      description="Detailed description",
      version="0.2.0",
      docs_url="/docs",         # Swagger UI
      redoc_url="/redoc",      # ReDoc
      openapi_url="/openapi.json"
  )

  @app.get("/items", tags=["items"], summary="List items", description="Returns a list of items.")
  def list_items():
      ...
  ```

  - Add examples via `Field(example=...)` or `response_model` examples.

- **Versioning & routing patterns**

  - Common approaches:

    - URL versioning: `/v1/items`, `/v2/items`
    - Header-based versioning (custom dependency to read header)
  - Keep routers grouped per version: `v1_router`, `v2_router`.

- **Pagination & filtering patterns**

  ```py
  @app.get("/items")
  def list_items(limit: int = 10, offset: int = 0, q: str | None = None):
      query = db.query(Item)
      if q:
          query = query.filter(Item.name.ilike(f"%{q}%"))
      items = query.offset(offset).limit(limit).all()
      return {"count": len(items), "items": items}
  ```

  - Return metadata (total_count, next_page) for clients.

- **Caching & rate limiting (third-party)**

  - Use `fastapi-cache2`, `aiocache` for caching responses.
  - Rate limiting: use `slowapi` or an API gateway (NGINX / Kong) for production rate limiting.

  ```py
  # example using fastapi-cache2
  from fastapi_cache import FastAPICache
  from fastapi_cache.backends.inmemory import InMemoryBackend

  @app.on_event("startup")
  async def startup():
      FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")
  ```

- **Observability: logging & tracing**

  - Use structured logging (structlog or Python logging with JSON formatter).
  - Integrate tracing (OpenTelemetry) and error tracking (Sentry).
  - Example Sentry setup:

    ```py
    import sentry_sdk
    sentry_sdk.init(dsn="your_dsn")
    ```

- **Mounting static files & templates**

  ```py
  from fastapi.staticfiles import StaticFiles
  from fastapi.templating import Jinja2Templates
  from fastapi import Request

  app.mount("/static", StaticFiles(directory="static"), name="static")
  templates = Jinja2Templates(directory="templates")

  @app.get("/page")
  def get_page(request: Request):
      return templates.TemplateResponse("index.html", {"request": request, "title": "Home"})
  ```

- **Mounting sub-applications**

  ```py
  from fastapi import FastAPI

  admin_app = FastAPI(openapi_prefix="/admin")

  @admin_app.get("/stats")
  def stats():
      return {"uptime": 100}

  app.mount("/admin", admin_app)
  ```

  - Useful when combining microservices or separate apps.

- **Webhooks & security tips**

  - Validate webhook payloads with signatures (HMAC).
  - Use HTTPS for production and verify certificates.

- **Common pitfalls & best practices**

  - Don’t run Uvicorn with `--reload` in production.
  - Avoid blocking IO in `async` endpoints (use threadpool).
  - Always validate user input and escape outputs (when rendering HTML).
  - Limit body size or implement streaming for large uploads.
  - Use connection pools for DBs; don’t create new engine/session per request.
  - Keep secrets out of code (use env vars / secret manager).
  - Use HTTPS + HSTS in production.

- **Deployment checklist (brief)**

  - Set environment variables (DB, secrets).

  - Use a process manager (systemd) or container orchestrator (Docker + Kubernetes).

  - Example Dockerfile:

    ```dockerfile
    FROM python:3.11-slim
    WORKDIR /app
    COPY pyproject.toml .
    RUN pip install --no-cache-dir fastapi uvicorn
    COPY . .
    CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
    ```

  - Use reverse proxy (NGINX) in front of app for static serving, HTTPS termination, rate limiting.

- **Extending FastAPI ecosystem (tools & libs to know)**

  - Databases: SQLAlchemy, SQLModel, Tortoise ORM, asyncpg
  - Migrations: Alembic
  - Authentication: python-jose, oauthlib, Authlib
  - Background workers: Celery, RQ, Dramatiq
  - Caching: fastapi-cache2, redis
  - Testing: pytest, httpx (async testing), TestClient
  - Docs: Swagger UI, ReDoc (customize/extend)
  - Observability: OpenTelemetry, Sentry

- **Minimal practical template (file layout)**

  ```txt
  project/
  ├─ app/
  │  ├─ main.py
  │  ├─ api/
  │  │  ├─ v1/
  │  │  │  ├─ users.py
  │  │  │  └─ items.py
  │  ├─ core/
  │  │  ├─ config.py
  │  │  └─ security.py
  │  ├─ db/
  │  │  ├─ base.py
  │  │  └─ session.py
  │  └─ models/
  ├─ alembic/
  ├─ tests/
  ├─ Dockerfile
  └─ pyproject.toml
  ```

- **Quick reference snippets**

  - Run async DB query example (SQLModel):

    ```py
    async with async_session() as session:
        result = await session.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
    ```

  - Override dependency for tests:

    ```py
    app.dependency_overrides[get_db] = override_get_db
    ```

  - Return paginated data with meta:

    ```py
    return {"total": total, "limit": limit, "offset": offset, "items": items}
    ```

[⬆️ Go to Context](#context)

## **Project Structure of FastAPI**

- **Minimal FastAPI App**

  ```txt
  fastapi_app/
  ├─ main.py                # app = FastAPI(), include routers, run with uvicorn
  ├─ requirements.txt       # fastapi, uvicorn[standard], pydantic...
  └─ README.md
  ```

  - `main.py` — tiny app (startup events, one route). Run: `uvicorn main:app --reload`

- **Standard Structure**

  ```txt
  fastapi_app/
  ├─ app/
  │  ├─ __init__.py         # optional; package marker
  │  ├─ main.py             # app factory or app instance, include routers, startup/shutdown
  │  ├─ core/
  │  │  ├─ config.py        # settings (pydantic BaseSettings)
  │  │  └─ security.py      # JWT helpers, password hashing
  │  ├─ api/
  │  │  ├─ __init__.py
  │  │  ├─ v1/
  │  │  │  ├─ __init__.py
  │  │  │  ├─ routers/
  │  │  │  │  ├─ users.py
  │  │  │  │  └─ items.py
  │  │  │  ├─ schemas.py    # Pydantic models (request/response)
  │  │  │  └─ crud.py       # DB access helpers
  │  ├─ db/
  │  │  ├─ base.py          # Base metadata, model imports
  │  │  ├─ session.py       # engine/session (sync/async)
  │  │  └─ models.py        # SQLAlchemy/SQLModel models
  │  ├─ services/
  │  │  └─ ml_inference.py  # model loading + inference endpoints caller
  │  ├─ dependencies.py     # common dependency functions (auth, pagination)
  │  ├─ background_tasks.py # Celery/RQ integration or FastAPI BackgroundTasks usage
  │  ├─ templates/          # Jinja2 if using server-side templates
  │  └─ static/             # static files (served by ASGI in dev or by CDN/nginx in prod)
  │
  ├─ alembic/               # DB migrations (if using SQLAlchemy/SQLModel + Alembic)
  ├─ tests/
  │  ├─ __init__.py
  │  └─ test_users.py       # pytest + AsyncClient/httpx or TestClient
  ├─ .env
  ├─ .gitignore
  ├─ requirements.txt
  └─ docker-compose.yml     # optional
  ```

  - Use routers to split endpoints; mount versions (e.g., `/api/v1`).
  - `schemas.py` = Pydantic models (validate and document automatically).
  - `dependencies.py` centralizes auth and reusable DI.

- **Large / Scalable (production-style)**

  ```txt
  fastapi_app/
  ├─ app/
  │  ├─ main.py
  │  ├─ core/
  │  │  ├─ config.py
  │  │  ├─ logger.py
  │  │  └─ events.py       # startup/shutdown hooks
  │  ├─ api/
  │  │  ├─ v1/
  │  │  │  ├─ routers/
  │  │  │  ├─ schemas/
  │  │  │  └─ crud/
  │  │  └─ v2/             # future versions
  │  ├─ models/             # per-model files or folder per domain
  │  ├─ db/
  │  │  ├─ session.py
  │  │  ├─ base.py
  │  │  └─ repositories/
  │  ├─ services/
  │  ├─ workers/            # celery tasks + workers
  │  ├─ utils/
  │  ├─ tests/
  │  └─ docs/               # extra documentation (MD files)
  │
  ├─ migrations/            # alembic or other migration tool
  ├─ infra/
  │  ├─ Dockerfile
  │  ├─ k8s/                # k8s manifests
  │  └─ helm/               # optional
  ├─ ci/
  │  └─ pipelines.yml
  ├─ requirements.txt
  ├─ poetry.lock / pyproject.toml
  └─ README.md
  ```

  - Separate `services/` for business logic and `repositories/` for DB access.
  - `infra/` for deployment artifacts; `ci/` for pipeline configs.

- **Common/Useful files & notes**

  - `main.py` (example minimal):

    ```py
    from fastapi import FastAPI
    from .api.v1.routers import users

    app = FastAPI(title="My App")

    app.include_router(users.router, prefix="/api/v1/users")
    ```

  - `core/config.py` — use `pydantic.BaseSettings` for env-driven config.
  - `db/session.py` — choose sync (SQLAlchemy + sessionmaker) or async (async_engine + AsyncSession / SQLModel).
  - `schemas.py` — place Pydantic models near routers or in per-domain `schemas/`.
  - `dependencies.py` — put reusable DI like `get_db`, `get_current_user`.
  - `Dockerfile` — use `uvicorn` (ASGI): `CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]`.
  - `requirements.txt` typical libs:

    - `fastapi`
    - `uvicorn[standard]`
    - `sqlalchemy` or `sqlmodel`
    - `databases` or `asyncpg` (if async)
    - `alembic`
    - `pydantic`
    - `pytest`, `httpx`
    - `python-jose` / `passlib` for auth

- **Testing**

  - Use `pytest` + `httpx.AsyncClient` for async endpoints or `TestClient` for sync.
  - Put fixtures for test DB in `tests/conftest.py` (use sqlite in-memory or test docker DB).

[⬆️ Go to Context](#context)
