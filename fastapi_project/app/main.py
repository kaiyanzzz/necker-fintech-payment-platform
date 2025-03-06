from fastapi import FastAPI
from app.routers import users, items
from app.database import engine, Base

# 创建数据库表（如果使用 Alembic，可省略）
Base.metadata.create_all(bind=engine)

app = FastAPI()

# 注册路由
app.include_router(users.router)
app.include_router(items.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI project!"}
