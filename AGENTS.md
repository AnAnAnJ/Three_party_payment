# Repository Guidelines

## 项目结构与模块组织
- `case/`：API示例与接口测试脚本，`api.py`提供FastAPI入口，`test_query_goods.py`封装三方支付查询流程，`test_data_*`预留校验用例。
- `util/`：预留日志或通用工具目录（当前为空，可放日志配置、公共请求封装等）。
- `README.md`：包含环境搭建与框架说明，可作为入口阅读。

## 构建、测试与开发命令
- 环境：`python3 -m venv .venv && source .venv/bin/activate`；`pip install -r requirements.txt`（如缺失文件，请按脚本需求安装`requests`、`fastapi`、`uvicorn`、`pytest`等）。
- 启动接口：`uvicorn case.api:app --host 127.0.0.1 --port 4567`，用于接收`/third_party_payment`请求并触发商品校验流程。
- 运行用例：`pytest case`，默认执行`test_*.py`；可通过`pytest case/test_query_goods.py -k goods -vv`聚焦单用例。

## 编码风格与命名约定
- 采用PEP 8，4空格缩进；文件与函数使用蛇形命名，类使用帕斯卡命名。
- HTTP调用保持幂等与明确超时，复用请求头或公共参数时请抽取到`util/`或fixture以减少重复（DRY）。
- 单一职责：拆分登录、数据拉取、断言逻辑，便于覆盖更多项目/页面（SOLID）。

## 测试指引
- 使用pytest，函数命名`test_*`；断言状态码和关键字段（如`payment`），必要时校验返回列表完整性。
- 对外部网络依赖可增加`--maxfail=1`或标记跳过，最好提供mock以避免非确定性失败。
- 生成报告可结合`pytest --junitxml=report/result.xml`或集成自定义报告目录（与README框架描述保持一致）。

## 提交与拉取请求规范
- 若初始化Git，推荐简洁英文前缀：`feat:`、`fix:`、`chore:`、`test:`，一提交一主题，描述具体变更对象。
- PR需说明：变更摘要、验证方式（命令或截图）、影响范围、未解决项；接口或配置变更需同步更新示例与README。

## 安全与配置提示
- 禁止提交密钥、token或真实账号；使用环境变量或本地忽略文件管理。
- 外部请求尽量保持`verify=True`，如需关闭请限定测试环境并在代码中注明原因与风险。
- 依赖更新或证书调整前先在隔离环境验证，避免影响现有用例。
