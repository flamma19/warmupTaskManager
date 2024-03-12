import uvicorn
from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="Warmup Task Manager API",
    description="A simple API to manage your tasks, warmup project",
    version="0.1.0",
    docs_url='/docs',
    redoc_url='/redoc',
    openapi_url='/openapi.json',
)

app.include_router(router)


@app.get("/")
async def root():
    return {"message": "API is running"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
