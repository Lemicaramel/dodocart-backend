from fastapi import FastAPI
from UserRepository import create_user
from User import User
import uvicorn
# from typing import List
from pydantic import BaseModel, Field
app = FastAPI()

@app.get("/users")
async def getUsers():
   return {"message": "All Users"}

@app.get("/users/{id}")
async def getUserById(id):
   message = "Users by Id " + id
   return {"message": message}


class UserRequest(BaseModel):
   name : str
   age : str
   emailID : str
   password : str
   designation : str

   
@app.post("/createUser")
async def createUser(user : UserRequest):
   message = "User created successfully!"
   userobj = User(user.name,user.age,user.emailID, user.password,user.designation)
   create_user(userobj)
   return {"message":message,"user": userobj}

@app.delete("/deleteUser/{id}")
async def deleteUser(id):
   message = "User deleted successfully."+ id
   return {"message":message}

@app.put("/updateUser/{id}")
async def updateUser(id,user:UserRequest):
   message = "User updated successfully."+ id 
   return {"message":message,"user" : user} 
if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
   
