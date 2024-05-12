from fastapi import APIRouter
from pydantic import BaseModel

import methods

from fastapi import HTTPException

import models

adminRouter = APIRouter()


# Route for admin login
@adminRouter.post("/admin/login")
async def login(user: models.User):
    admin_user = methods.get_admin_user()
    if user.username == admin_user["username"] and methods.pwd_context.verify(user.password, admin_user["password"]):
        access_token = methods.create_access_token(data={"sub": user.username}, expires_in=methods.ACCESS_TOKEN_EXPIRE_MINUTES)
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        return HTTPException(status_code=401, detail="Invalid username or password")
