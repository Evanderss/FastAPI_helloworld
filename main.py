#python
from typing import Optional
#pydantic
from pydantic import BaseModel
#fastapi
from fastapi import FastAPI, Body


app = FastAPI()


#Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


#Path operations "decorator"
@app.get("/")
def home():
    return {"hello": "World"}


#Request and Response Body
@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person