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
| PROJ-20260116-101 | PRD-RMP-001 | Arch | 模块边界与状态机 | 定义平台模块边界、核心状态机与权限矩阵 | Architect | 待定 | P0 | TODO | 2.5 | feature/PROJ-20260116-101-arch | - | 模块边界+状态机清单+权限矩阵评审通过 | SYSTEM_MAP#模块; DETAIL_DESIGN#Arch | CASES#Arch-01 | - | 2026-01-16 | - |
| PROJ-20260116-102 | PRD-RMP-001 | 需求管理 | PRD/用户故事/验收标准 | 需求录入、用户故事拆分、验收标准管理与状态流转 | Dev | 待定 | P0 | TODO | 3.0 | feature/PROJ-20260116-102-req | PROJ-20260116-101 | 状态流转可配置；验收口径可追溯 | PRD#RMP; SRS#RMP | CASES#REQ-01~05 | - | 2026-01-16 | - |
| PROJ-20260116-103 | PRD-RMP-001 | 研发管理 | 任务拆解/分支策略/MR评审 | 研发任务管理、分支策略约束、MR/PR评审流转 | Dev | 待定 | P0 | TODO | 3.0 | feature/PROJ-20260116-103-devmgmt | PROJ-20260116-101 | 任务-分支-评审可追踪；审计记录完整 | PRD#RMP; QUALITY_GATE#Review | CASES#DEV-01~04 | - | 2026-01-16 | - |
| PROJ-20260116-104 | PRD-RMP-001 | 研发统计 | 指标口径与趋势 | 提交次数/评审时长/缺陷密度等统计与趋势 | Algo | 待定 | P1 | TODO | 2.0 | feature/PROJ-20260116-104-metrics | PROJ-20260116-103 | 指标口径文档化；趋势图可复算 | PRD#RMP; DETAIL_DESIGN#Metrics | CASES#MET-01~03 | - | 2026-01-16 | - |
| PROJ-20260116-105 | PRD-RMP-001 | CI管理 | 流水线状态与失败定位 | 汇总流水线状态、失败步骤定位与日志摘要 | Dev | 待定 | P0 | TODO | 3.0 | feature/PROJ-20260116-105-ci | PROJ-20260116-101 | 失败步骤+日志摘要可定位 | PRD#RMP; SRS#CI | CASES#CI-01~04 | - | 2026-01-16 | - |
| PROJ-20260116-106 | PRD-RMP-001 | CI管理 | 构建产物管理 | 构建产物索引、下载与版本关联 | Dev | 待定 | P0 | TODO | 2.0 | feature/PROJ-20260116-106-artifacts | PROJ-20260116-105 | 产物可追溯且与版本关联 | PRD#RMP; SRS#CI | CASES#CI-05~06 | - | 2026-01-16 | - |
| PROJ-20260116-107 | PRD-RMP-001 | 自动化测试 | 用例库/计划/报告 | 用例库管理、测试计划编排、报告生成 | QA | 待定 | P0 | TODO | 3.0 | feature/PROJ-20260116-107-test | PROJ-20260116-101 | 计划与报告可回溯；用例可复用 | PRD#RMP; SRS#Test | CASES#TEST-01~04 | - | 2026-01-16 | - |
| PROJ-20260116-108 | PRD-RMP-001 | 自动化测试 | 覆盖率与趋势 | 覆盖率统计口径、趋势展示与告警阈值 | Algo | 待定 | P1 | TODO | 2.0 | feature/PROJ-20260116-108-coverage | PROJ-20260116-107 | 覆盖率趋势可复算；口径可配置 | PRD#RMP; DETAIL_DESIGN#Coverage | CASES#COV-01~03 | - | 2026-01-16 | - |
| PROJ-20260116-109 | PRD-RMP-001 | Bug管理 | 提交/分派/复现/修复/验证/回归 | Bug 全流程状态机与回归闭环 | Dev | 待定 | P0 | TODO | 3.0 | feature/PROJ-20260116-109-bug | PROJ-20260116-101 | 状态机完整；回归清单更新 | PRD#RMP; SRS#Bug | CASES#BUG-01~05 | - | 2026-01-16 | - |
| PROJ-20260116-110 | PRD-RMP-001 | 版本发布 | 版本号/变更清单/审批/记录 | 版本发布流程与审批记录 | Dev | 待定 | P0 | TODO | 3.0 | feature/PROJ-20260116-110-release | PROJ-20260116-101 | 版本发布可审计；变更清单可追溯 | PRD#RMP; SRS#Release | CASES#REL-01~04 | - | 2026-01-16 | - |
| PROJ-20260116-111 | PRD-RMP-001 | 版本发布 | 灰度/回滚策略 | 支持灰度发布与回滚记录 | Dev | 待定 | P1 | TODO | 2.5 | feature/PROJ-20260116-111-gray | PROJ-20260116-110 | 灰度比例可配置；回滚可追踪 | PRD#RMP; SRS#Release | CASES#REL-05~06 | - | 2026-01-16 | - |
| PROJ-20260116-112 | PRD-RMP-001 | UI | 核心页面信息架构 | 核心页面布局与交互规范 | UI | 待定 | P0 | TODO | 2.0 | feature/PROJ-20260116-112-ui | PROJ-20260116-101 | 页面IA与交互规范评审通过 | DETAIL_DESIGN#UI | CASES#UI-01~04 | - | 2026-01-16 | - |
| PROJ-20260116-113 | PRD-RMP-001 | Doc | 文档与门禁 | PRD/SRS/QUALITY_GATE/回归清单完善 | Doc | 待定 | P0 | TODO | 1.5 | docs/PROJ-20260116-113-docs | - | 文档结构完整；门禁标准明确 | PRD#RMP; QUALITY_GATE | CASES#DOC-01 | - | 2026-01-16 | - |
