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

    project = "viva"
    page_name = "Swert"
    bundle_id = "com.swerlzenfigmaderlas.swerl"
    Z_App_Info = f'bundle_id={bundle_id};version=1.3.0;build=13'
    Z_User_Agent = f"Z-User-Agent: '{page_name}/1.2.0 iOS/18.6.2 (iPhone 14)'"

    # 登录
    def test_login(self):
        if self.project == "viva":
            uri = f"/v1/auth?type=device_quick"
            try:
                res = requests.post(url= get_yaml_datas_str("func/url_config.yaml","url","Viva","staging") + uri,
                                    headers=get_yaml_dict_value("func/url_config.yaml", "Viva_headers",
                                                                Z_User_Agent=self.Z_User_Agent, Z_App_Info=self.Z_App_Info),
                                    verify=False,
                                    timeout=40)
                assert res.status_code == 200
                if (res.headers.get('Z-Auth-Token')) != None:
                    viva_token = res.headers.get('Z-Auth-Token')
                    return viva_token
            except Exception as e:
                        print(f"Request failed: {e}")
                        raise
        elif self.project == "joymeet":
            #待确认joy meet项目登录方式
            print("joymeet项目")
        else:
            print("未查询到项目名称，请检查配置是否存在当前内容")


    #查询商品
    def test_api_goods(self):
        if self.project == "viva":
            uri = f"/v1/trades/goods?type=coin"
            try:
                res = requests.get(url=get_yaml_datas_str("func/url_config.yaml","url","Viva","staging") + uri,
                                   headers=get_yaml_dict_value("func/url_config.yaml", "Viva_headers",
                                                               Z_Auth_Token=self.test_login(),Z_App_Info=self.Z_App_Info,Z_User_Agent=self.Z_User_Agent),
                                    verify=False,
                                    timeout=40)
                assert res.status_code == 200
                data = res.json()
                result = {}
                for item in data["data"]:
                    product_id = item.get("product_id")
                    payments = item.get("payment", [])

                    result[product_id] = [
                        {
                            "name": p.get("name"),
                            "platform": p.get("platform")
                        }
                        for p in payments
                    ]
                return json.dumps(result, indent=2, ensure_ascii=False)
            except Exception as e:
                print(f"Request failed: {e}")
                raise
        elif self.project == "joymeet":
            # 待确认joy meet项目登录方式 获取token信息后维护当前数据
            print("joymeet项目")
        else:
            print("未查询到项目名称，请检查配置是否存在当前内容")


if __name__ == '__main__':
    Test_API_Query_goods().test_login()
    Test_API_Query_goods().test_api_goods()
