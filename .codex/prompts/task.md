---
description: task：sync/start/commit/finish/switch（Excel任务板 + Git分支交付 + 快照重置）
argument-hint: ACTION=sync|start|commit|finish|switch [TASK_ID=TASK-xxxx] [MSG="提交说明(中文)"]
---

ACTION=$ACTION
TASK_ID=$TASK_ID
MSG=$MSG

任务源：ops/tasks.xlsx（python tools/task_board.py）
硬规则：
- 不要询问是否继续
- 禁止直接向 main 提交
- commit message 必须中文且包含 TASK_ID
- finish 必须 push 到服务器
- 每开始新任务前必须更新 docs/01_计划/CONTEXT_SNAPSHOT.md（用于重置环境避免输入上限）

如果 ACTION=sync：
- python tools/task_board.py list --status TODO,DOING --pretty
- 同步/生成：
    - docs/01_计划/PROGRESS.md（进度表）
    - docs/04_实现/TASKS.md（任务表）
- 对每个 TODO 任务追加 WorkLog（简短：计划与风险）
- 输出：建议优先做哪3个任务（含理由）

如果 ACTION=start：
1) 读取任务：
    - python tools/task_board.py get --task-id $TASK_ID --pretty
2) 生成分支名：
    - python tools/task_board.py suggest-branch --task-id $TASK_ID --pretty
3) 更新快照（必须）：
    - 写 docs/01_计划/CONTEXT_SNAPSHOT.md（任务目标/分支/约束/下一步）
4) 执行 git：
    - git fetch --all
    - git checkout main
    - git pull
    - git checkout -b <branch>
5) 回写 Excel：
    - python tools/task_board.py update --task-id $TASK_ID Status=DOING Branch=<branch> Progress=0
    - python tools/task_board.py append-log --task-id $TASK_ID "开始开发：已创建分支 <branch>"

如果 ACTION=commit：
- 如果未提供 TASK_ID：允许省略（脚本可从当前分支推断）
1) git status / git diff --staged
2) 生成提交信息（必须中文+含TASK_ID）：
    - feat/fix/refactor/test/docs/chore: 中文摘要 [TASK_ID]
3) git commit -m "<message>"
4) 记录到 Excel：
    - python tools/task_board.py append-log "提交：<hash> <message>；自测：<结果或建议命令>"
    - python tools/task_board.py update Progress=<0-100>（可选）

如果 ACTION=finish：
- 如果未提供 TASK_ID：允许省略（脚本可从当前分支推断）
1) 汇总 + 推送：
    - git branch --show-current
    - git log --oneline -n 30
    - git diff main...HEAD --stat
    - git push -u origin HEAD
2) 生成 MR/PR 描述文本（并写入 WorkLog）：
    - 背景/需求（TASK_ID）
    - 实现要点
    - 变更文件
    - 测试结果（编译/单测命令）
    - 风险与回滚
3) 更新 Excel：
    - python tools/task_board.py update Status=REVIEW Progress=95
    - python tools/task_board.py append-log "进入评审：已推送分支；MR描述：<摘要>"

如果 ACTION=switch：
1) git status（必须干净）
2) 若不干净：要求先 wip 提交（中文+TASK_ID）
3) git checkout main && git pull
4) git checkout <目标分支> 或 git checkout -b <新分支>
5) 更新快照 docs/01_计划/CONTEXT_SNAPSHOT.md（切换原因/当前任务/下一步）
