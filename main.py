from fastapi import FastAPI
from typing import Optional
import json
from pydantic import BaseModel,EmailStr,constr

app = FastAPI()

lstPersons= list()

def registerPerson(self):
    aperson = (self.name,self.personal_id,self.jobtitle,self.mail,self.department_id,self.country,self.manager_mail,self.account_type)
    lstPersons.append(aperson)
    
def filter_value( someList, value ):
    for x in someList:
        if x == value :
            yield x


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
                "department_id":"5",
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
     
    registerPerson(person)
    print(lstPersons)
    results = {"person": person,"status":"created"}
    
    return results

@app.get("/api/v1/person/read")

async def personRead(email:Email):
    print(email.email)
    
    output= [item for item in lstPersons
          if item[3] == email.email]
    
    readedPerson=json.dumps(output)
    
    results = {"person": readedPerson,"status":"Exists"}
   
    return results