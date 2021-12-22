from fastapi import FastAPI, Depends
from starlette.requests import Request
import uvicorn
import gunicorn

from app.api.api_v1.routers.users.users import users_router
from app.api.api_v1.routers.auth.auth import auth_router
from app.api.api_v1.routers.area.area import area_router
from app.api.api_v1.routers.live.live import live_router
from fastapi.middleware.cors import CORSMiddleware


from app.core import config
from app.db.session import SessionLocal
from app.core.auth import get_current_active_user
from app.core.celery_app import celery_app
from app import tasks



app = FastAPI(
    title=config.PROJECT_NAME, docs_url="/api/docs", openapi_url="/api"
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    # response.headers[ {'Access-Control-Expose-Headers', 'Content-Range'}]
    # response.headers['Content-Range','bytes : 0-9/*']

    request.state.db.close()
    return response

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # Access-Control-Expose-Headers
    # acces_control_expose_headers=True

)


@app.get("/api/v1")
async def root():
    return {"message": "Hello World"}


@app.get("/api/v1/task")
async def example_task():
    celery_app.send_task("app.tasks.example_task", args=["Hello World"])

    return {"message": "success"}


# Routers
app.include_router(
    users_router,
    prefix="/api/v1",
    tags=["users"],
    dependencies=[Depends(get_current_active_user)],
)
app.include_router(auth_router, prefix="/api", tags=["auth"])
app.include_router(area_router, prefix="/api" , tags=["area"])
app.include_router(live_router, prefix="/api", tags=["live"])

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8888,workers=4)
    
    

# gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80