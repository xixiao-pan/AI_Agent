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
            "history": []
        }
        save_user_db(db)
    return {"status": "ok", "user": db[user_id]}

@router.get("/history/{user_id}")
def get_user_history(user_id: str):
    db = load_user_db()
    if user_id in db:
        return {"history": db[user_id].get("history", [])}
    return JSONResponse(status_code=404, content={"error": "User not found"})