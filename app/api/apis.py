from fastapi import APIRouter
from .user_route import routes as user_router
from .customer_route import router as customer_router
router= APIRouter()

router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(customer_router, prefix="/customer", tags=["customer"])