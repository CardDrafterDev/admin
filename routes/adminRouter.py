import methods
import models

from error_handling import HTTPErrorHandler as httperr

from fastapi import APIRouter
from fastapi import Request, Response, status
from fastapi import HTTPException


adminRouter = APIRouter()


# Route for admin login
@adminRouter.post("/admin/login")
async def login(user: models.User, request: Request, response: Response):
    admin_user = methods.get_admin_user()
    if user.username == admin_user["username"] and methods.pwd_context.verify(user.password, admin_user["password"]):
        access_token = methods.create_access_token(data={"sub": user.username}, expires_in=methods.ACCESS_TOKEN_EXPIRE_MINUTES)
        methods.create_cookie(response=response, jwt_token=access_token, expires_in=methods.ACCESS_TOKEN_EXPIRE_MINUTES)
        return status.HTTP_202_ACCEPTED
    else:
        err =  HTTPException(status_code=401, detail="Invalid username or password")
        handled_err = httperr.handle_http_exception(request=request, exc=err)
        return handled_err
