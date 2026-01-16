# 详细设计

## 关键改动
- 扩展 CANON/CN_HEADERS/ALIASES
- list/get 支持补齐表头并保存
- 统一 stdout/stderr 为 UTF-8

## 字段映射
- 采用中文表头写入 Excel
- TaskID 作为 TASK_ID 的别名

## 兼容策略
- 保留现有字段与命令行为
- 新字段默认空值
