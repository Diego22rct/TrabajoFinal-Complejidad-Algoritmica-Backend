from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.routers import graph_route, index


app = FastAPI()


@app.get("/")
async def root():
    """
    Redirect to /docs.
    """
    return RedirectResponse(url="/docs")


app.include_router(index.router)
app.include_router(graph_route.router)
