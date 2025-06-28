from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import user, logo
from app.routes import task  # 引入 task 路由
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 创建静态文件目录
STATIC_LOGO_PATH = "./backend/static"
os.makedirs(STATIC_LOGO_PATH, exist_ok=True)

# 引入路由
app.include_router(user.router, prefix="/user", tags=["user"])
app.include_router(logo.router, prefix="/logo", tags=["logo"])
app.include_router(task.router, prefix="/task", tags=["task"])