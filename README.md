# 三方支付接口自动化测试

基于 FastAPI + pytest 的三方支付校验脚手架，主要完成接口触发、商品信息查询与 admin 配置比对，确保 API 返回的数据与后台一致。

## 环境要求
- Python 3.8+
- `pip` 可用（建议使用虚拟环境隔离依赖）

## 快速开始
```bash
python3 -m venv .venv
source .venv/bin/activate3
pip install -r requirements.txt  #pip3 freeze > requirements.txt
```

## 目录结构
- `case/`：FastAPI 入口 `api.py` 与核心用例（商品查询、admin 比对等）。
- `func/`：配置文件（如 `url_config.yaml`）用于拼装请求地址。
- `lib/`：通用工具与数据读取。
- `util/`：预留日志或公共封装。
- `report/`：测试报告输出目录。

## 运行接口
- 启动：`uvicorn case.api:app --host 127.0.0.1 --port 4567`
- 文档：`http://127.0.0.1:4567/docs`
- 示例请求：
  ```bash
  curl -X POST "http://127.0.0.1:4567/third_party_payment" \
    -H "Content-Type: application/json" \
    -d '{"items":[{"page_name":"Drift","bundle_id":"com.Drift.cf.ios"}]}'
  ```

## 运行测试
- 全量：`pytest case`
- 聚焦：`pytest case/test_api_query_goods.py -k goods -vv`
- 生成报告（示例）：`pytest case --junitxml=report/result.xml`

## 开发提示
- 遵循 PEP 8，使用 4 空格缩进。
- 所有 HTTP 请求设置超时，默认 `verify=True`，仅在测试环境显式关闭并注明原因。
- 公共请求头、配置读取等逻辑集中到 `util/` 或工具函数，避免重复实现。

## 常见问题
- 找不到配置：确认 `func/url_config.yaml` 是否包含目标环境与项目配置。
- 证书校验失败：仅在受控测试环境下使用 `verify=False`，生产环境保持证书校验。
