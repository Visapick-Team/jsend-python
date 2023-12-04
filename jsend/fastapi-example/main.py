from fastapi import FastAPI
from pydantic import BaseModel, Field
from jfast.pagination import Pagination
from jfast.response import Response, render_jsend
from fastapi_pagination import paginate, add_pagination

app = FastAPI()

add_pagination(app)


class Person(BaseModel):
    name: str = Field(default='amir')


@app.get("/user/", response_model=Response[Person])
def single_user():
    person = Person(name='ali')
    return render_jsend(person.model_dump(), status_code=200)


@app.post("/user/", response_model=Response[Person])
def single_user(person: Person):
    return render_jsend(person.model_dump(), status_code=201)


@app.delete("/user/", response_model=Response[Person])
def single_user():
    return render_jsend({}, status_code=204)


@app.get("/users/", response_model=Pagination[Person])
def single_user():
    persons = [Person(name='ali'), Person(name='ali'), Person(name='ali')]
    return paginate(persons)
