import routes.initRouter as initRouter

from fastapi import FastAPI


server = FastAPI()


server.include_router(initRouter.Router)

@server.get("/")
async def root():
    return "Root :)"
