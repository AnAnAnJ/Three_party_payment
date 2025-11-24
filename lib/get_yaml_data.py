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

def get_yaml_dict_value(filename, *args, **kwargs):
    # 读取当前路径
    root_path = os.path.dirname(os.path.abspath(__file__))
    # 读取yaml文件路径
    yaml_path = os.sep.join([root_path, '..', filename])
    yaml_data = read_yaml_file(yaml_path)
    data = yaml_data
    # 遍历 args，区分路径参数和需要添加的数据
    # 假设 args 中前面的参数是路径，直到遇到不在 yaml 中的 key，或者不再是 dict
    path_args = []
    update_args = []
    
    temp_data = data
    for i, key in enumerate(args):
        if isinstance(temp_data, dict) and key in temp_data:
            temp_data = temp_data[key]
            path_args.append(key)
        else:
            # 遇到第一个不是路径的参数，剩下的都是要添加的数据
            update_args = args[i:]
            break
            
    # 根据路径获取数据
    for key in path_args:
        data = data.get(key)
        
    if data is None:
        return None

    # 将剩余的 args 添加到字典中
    if isinstance(data, dict):
        for item in update_args:
            if isinstance(item, str) and ": " in item:
                k, v = item.split(": ", 1)
                data[k] = v.strip("'").strip('"')
            # 如果不是 Key: Value 格式，可以根据需求处理，这里暂时忽略或打印日志
            
    # 将 kwargs 中的内容添加到字典中
    if isinstance(data, dict):
        for k, v in kwargs.items():
            if isinstance(v, str) and ": " in v:
                key, value = v.split(": ", 1)
                data[key] = value.strip("'").strip('"')
            else:
                # 将 key 中的下划线替换为中划线，例如 Z_Auth_Token -> Z-Auth-Token
                data[k.replace('_', '-')] = v

    return data


if __name__ == '__main__':
    Z_User_Agent = f"Z-User-Agent: 'Drift/1.2.0 iOS/18.6.2 (iPhone 14)'"
    Z_App_Info = f'bundle_id=com.swerlzenfigmaderlas.swerl;version=1.3.0;build=13'
    Z_Auth_Token = "123456"

    print(get_yaml_dict_value("func/url_config.yaml", "Viva_headers", Z_User_Agent, Z_Auth_Token=Z_Auth_Token))










    

