from fastapi import HTTPException
from fastapi.responses import JSONResponse



def http_error_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )