from .start import router as start_router
from .subscriptions import router as subscriptions_router
from .news import router as news_router

routers = [start_router, news_router, subscriptions_router]