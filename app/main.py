from fastapi import FastAPI

from .routers import index as index_router
from fastapi.responses import RedirectResponse

# from .routers import graph_route as graph_router


app = FastAPI()


@app.get("/")
async def root():
    """
    Redirect to /docs.
    """
    return RedirectResponse(url="/docs")


app.include_router(index_router.router)
# app.include_router(graph_router.router)
