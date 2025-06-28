from fastapi import APIRouter, Request
from app.db.user_db import load_user_db, save_user_db
import uuid
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/{user_id}/init")
async def init_task(user_id: str, request: Request):
    data = await request.json()
    company_name = data["company_name"]
    industry_field = data["industry_field"]

    db = load_user_db()
    if user_id not in db:
        return {"status": "error", "message": "User not found"}

    task_id = f"task_{str(uuid.uuid4())[:8]}"
    new_task = {
        "task_id": task_id,
        "company_name": company_name,
        "industry_field": industry_field,
        "messages": [],
        "history": []
    }

    db[user_id]["task"].append(new_task)
    save_user_db(db)

    return {"status": "ok", "task_id": task_id, "task": new_task}

# GET /user/{user_id}/tasks
@router.get("/{user_id}/tasks")
def get_user_tasks(user_id: str):
    db = load_user_db()
    if user_id not in db:
        return JSONResponse(status_code=404, content={"error": "User not found"})
    return {"tasks": db[user_id].get("task", [])}

