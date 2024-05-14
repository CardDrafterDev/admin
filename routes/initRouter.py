from .adminRouter import adminRouter

from fastapi import APIRouter


Router = APIRouter()

Router.include_router(adminRouter)
