# 任务清单 TASKS

> 维护规则：
> - 每个任务必须具备：验收标准(DoD) + 分支 + 关联用例
> - 每个任务开发必须在独立分支完成（feature/ 或 bugfix/）
> - 每次提交（commit）必须包含 TASK_ID 且中文描述
> - DONE 之前必须：
    >   1) push 到服务器
>   2) 发起 MR/PR
>   3) 通过 Gate Review（代码评审/编译门禁/单测门禁/测试门禁按阶段）

状态枚举：TODO / DOING / REVIEW / BLOCKED / DONE / RELEASED

| TASK_ID | 需求ID | 模块 | 标题 | 任务说明 | Owner角色 | Owner | 优先级 | 状态 | 预估(人日) | 分支(branch) | 依赖任务 | 验收标准(DoD) | 关联文档 | 测试用例 | MR/PR链接 | 最后更新 | 备注 |
|--------|--------|------|------|----------|----------|-------|--------|------|-----------|--------------|----------|---------------|----------|----------|----------|----------|------|
| PROJ-20260116-001 | PRD-001 | Auth | 登录与权限校验 | 支持账号密码登录、鉴权拦截、权限缓存 | Dev | 张三 | P0 | TODO | 1.5 | feature/PROJ-20260116-001-auth | - | 见ACCEPTANCE#A1-A3；单测>=3条 | DETAIL_DESIGN#Auth | CASES#Auth-01~03 | - | 2026-01-16 | - |
| PROJ-20260116-002 | PRD-001 | UI | 登录界面 | QML登录页，控件可自动化定位 | UI | 李四 | P0 | TODO | 1.0 | feature/PROJ-20260116-002-login-ui | PROJ-20260116-001 | objectName齐全；冒烟通过 | DETAIL_DESIGN#UI | CASES#UI-Login | - | 2026-01-16 | - |
