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
def get_yaml_datas(filename,*args):
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


if __name__ == '__main__':
    print(get_yaml_datas("func/url_config.yaml", "url", "Viva", "staging"))


