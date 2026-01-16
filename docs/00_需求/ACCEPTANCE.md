# 验收标准 ACCEPTANCE

1) Given 需求为草稿，When 提交评审，Then 状态为评审中  
2) Given PRD 已确认，When 拆分用户故事，Then 用户故事进入已确认状态  
3) Given 用户故事已确认，When 开发开始，Then 状态为实现中  
4) Given MR/PR 提交，When 评审完成，Then 记录评审结论与时间  
5) Given CI 失败，When 查看流水线详情，Then 显示失败步骤与日志摘要  
6) Given 构建成功，When 查看产物，Then 产物可下载且关联版本  
7) Given 测试计划已发布，When 执行用例，Then 生成测试报告  
8) Given 覆盖率统计开启，When CI 完成，Then 覆盖率趋势更新  
9) Given Bug 已分派，When 修复提交，Then 状态为待验证  
10) Given 回归通过，When 关闭 Bug，Then 状态为已关闭  
11) Given 发布审批开启，When 审批拒绝，Then 发布被阻止并记录原因  
12) Given 灰度发布中，When 触发回滚，Then 状态为回滚并记录日志  
