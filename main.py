from fastapi import FastAPI


import routes.initRouter as initRouter


server = FastAPI()



server.include_router(initRouter.Router)

@server.get("/")
async def root():
    return "Root :)"
