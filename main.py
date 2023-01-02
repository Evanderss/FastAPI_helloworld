#python
from typing import Optional
from enum import Enum
#pydantic
from pydantic import BaseModel, Field
#fastapi
from fastapi import FastAPI, Body, Query, Path


app = FastAPI()


#Models
class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"


class Location(BaseModel): 
    city: str = Field(..., min_length=0, max_length=50)
    state: str = Field(..., min_length=0, max_length=50)
    country: str = Field(..., min_length=0, max_length=50)


class Person(BaseModel):
    first_name: str = Field(..., min_length=0, max_length=50, example="Miguel")
    last_name: str = Field(..., min_length=0, max_length=50, example="Torres")
    age: int = Field(..., gt=0, le=115, example=25)
    hair_color: Optional[HairColor] = Field(default=None, example=HairColor.black)
    is_married: Optional[bool] = Field(default=None, example=False)
    password: str = Field(..., min_length=8)


class PersonOut(BaseModel): 
    first_name: str = Field(..., min_length=0, max_length=50, example="Miguel")
    last_name: str = Field(..., min_length=0, max_length=50, example="Torres")
    age: int = Field(..., gt=0, le=115, example=25)
    hair_color: Optional[HairColor] = Field(default=None, example=HairColor.black)
    is_married: Optional[bool] = Field(default=None, example=False)


#Path operations "decorator"
@app.get("/")
def home():
    return {"hello": "World"}


#Request and Response Body
@app.post("/person/new", response_model=PersonOut)
def create_person(person: Person = Body(...)):
    return person


#Validations: Query Parameters
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(None, min_length=1, max_length=50, title="Person Name",description="This is the person name. It's between 1 and 50 characters", example="Rocío"),
    age: str = Query(..., title="Person Age", description="This is the person age. It's required", example=25)): 
    return {name: age}


#Validations: Path Parameters
@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(..., gt=0, example=123)): 
    return {person_id: "It exists!"}


#Validations: Request Body
@app.put("/person/{person_id}")
def update_person(person_id: int = Path(..., title="Person ID", description="This is the person ID", gt=0, example=123),
    person: Person = Body(...)): 
    #location: Location = Body(...)
    #results = person.dict()
    #results.update(location.dict())
    return person