from fastapi import FastAPI
from .routers import index as index_router
from .routers import graph_route as graph_router


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(index_router.router)
app.include_router(graph_router.router)
