# SYSTEM MAP

## 模块概览
- tools/task_board.py：Excel 任务板读写与字段映射
- ops/tasks.xlsx：任务数据源
- .codex/prompts：流程化提示模板
- backend/：后端服务（FastAPI）
- web-console/：前端应用（React）

## 数据流
- 用户 -> task_board.py -> ops/tasks.xlsx
- prompts -> docs/* 落盘

## 边界
- 本次变更仅涉及工具与文档，不修改后端/前端功能
