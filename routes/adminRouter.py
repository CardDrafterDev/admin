import methods

from decorators import protected

from fastapi import APIRouter
from fastapi import Request, status



adminRouter = APIRouter()




@adminRouter.get("/admin")
async def admin(request: Request):
    cookies = request.cookies

    if "jwt-token" in cookies:
        token = cookies["jwt-token"]
        res = methods.validate_token(token)
    
        if res["result"]:
            return status.HTTP_202_ACCEPTED
        
        else:
            return {
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": res["message"]
                }
        
    else:
        return {
            "status": status.HTTP_401_UNAUTHORIZED,
            "message": "No token provided"
        }



@adminRouter.get("/admin/protected")
@protected
async def admin(request: Request):
    return request.headers
    