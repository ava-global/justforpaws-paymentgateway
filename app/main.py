from fastapi import FastAPI
import uvicorn
from app.api.api_v1.api import api_router

app = FastAPI(
    title='Just for paw payment gateway', openapi_url='/v1/openapi.json'
)

app.include_router(api_router, prefix='/v1')

if __name__ == '__main__':
    uvicorn.run(app, port=8082, host='0.0.0.0')
