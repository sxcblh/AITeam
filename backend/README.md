# Backend

## 运行

```bash
cp .env.example .env
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload --port 8000
```

## 结构

- app/main.py: 入口
- app/api/v1: 路由
- app/models: ORM
- app/schemas: Pydantic
- app/core: 配置 / 鉴权
- alembic: 迁移
