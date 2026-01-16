# TRACEABILITY

## 1. 编号规则
### 需求编号
- PRD: PRD-RMP-001
- 用户故事: US-<需求编号>-<序号>（例如：US-PRD-RMP-001-01）
- 验收标准: ACC-<需求编号>-<序号>（例如：ACC-PRD-RMP-001-01）

### 任务编号
- TASK: PROJ-YYYYMMDD-XXX（例如：PROJ-20260117-201）

### 测试编号
- 用例: CASE-<模块>-<序号>（例如：CASE-REQ-01）
- 回归: REG-<模块>-<序号>（例如：REG-REQ-01）

## 2. 追踪链结构
需求(PRD/US/ACC) → 任务(TASK) → 代码(分支/MR) → 用例(CASE) → 回归(REG) → 测试报告

## 3. 需求 → 任务映射（示例）
| PRD/US/ACC | TASK_ID | 任务标题 | Owner角色 |
| --- | --- | --- | --- |
| PRD-RMP-001 | PROJ-20260116-102 | 需求管理 | Dev |
| PRD-RMP-001 | PROJ-20260116-103 | 研发管理 | Dev |
| PRD-RMP-001 | PROJ-20260116-105 | CI 管理 | Dev |
| PRD-RMP-001 | PROJ-20260116-107 | 自动化测试 | QA |
| PRD-RMP-001 | PROJ-20260116-109 | Bug 管理 | Dev |
| PRD-RMP-001 | PROJ-20260116-110 | 版本发布 | Dev |

## 4. 任务 → 用例映射（示例）
| TASK_ID | CASE_ID | 用例说明 |
| --- | --- | --- |
| PROJ-20260116-102 | CASE-REQ-01 | 需求状态流转 |
| PROJ-20260116-103 | CASE-DEV-01 | 任务评审流程 |
| PROJ-20260116-105 | CASE-CI-01 | 流水线失败定位 |
| PROJ-20260116-107 | CASE-TEST-01 | 测试计划执行 |
| PROJ-20260116-109 | CASE-BUG-01 | Bug 复现与回归 |
| PROJ-20260116-110 | CASE-REL-01 | 发布审批与记录 |

## 5. 回归覆盖规则
- 所有 P0 功能必须有 REG-<模块>-<序号> 对应回归项
- 关键状态流转必须进入回归清单
