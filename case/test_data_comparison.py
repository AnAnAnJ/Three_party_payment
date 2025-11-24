"""
 - 对比api查询出来的三方支付商品信息与admin配置是否一致
    test_admin_goods  -- > test_api_goods
    成功  - 全部信息匹配
    异常  - 部分信息匹配
    失败  - 全部不匹配
"""
from case.test_admin_search import TestSearchValue
from case.test_api_query_goods import Test_API_Query_goods


class Test_Data_Comparison():

    def test_data_comparison(self):
        admin_goods_res = TestSearchValue().test_admin_goods()
        api_goods_res = Test_API_Query_goods().test_api_goods()

        if admin_goods_res == api_goods_res:
            print("✅api查询三方支付商品信息与admin配置一致")
        elif admin_goods_res != api_goods_res:
            print("⚠️api查询三方支付商品信息与admin配置不一致")
        else:
            print("❌api查询三方支付商品信息与admin配置不一致")

