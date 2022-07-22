from fastapi import FastAPI
from routers import items
import uvicorn

app = FastAPI()

app.include_router(items.router)

if __name__ == '__main__':
    uvicorn.run("main:app", port=80, reload=True)