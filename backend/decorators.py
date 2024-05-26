from methods import validate_token

from fastapi import status, Request
from functools import wraps


def protected(func):
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
        token = request.cookies.get("jwt-token")
        if token == None:
            return {
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": "Unauthorized"
            }
        if validate_token(token)["result"]:
            return await func(request, *args, **kwargs)
        
    return wrapper
 