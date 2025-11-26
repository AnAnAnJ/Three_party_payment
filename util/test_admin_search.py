

class TestSearchValue:
    def __init__(self, bundle_id=None):
        self.bundle_id = bundle_id

    #admin数据库连接添加好后维护数据
    def test_admin_search(self):
        bundle_id_list = ["com.Drift.cf.ios", "com.swerlzenfigmaderlas.swerl", "com.Drift111.cf.ios"]

        if self.bundle_id is None:
            print("未查询到bundle_id，请检查配置是否存在当前内容")
            return "unknown_project", "unknown_bundle", "unknown_page"

        bundle_ids = self.bundle_id if isinstance(self.bundle_id, list) else [self.bundle_id]

        for bundle_id in bundle_ids:
            if bundle_id in bundle_id_list:
                project = "viva"
                page_name = "Swert"
                return project, bundle_id, page_name

        return "unknown_project", "unknown_bundle", "unknown_page"

    # def test_search_value(self):
    #     """
    #     1、查询joy happier数据库信息，根据bundle_id 查询 对应的项目名称（viva / joy meet） 和 包名
    #     :return:项目名称 / 包名
    #     """
    #     sql  = Test_Query_admin_data()
    #     #待维护对应的项目名称 / 包名 sql  https://admin.joyhappier.com/app_package
    #     res = sql.read_mysql("admin",f"待维护{self.bundle_id}")
    #     return res  #返回bundle_id /项目名称 / 包名
    #
    #
    # def test_admin_goods(self):
    #     """
    #     1、根据项目区分查询api
    #         - 项目等于 viva 查询数据库库为 ： XXXX
    #             - 根据项目昵称获取对应项目的商品信息及所有的支付方式
    #         - 项目等于 joy meet 查询数据库库为 ： XXXX
    #             - 根据项目昵称获取对应项目的商品信息及所有的支付方式
    #     :return: 商品id 对应的支付名称及平台信息
    #     """
    #     try:
    #         if project == "viva":
    #             sql  = Test_Query_admin_data()
    #             res = sql.read_mysql(f"待维护{ self.page_name}")
    #             return res
    #
    #         elif project  == "joy meet":
    #             sql  = Test_Query_admin_data()
    #             res = sql.read_mysql(f"待维护{self.page_name}")
    #             return res
    #         else:
    #             print("未查询到项目名称，请检查配置是否存在当前内容")
    #
    #     except Exception as e:
    #         print(e)
