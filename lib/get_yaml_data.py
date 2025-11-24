import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import allure
import yaml


def read_data_file(filename):
    with open(filename, 'r',encoding="utf-8") as file:
        # print(f'执行读取文件信息，文件地址为：{filename}')
        return [line.strip() for line in file.readlines()]

def read_yaml_file(filename):
    yaml_file = yaml.safe_load(open(filename,encoding="utf-8"))
    # print(f'执行读取文件信息，文件地址为：{filename}')
    return yaml_file

#获取yaml文件的路径，并读取测试用例数据
def get_yaml_datas_str(filename,*args):
    #读取当前路径
    root_path = os.path.dirname(os.path.abspath(__file__))
    #读取yaml文件路径
    yaml_path = os.sep.join([root_path,'..',filename])
    yaml_data = read_yaml_file(yaml_path)
    data = yaml_data
    for key in args:
        if isinstance(data, dict):
            data = data.get(key)
        else:
            return None
        if data is None:
            return None
    return data

def get_yaml_dict_value(filename, *args, Z_User_Agent):
    # 读取当前路径
    root_path = os.path.dirname(os.path.abspath(__file__))
    # 读取yaml文件路径
    yaml_path = os.sep.join([root_path, '..', filename])
    yaml_data = read_yaml_file(yaml_path)
    data = yaml_data
    for key in args:
        if isinstance(data, dict):
            data = data.get(key)
        else:
            return None
        if data is None:
            return None
            
    # 遍历完成后，如果结果是字典且需要添加 User-Agent
    if isinstance(data, dict) and Z_User_Agent and ": " in Z_User_Agent:
        key, value = Z_User_Agent.split(": ", 1)
        data[key] = value.strip("'").strip('"')
        
    return data


if __name__ == '__main__':
    Z_User_Agent = f"Z-User-Agent: 'Drift/1.2.0 iOS/18.6.2 (iPhone 14)'"
    # print(get_yaml_datas_str("func/url_config.yaml", "url", "Viva", "staging"))
    print(get_yaml_dict_value("func/url_config.yaml", "Viva_headers", Z_User_Agent=Z_User_Agent))