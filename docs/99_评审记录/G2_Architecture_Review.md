# G2 Architecture Review

## Stage
- STAGE: G2_Architecture
- SCOPE: 架构与任务评审

## Artifacts
### 已具备
- docs/02_架构/SYSTEM_MAP.md
- docs/04_实现/TASKS.md
- docs/03_设计/QUALITY_GATE.md

### 缺失
- docs/00_需求/PRD.md
- docs/00_需求/SRS.md
- docs/00_需求/ACCEPTANCE.md
- docs/00_需求/FUNCTION_LIST.md
- docs/05_测试/CASES.md
- docs/05_测试/REGRESSION_CHECKLIST.md
- docs/04_实现/TRACEABILITY.md

## Risks & Blockers
- Blocker: 需求与验收标准缺失，无法评估可测试性（Owner=Customer）
- Blocker: 用例/回归清单缺失，测试闭环无法建立（Owner=QA）
- Blocker: 需求-任务-用例追踪链缺失（Owner=PM/RD Lead）

## Conclusion
- FAIL

## Release List (if PASS)
- docs only (N/A)

## Next Actions
- /prompts:customer GOAL="补齐PRD/SRS/ACCEPTANCE/FUNCTION_LIST"
- /prompts:qa_tester GOAL="补齐测试用例与回归清单骨架"
- /prompts:pm GOAL="建立TRACEABILITY追踪链" ACTION="plan"
