# Building a simple FastAPI

## Todos Project

> fastapi: The framework to build our applications.
> uvicorn: An Asynchronous Server Gateway Interface module to run our
> applications.

### Install Framework

* `source venv/bin/activate`
* `pip install fastapi uvicorn`

### Understanding routing in FastAPI

[HTTP Method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

### Validating request bodies using Pydantic models

> What is Pydantic?

Pydantic is a Python library that handles data validation using Python-type annotations.

Models, when defined, are used as type hints for request body objects and request-response objects. In this chapter, we will only look at using Pydantic models for request bodies.

example:

```python
from pydantic import BaseModel

class Book(BaseModel):
    id: int
    Name: str
    Publishers: str
    Isbn: str
```

## Responses in FastAPI

### What is a response header?

> A response header consists of the request's status and additional information to guide the delivery of the response body.

### What is a response body

> The data requested from the server by the client. The response body is determined from the Content-Type header variable and the most commonly used one is application/json.

## Status Codes

Status codes are unique short codes issued by a server in response to a client’s request. Response status codes are grouped into five categories, each denoting a different response:

* 1XX: Request has been received.
* 2XX: The request was successful.
* 3XX: Request redirected.
* 4XX: There’s an error from the client.
* 5XX: There’s an error from the server.

[Ref https status](https://www.webfx.com/web-development/glossary/http-status-codes/)
