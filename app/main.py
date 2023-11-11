from fastapi import FastAPI
from .routers import index as index_router


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(index_router.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
