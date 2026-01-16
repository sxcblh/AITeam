# ALM + DevOps Platform (MVP Skeleton)

一个从 0 起步的研发管理平台骨架：**需求 / Bug / CI 聚合 / 版本发布**。

- Backend: **FastAPI + SQLAlchemy + Alembic + JWT + RBAC**
- Frontend: **React + TypeScript + Vite**
- Infra: **PostgreSQL + Redis**（docker-compose 一键启动）

## 快速启动

### 1) 启动基础设施（Postgres + Redis）

```bash
cd ops
docker compose up -d
```

### 2) 启动后端

```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt

# 初始化数据库
alembic upgrade head

# 启动
uvicorn app.main:app --reload --port 8000
```

访问：
- API 文档：`http://localhost:8000/docs`

### 3) 启动前端

```bash
cd web-console
npm i
npm run dev
```

访问：
- Web Console：`http://localhost:5173`

## 默认账号（开发模式）

- admin / admin123

> ⚠️ 这是骨架示例，仅用于本地开发。

---

## MVP 已包含

- ✅ JWT 登录 / RBAC（admin / member）
- ✅ 项目 Project CRUD
- ✅ 需求 Requirement CRUD
- ✅ Bug CRUD
- ✅ 版本 Release CRUD
- ✅ GitLab Webhook 接收端点（占位 + 保存事件）

## 下一步建议

- Task（任务）与 MR / Pipeline 的关联
- CI 失败摘要（接入 Codex / LLM）
- 测试报告入库（JUnit / Allure）
- 发布审批 / 灰度 / 回滚

