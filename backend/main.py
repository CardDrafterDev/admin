import routes.initRouter as initRouter
from middleware.cors import setup_cors

from fastapi import FastAPI


server = FastAPI()


server.include_router(initRouter.Router)

setup_cors(app=server)

@server.get("/")
async def root():
    return "Root :)"
