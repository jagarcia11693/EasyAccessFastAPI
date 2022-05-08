from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel,EmailStr,constr

app = FastAPI()

class Email(BaseModel):
    email: EmailStr

class Person(BaseModel):
    name: str
    jobtitle: Optional[str] = None
    mobile: str
    personal_id: str
    mail: EmailStr
    joined:Optional[str] = None
    manager_mail: EmailStr 
    department_id: int
    country: constr(min_length=2,max_length=2)
    account_type:str
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Javier Andres Garcia",
                "personal_id":"1144058415",
                "jobtitle": "IT Analyst",
                "mobile": "3046387028",
                "mail": "gaton11693@gmail.com",
                "department":"5",
                "country":"CO",
                "manager_mail":"jefe@gmail.com",
                "account_type":"normal"
            }
        }

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/api/v1/person/create")

async def person(person:Person):
     
    results = {"person": person,"status":"created"}
    
    return results

@app.get("/api/v1/person/read/")

async def personRead(email:Email):
     
    results = {"person": person,"status":"Exists"}
    return results