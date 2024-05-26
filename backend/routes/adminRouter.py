import methods

from decorators import protected

from fastapi import APIRouter
from fastapi import Request, status



adminRouter = APIRouter()


@adminRouter.get("/admin/cards")
@protected
async def admin(request: Request):
    return request.headers
