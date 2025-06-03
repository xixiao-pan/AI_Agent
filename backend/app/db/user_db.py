import json
import os

USER_DB_PATH = "./backend/user_db.json"

def load_user_db():
    """加载用户数据库（JSON 文件）"""
    if not os.path.exists(USER_DB_PATH):
        with open(USER_DB_PATH, 'w') as f:
            json.dump({}, f)
    with open(USER_DB_PATH, 'r') as f:
        return json.load(f)

def save_user_db(db):
    """保存用户数据库到 JSON 文件"""
    with open(USER_DB_PATH, 'w') as f:
        json.dump(db, f, indent=2)