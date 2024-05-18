from .loginRouter import loginRouter
from .adminRouter import adminRouter

from fastapi import APIRouter


Router = APIRouter()

Router.include_router(loginRouter)
Router.include_router(adminRouter)
