from fastapi.responses import JSONResponse



def handle_http_exception(exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )
