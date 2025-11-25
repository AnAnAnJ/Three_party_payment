import sys
import os

from util.test_api_query_goods import TestApiQueryGoods

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json

class TestDataComparison:

    admin_goods_res = """{
      "com.swerlzenfigmaderlas.swerl.gems.120_normal": [
        {
          "name": "Apple Pay",
          "platform": "onerway_apple_pay"
        }
      ]
    }"""
    api_goods_res = """{
      "com.swerlzenfigmaderlas.swerl.gems.120_normal": [
        {
          "name": "Apple Pay",
          "platform": "onerway_apple_pay"
        }
      ],"com.swerlzenfigmaderlas.swerl.gems.220_normal": [
        {
          "name": "Apple Pay",
          "platform": "onerway_apple_pay"
        }
      ]
    }"""

    # admin_goods_res = TestApiQueryGoods().test_admin_goods()
    # api_goods_res = TestApiQueryGoods().test_api_goods()


    def test_data_comparison(self):
        """
        对单个项目进行数据对比
            :param admin_data: 管理端配置数据
            :param api_data: API查询数据
            :return: 对比结果
        """
        admin_json = json.loads(self.admin_goods_res)
        api_json = json.loads(self.api_goods_res)

        messages = []
        admin_ids = set(admin_json.keys())
        api_ids = set(api_json.keys())

        missing_in_admin = api_ids - admin_ids
        missing_in_api = admin_ids - api_ids

        if missing_in_admin:
            messages.append(f"【当前商品 product_id为：admin当中无当前数据，api存在】: {sorted(missing_in_admin)}")
        if missing_in_api:
            messages.append(f"【当前商品 product_id为：api当中无当前数据，admin存在】: {sorted(missing_in_api)}")


        common_ids = admin_ids & api_ids
        for pid in sorted(common_ids):
            admin_items = admin_json.get(pid, [])
            api_items = api_json.get(pid, [])

            admin_map = {item.get("name"): item.get("platform") for item in admin_items}
            api_map = {item.get("name"): item.get("platform") for item in api_items}

            all_names = set(admin_map.keys()) | set(api_map.keys())

            for name in all_names:
                admin_plat = admin_map.get(name)
                api_plat = api_map.get(name)

                if admin_plat != api_plat:
                    messages.append(
                        f"【product_id ： {pid}】name == '{name}' platform 不一致: "
                        f"admin中为：'{admin_plat}' vs api数据为：'{api_plat}'"
                    )

                if admin_plat == "revenuecat" or api_plat == "revenuecat":
                    messages.append(
                        f"【product_id {pid}】包含 revenuecat（原生支付）, 不是三方支付商品"
                    )

        if not messages:
            result = "✅ 三方支付数据无异常, api返回数据与admin配置一致"
        else:
            result = "\n" + "\n".join(messages)

        print(result)
        return result