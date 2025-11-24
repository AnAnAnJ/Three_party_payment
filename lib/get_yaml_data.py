import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import yaml
import pathlib

def read_data_file(filename):
    with open(filename, 'r',encoding="utf-8") as file:
        print(f'执行读取文件信息，文件地址为：{filename}')
        return [line.strip() for line in file.readlines()]

def read_yaml_file(filename):
    yaml_file = yaml.safe_load(open(filename,encoding="utf-8"))
    print(f'执行读取文件信息，文件地址为：{filename}')
    return yaml_file


def get_yaml_datas(filename, data, group, case):
    # 获取当前脚本所在目录
    root_path = pathlib.Path(__file__).parent.absolute()
    # 正确构建目标文件路径
    yaml_path = (root_path / '..' / filename).resolve()
    # if not yaml_path.exists():
    #     raise FileNotFoundError(f"YAML file not found at: {yaml_path}")
    yaml_data = read_yaml_file(str(yaml_path))
    values = yaml_data.get(data).get(group).get(case)
    print(values)
    return values


if __name__ == '__main__':
    # Example usage
    print(get_yaml_datas("./func/url_config.yaml", "url_config", "Viva", "staging"))
