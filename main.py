from fastapi import FastAPI
from routers import items
import uvicorn

from utils.telegram.mibot import MiBot


app = FastAPI()

# TODO: manera correcta de usar current_app
app.include_router(items.router)
app.telegram = MiBot()

if __name__ == '__main__':
    uvicorn.run("main:app", port=80, reload=True)
