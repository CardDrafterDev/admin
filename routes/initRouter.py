from fastapi import APIRouter

from .adminRouter import adminRouter



Router = APIRouter()

Router.include_router(adminRouter)
