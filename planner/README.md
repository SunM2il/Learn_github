# Planner Project.

## Structure FastAPI application

```bash
planner/
├── README.md
├── database
│   ├── __init__.py
│   └── connection.py
├── main.py
├── models
│   ├── __init__.py
│   ├── events.py
│   └── users.py
└── routes
    ├── __init__.py
    ├── events.py
    └── users.py
```

## Building an event planner application

Create virtual environment and active it:

```bash
python3 -m venv venv
source venv/bin/activate
```

Let's install application dependencies:

```bash
pip install fastapi uvicorn "pydantic[email]"
```

Lastly save the requirements into **requirements.txt**:

`pip freeze > requirements.txt`

## Dependency

### Planner sql

Set up **SQLModel** in our application.

`pip install sqlmodel`

### Python-jose

`pip install "python-jose[cryptography]"`

### Hashing password

`pip install "passlib[bcrypt]"`

### Multipart

`pip install python-multipart`

### Dot Env

`pip install "pydantic[dotenv]"`

## CORS

[FastAPI CORS](https://fastapi.tiangolo.com/tutorial/cors/)

## Deployment

### Managing Dependencies

We need to export list of all package installed

`pip freeze > requirements.txt`
