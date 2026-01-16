# DEPENDENCY RULES

## 允许依赖
- tools/* 可依赖 ops/* 与 docs/*
- docs/* 不依赖代码模块
- backend 与 web-console 不依赖 tools

## 禁止依赖
- tools 不可依赖 web-console
- backend 不可依赖 docs

## 现状问题与建议
- 终端编码差异导致输出混乱：建议统一 UTF-8 输出
