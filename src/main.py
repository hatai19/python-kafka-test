from fastapi import FastAPI

from applications.routers import applications_router
from applications.dependencies import kafka_router

app = FastAPI()

app.include_router(applications_router)
app.include_router(kafka_router)

if __name__=='__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)