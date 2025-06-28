from fastapi import APIRouter, Request
from fastapi.responses import FileResponse, JSONResponse
from app.db.user_db import load_user_db, save_user_db
import os
from datetime import datetime
import uuid

router = APIRouter()
STATIC_LOGO_PATH = "./backend/static"
PLACEHOLDER = os.path.join(STATIC_LOGO_PATH, "placeholder_logo.png")

@router.post("/generate/{user_id}/{task_id}")
async def generate_logo(user_id: str, task_id: str, request: Request):
    data = await request.json()
    prompt = data["prompt"]

    logo_id = f"logo_{datetime.utcnow().timestamp()}"
    image_path = os.path.join(STATIC_LOGO_PATH, f"{logo_id}.png")
    with open(PLACEHOLDER, "rb") as src, open(image_path, "wb") as dst:
        dst.write(src.read())

    db = load_user_db()
    if user_id not in db:
        return JSONResponse(status_code=404, content={"error": "User not found"})

    user_tasks = db[user_id].get("task", [])
    task_found = False
    for task in user_tasks:
        if task["task_id"] == task_id:
            task["history"].append({
                "timestamp": datetime.utcnow().isoformat(),
                "prompt": prompt,
                "logo_id": logo_id,
                "image_path": f"/logo/static/{logo_id}.png"
            })
            task_found = True
            break

    if not task_found:
        return JSONResponse(status_code=404, content={"error": "Task ID not found for user"})

    save_user_db(db)

    return {
        "status": "ok",
        "task_id": task_id,
        "logo_id": logo_id,
        "image_path": f"/logo/static/{logo_id}.png"
    }

@router.get("/static/{filename}")
def get_logo_image(filename: str):
    path = os.path.join(STATIC_LOGO_PATH, filename)
    if os.path.exists(path):
        return FileResponse(path)
    return JSONResponse(status_code=404, content={"error": "File not found"})