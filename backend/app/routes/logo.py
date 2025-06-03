from fastapi import APIRouter, Request
from fastapi.responses import FileResponse, JSONResponse
from app.db.user_db import load_user_db, save_user_db
import os
from datetime import datetime

router = APIRouter()
STATIC_LOGO_PATH = "./backend/static"
PLACEHOLDER = os.path.join(STATIC_LOGO_PATH, "placeholder_logo.png")

@router.post("/generate")
async def generate_logo(request: Request):
    data = await request.json()
    user_id = data["user_id"]
    prompt = data["prompt"]

    logo_id = f"logo_{datetime.utcnow().timestamp()}"
    image_path = os.path.join(STATIC_LOGO_PATH, f"{logo_id}.png")
    with open(PLACEHOLDER, "rb") as src, open(image_path, "wb") as dst:
        dst.write(src.read())

    db = load_user_db()
    if user_id in db:
        db[user_id]["history"].append({
            "timestamp": datetime.utcnow().isoformat(),
            "prompt": prompt,
            "logo_id": logo_id,
            "image_path": f"/logo/static/{logo_id}.png"
        })
        save_user_db(db)
    return {"status": "ok", "logo_id": logo_id, "image_path": f"/logo/static/{logo_id}.png"}

@router.get("/static/{filename}")
def get_logo_image(filename: str):
    path = os.path.join(STATIC_LOGO_PATH, filename)
    if os.path.exists(path):
        return FileResponse(path)
    return JSONResponse(status_code=404, content={"error": "File not found"})