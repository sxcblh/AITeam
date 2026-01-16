# QUALITY GATE

## 目标
- 统一编译/单测/提测门禁标准，确保可追踪与可复现。

## 门禁标准
### Build Gate
- build_gate PASS
- 产物与日志路径：artifacts/build/<version>/
- 失败必须回到开发修复后重试

### Unit Test Gate
- unit_test_gate PASS
- 报告路径：artifacts/unit_test/<version>/
- 关键功能至少有单测用例覆盖

### QA Gate
- 仅在 build_gate 与 unit_test_gate PASS 后进入 QA
- QA 需输出测试报告与缺陷清单
- 截图路径：artifacts/qa/screenshots/
- 日志路径：artifacts/qa/logs/

## 提测标准
- build_gate PASS
- unit_test_gate PASS
- 关键功能有用例 + 回归清单更新

## 协作方式
- 分支策略：feature/ 或 bugfix/ 或 docs/
- MR/PR 评审：至少 1 名评审；状态机/权限变更需 2 名评审
- 合并前必须通过 build_gate 与 unit_test_gate
- commit message 必须中文且包含 TASK_ID

## 证据归档
- artifacts/build/<version>/
- artifacts/unit_test/<version>/
- artifacts/qa/screenshots/
- artifacts/qa/logs/
