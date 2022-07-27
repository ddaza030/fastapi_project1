from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from routers import items
import uvicorn
from starlette.exceptions import HTTPException as StarletteHTTPException
from pydantic import ValidationError
from utils.telegram.mibot import MiBot

app = FastAPI()


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    content = {"success": False,
               "message": exc.detail,
               "data": None}
    return JSONResponse(status_code=exc.status_code, content=content)


@app.exception_handler(RequestValidationError)
async def request_validation_exception_handler(request, exc):
    content = {"success": False,
               "message": str(exc),
               "data": None}
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                        content=content)


@app.exception_handler(ValidationError)
async def validation_exception_handler(request, exc):
    content = {"success": False,
               "message": str(exc),
               "data": None}
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        content=content)

async def get_current_user()

app.include_router(items.router)
app.telegram = MiBot()

if __name__ == '__main__':
    uvicorn.run("main:app", port=80, reload=True)
