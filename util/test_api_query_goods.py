"""
 - api层：
    - 登录
        - 区分项目和page_name
    - 查询商品信息
        viva
            - type=coin
        joymeet项目
            - type=member_subscribe
            - type=ticket_private_photo
            - type=ticket_private_video
"""
import json
import requests

from lib.get_yaml_data import get_yaml_datas_str, get_yaml_dict_value


class Test_API_Query_goods():


    # 登录
    def test_login(self,project,page_name):
        Z_User_Agent = f"Z-User-Agent: '{page_name}/1.2.0 iOS/18.6.2 (iPhone 14)'"
        if project == "viva":
            uri = f"/v1/auth?type=device_quick"
            try:
                res = requests.post(url= get_yaml_datas_str("func/url_config.yaml","url","Viva","staging") + uri,
                                    headers=get_yaml_dict_value("func/url_config.yaml", "Viva_headers", Z_User_Agent=Z_User_Agent),
                                    verify=False,
                                    timeout=40)
                assert res.status_code == 200
                if (res.headers.get('Z-Auth-Token')) != None:
                    viva_token = res.headers.get('Z-Auth-Token')
                    return viva_token
            except Exception as e:
                        print(f"Request failed: {e}")
                        raise
        elif project == "joymeet":
            #待确认joy meet项目登录方式
            print("joymeet项目")
        else:
            print("未查询到项目名称，请检查配置是否存在当前内容")


    #查询商品
    def test_api_goods(self,project,page_name):
        token = self.test_login(project,page_name)
        Z_User_Agent = f"Z-User-Agent: '{page_name}/1.2.0 iOS/18.6.2 (iPhone 14)'"
        if project == "viva":
            uri = f"/v1/trades/goods?type=coin"
            try:
                res = requests.get(url=get_yaml_datas_str("func/url_config.yaml","url","Viva","staging") + uri,
                                   headers={
                                                'Z-App-Info': 'bundle_id=com.swerlzenfigmaderlas.swerl;version=1.3.0;build=13',
                                                'Z-Auth-Token': token,
                                                'Z-Client-Id': '4886037297291990',
                                                'Z-Lon': '0',
                                                'Z-Lat': '0',
                                                'Z-Language': 'en-us',
                                                'Z-User-Agent': Z_User_Agent,
                                                'Z-Timezone': 'GMT-06:00',
                                                'Content-Type': 'application/json'},
                                    verify=False,
                                    timeout=40)
                assert res.status_code == 200
                data = res.json()
                return json.dumps(data, indent=2, ensure_ascii=False)
            except Exception as e:
                print(f"Request failed: {e}")
                raise
        elif project == "joymeet":
            print("joymeet项目")
        else:
            print("未查询到项目名称，请检查配置是否存在当前内容")


if __name__ == '__main__':
    Test_API_Query_goods().test_login("viva","Drift")
    Test_API_Query_goods().test_api_goods("viva","Drift")
