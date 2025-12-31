from lib.sql import sql_def


class TestSearchValue:
    def __init__(self, bundle_id=None):
        self.bundle_id = bundle_id

    def test_search_value(self):
        """
        1、查询joy happier数据库信息，根据bundle_id 查询 对应的项目名称（viva / joy meet） 和 包名
        :return: 项目名称 / 包名 / bundle_id
        """
        search_value = sql_def(sql_query = f"SELECT app_project_name,bundle_id,name FROM `joymeet`.`app_package` WHERE `bundle_id`  LIKE '{self.bundle_id}';")
        if self.bundle_id is None:
            return f"未查询到bundle_id，请检查配置是否存在当前内容 : {self.bundle_id}"
        return search_value


    def test_admin_search(self):
        try:
            if self.test_search_value()[0] == "viva":
                #查询admin配置的项目商品信息
                admin_goods_res = list(sql_def(sql_query = f"SELECT product_id,name,platform from `viva`."
                                                           f"`goods_payment` WHERE `product_id` LIKE '%{self.test_search_value()[1]}%'"))
                print(admin_goods_res)
                return admin_goods_res
            elif self.test_search_value()[0]  == "joy meet":
                pass
            else:
                print("未查询到项目名称，请检查配置是否存在当前内容")

        except Exception as e:
            print(e)


