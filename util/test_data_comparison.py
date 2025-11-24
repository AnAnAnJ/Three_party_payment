"""
 - 对比api查询出来的三方支付商品信息与admin配置是否一致
    test_admin_goods  -- > test_api_goods
    成功  - 全部信息匹配
    异常  - 部分信息匹配
    失败  - 全部不匹配
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from util.test_admin_search import TestSearchValue
from util.test_api_query_goods import Test_API_Query_goods
import json


class Test_Data_Comparison():

    def test_data_comparison(self):
        #admin后台配置数据
        admin_goods_res = TestSearchValue().test_admin_goods()
        #api下发数据
        api_goods_res = Test_API_Query_goods().test_api_goods()

        admin_json = json.loads(admin_goods_res)
        api_json = json.loads(api_goods_res)

        # 获取两个字典的所有键的并集
        all_keys = set(admin_json.keys()) | set(api_json.keys())

        # 用于跟踪是否有不一致的数据
        has_inconsistencies = False

        # 遍历所有键进行比较
        for key in all_keys:
            # 检查键是否在admin_json中存在
            if key not in admin_json:
                return (f"【商品数据不一致】admin 中缺少 key: {key}")
                has_inconsistencies = True
                continue
            # 检查键是否在api_json中存在
            if key not in api_json:
                return (f"【商品数据不一致】api 中缺少 key: {key}")
                has_inconsistencies = True
                continue

            # 比较两个数组内容是否相等
            # if admin_json[key] != api_json[key]:
            #     return (f"【商品数据不一致】key: {key}")
            #     return (" 【admin】数据：", admin_json[key])
            #     return ("【api】数据：", api_json[key])
            #     has_inconsistencies = True

            # 检查是否存有原声支付
            for item in admin_json[key] + api_json[key]:
                if item.get('platform') == 'revenuecat':
                    return (f"⚠️当前商品 {key} 包含原生支付 (revenuecat)")
                    has_inconsistencies = True

        # 增强验证 - 不取交集检查所有字段
        print("\n===有缺失的数据===")
        for key in all_keys:
            # 获取每个键对应的支付方式列表，默认为空列表
            a_items = admin_json.get(key, [])
            b_items = api_json.get(key, [])

            # 创建字典以便于比较，使用支付方式名称作为键
            a_dict = {item['name']: item for item in a_items}
            b_dict = {item['name']: item for item in b_items}

            # 检查在admin中存在但在api中不存在的支付方式
            for name, item in a_dict.items():
                if name not in b_dict:
                    return (f"商品： {key}: 【api】中缺少支付方式 '{name}'")
                    has_inconsistencies = True

            # 检查在api中存在,但在admin中不存在的支付方式
            for name, item in b_dict.items():
                if name not in a_dict:
                    return (f"商品： {key}: 【admin】中缺少支付方式 '{name}'")
                    has_inconsistencies = True

            # 检查相同支付方式名称但平台不同的情况
            common_names = set(a_dict.keys()) & set(b_dict.keys())
            for name in common_names:
                if a_dict[name]['platform'] != b_dict[name]['platform']:
                    return (
                        f"商品： {key}: 支付方式 '{name}' platform不一致, 【admin】数据为: = {a_dict[name]['platform']}, 【api】数据为: = {b_dict[name]['platform']}")
                    has_inconsistencies = True

        # 如果没有发现任何不一致，则输出数据一致无异常
        if not has_inconsistencies:
            return ("\n✅三方支付数据无异常,api查询三方支付商品信息与admin配置一致")

