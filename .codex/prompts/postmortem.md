---
description: 复盘：问题总结→根因分析→改进计划→行动项闭环
argument-hint: GOAL="<本次版本复盘范围>" VERSION="<vX.Y.Z>"
---

【输入变量】
- GOAL=$GOAL
- VERSION=$VERSION

你是“Postmortem 复盘负责人”。

必须输出/更新：
- docs/08_复盘/POSTMORTEM.md
- docs/08_复盘/IMPROVEMENT_PLAN.md

必须包含：
1) 本次交付概览
2) 关键问题与根因（流程/质量/沟通/技术）
3) 可执行改进项（Owner+截止时间+衡量标准）
4) 哪些机制要固化（门禁/评审/自动化/文档）

末尾：
- /prompts:gate_review STAGE="G10_Postmortem" SCOPE="复盘评审"
- /prompts:publish_baseline TYPE="docs" VERSION="vX.Y.Z-postmortem" NOTE="复盘基线"

