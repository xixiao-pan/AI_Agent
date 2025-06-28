from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.db.user_db import load_user_db, save_user_db

router = APIRouter()

@router.post("/init")
async def init_user(request: Request):
    data = await request.json()
    user_id = data["user_id"]
    db = load_user_db()

    if user_id not in db:
        db[user_id] = {
            "name": data.get("name", ""),
            "organization": data.get("organization", ""),
            "role": data.get("role", ""),
            "logo_preferences": {},
            "task": [  # 初始化一个默认任务
                # {
                #     "task_id": "task_0",
                #     "company_name": data.get("company_name", ""),
                #     "industry_field": data.get("industry_field", ""),
                #     "history": []
                # }
            ]
        }
        save_user_db(db)

    return {"status": "ok", "user": db[user_id]}

@router.get("/login")
async def login_user(request: Request):
    data = await request.json()
    user_id = data["user_id"]
    db = load_user_db()

    if user_id in db:
        return {"status": "ok", "user": db[user_id]}
    return JSONResponse(status_code=404, content={"error": "User not found"})


@router.get("/history/{user_id}")
def get_user_history(user_id: str):
    db = load_user_db()
    if user_id in db:
        tasks = db[user_id].get("task", [])
        return {"history": tasks}  # 返回所有 task 的历史
    return JSONResponse(status_code=404, content={"error": "User not found"})