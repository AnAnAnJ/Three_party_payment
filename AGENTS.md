# AGENTS 指南

面向贡献者的快速指引，聚焦三方支付接口自动化测试场景，遵循 KISS、DRY、YAGNI 与 SOLID 原则。

## 目录速览
- `case/`：FastAPI 入口 `api.py` 以及接口/数据比对用例。
- `func/`：YAML 配置（如 `url_config.yaml`），供请求拼装读取。
- `lib/`：通用工具（如 `get_yaml_data.py`），封装公共读取逻辑。
- `util/`：预留日志与通用工具位，避免重复实现。
- `report/`：测试报告输出目录。

## 快速开始
1) 创建虚拟环境并安装依赖：
   - `python3 -m venv .venv`
   - `source .venv/bin/activate`
   - `pip install -r requirements.txt`
2) 启动接口（默认 127.0.0.1:4567）：`uvicorn case.api:app --host 127.0.0.1 --port 4567`
3) 运行用例：`pytest case`，或使用 `pytest case/test_api_query_goods.py -k goods -vv` 聚焦调试。

## 开发规范
- 遵循 PEP 8、4 空格缩进，命名采用蛇形（函数/变量）与帕斯卡（类）。
- HTTP 调用必须设置超时，默认开启 `verify=True`，如需关闭仅限测试环境并说明原因。
- 抽取复用：公共请求头、基础配置放入 `util/` 或独立函数，避免复制粘贴。
- 单一职责：登录、数据获取、断言拆分清晰，便于扩展不同项目或 `page_name`。

## 测试与验证
- 测试命名 `test_*`，断言状态码与关键业务字段（如支付配置/商品列表完整性）。
- 外部依赖不稳定时使用 `--maxfail=1` 或标记跳过，优先考虑本地 mock。
- 生成报告可结合 `pytest --junitxml=report/result.xml`，与 README 说明保持一致。

## 安全与提交
- 不提交密钥或真实账号；配置通过 YAML/环境变量注入，必要时忽略敏感文件。
- 依赖升级前先在隔离环境验证；接口或配置变更需同步 README/示例。
- Git 提交建议单一主题（如 `feat: add goods query test`），PR 写明变更摘要、验证方式与影响范围。
