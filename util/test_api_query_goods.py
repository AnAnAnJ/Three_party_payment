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

from lib.get_yaml_data import get_yaml_datas


class Test_API_Query_goods():

    page_name = "Drift"
    Project = "viva"
    viva_host_url = "https://staging-api.vivaaaa.com"


    # 登录
    def test_login(self):
        if self.Project == "viva":
            uri = f"/v1/auth?type=device_quick"
            try:
                res = requests.post(url= get_yaml_datas(f"/url_config.yaml", "url_config", "viva","staging") + uri,
                                    headers={
                                                'Z-App-Info': 'bundle_id=com.swerlzenfigmaderlas.swerl;version=1.3.0;build=13',
                                                'Z-Client-Id': '4886037297291990',
                                                'Z-Lon': '0',
                                                'Z-Lat': '0',
                                                'Z-Language': 'en-us',
                                                'Z-User-Agent': f'{self.page_name}/1.2.0 iOS/18.6.2 (iPhone 14)',
                                                'Z-Timezone': 'GMT-06:00',
                                                'Content-Type': 'application/json'
                                            },
                                    verify=False,
                                    timeout=40)
                assert res.status_code == 200
                if (res.headers.get('Z-Auth-Token')) != None:
                    viva_token = res.headers.get('Z-Auth-Token')
                    return viva_token
            except Exception as e:
                        print(f"Request failed: {e}")
                        raise
        elif self.Project == "joymeet":
            #待确认joy meet项目登录方式
            print("joymeet项目")
        else:
            print("未查询到项目名称，请检查配置是否存在当前内容")


    #查询商品
    def test_api_goods(self):
        if self.Project == "viva":
            uri = f"/v1/trades/goods?type=coin"
            try:
                res = requests.get(url=self.viva_host_url + uri,
                                   headers={
                                                'Z-App-Info': 'bundle_id=com.swerlzenfigmaderlas.swerl;version=1.3.0;build=13',
                                                'Z-Auth-Token': self.test_login(),
                                                'Z-Client-Id': '4886037297291990',
                                                'Z-Lon': '0',
                                                'Z-Lat': '0',
                                                'Z-Language': 'en-us',
                                                'Z-User-Agent': f'{self.page_name}/1.2.0 iOS/18.6.2 (iPhone 14)',
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
        elif self.Project == "joymeet":
            print("joymeet项目")
        else:
            print("未查询到项目名称，请检查配置是否存在当前内容")


if __name__ == '__main__':
    Test_API_Query_goods().test_login()
    # Test_Query_goods().test_api_goods()

