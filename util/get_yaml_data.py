from pathlib import Path
from typing import Any, List

import yaml

CONFIG_PATH = Path(__file__).resolve().parent / "url_config.yaml"


def load_config(config_path: Path = CONFIG_PATH) -> Any:
    """加载并返回配置数据，避免重复读取文件。"""
    with config_path.open(encoding="utf-8") as file:
        return yaml.safe_load(file) or []


def _pick_from_list(items: List[Any], key: str) -> Any:
    """在列表中的字典里查找匹配字段。"""
    for item in items:
        if isinstance(item, dict) and key in item:
            return item[key]
    raise KeyError(key)


def get_config_value(
    *keys: str,
    default: Any = None,
    config_path: Path = CONFIG_PATH,
) -> Any:
    """
    通过可变路径提取任意字段数据。
    - 自动处理列表包裹的字典结构（当前yaml的顶层即为列表）。
    - 未找到时返回default，未提供default则抛出KeyError，方便调用层自行决策。
    """
    data = load_config(config_path)
    if not keys:
        return data

    try:
        value: Any = data
        for key in keys:
            if isinstance(value, list):
                value = _pick_from_list(value, key)
            elif isinstance(value, dict):
                value = value[key]
            else:
                raise KeyError(key)
        return value
    except KeyError:
        if default is not None:
            return default
        raise


def get_first_value(*keys: str, default: Any = None, config_path: Path = CONFIG_PATH) -> Any:
    """
    在get_config_value基础上，若结果为列表则返回首个元素，方便获取url单值字段。
    """
    value = get_config_value(*keys, default=default, config_path=config_path)
    if isinstance(value, list):
        return value[0] if value else default
    return value
