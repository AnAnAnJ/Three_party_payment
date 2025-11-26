from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from util.test_admin_search import TestSearchValue
from util.test_api_query_goods import TestApiQueryGoods
from util.test_data_comparison import TestDataComparison

import logging

app = FastAPI()
class Item(BaseModel):
    bundle_id: str

class ItemList(BaseModel):
    items: List[Item]

@app.post("/third_party_payment")
def create_items(item_list: ItemList):

    results = []

    # 遍历所有传入的项目
    for item in item_list.items:
        # 提取 bundle_id 值
        bundle_id = item.bundle_id
        # return bundle_id

        try:

            # 1. 获取项目信息
            search = TestSearchValue(bundle_id)
            project, _, page_name = search.test_admin_search()
            print(f"TestSearchValue: project={project}, page_name={page_name}")

            if project == "unknown_project":
                raise Exception(f"Bundle ID {bundle_id} not found in configuration")

            # 2. 查询API商品数据
            api_goods = TestApiQueryGoods(project, bundle_id, page_name)
            # test_api_goods内部会自动调用test_login获取token
            api_data = api_goods.test_api_goods()
            print(f"TestApiQueryGoods: Data retrieved{api_goods},{api_data}")

            # 3. 数据比对
            # 目前admin数据使用TestDataComparison默认值，后续可扩展传入admin_data
            comparison = TestDataComparison()
            comparison_result = comparison.test_data_comparison(api_data=api_data)
            print(f"TestDataComparison: {comparison_result}")

            # 存储处理结果bundle_id
            results.append({
                "bundle_id": bundle_id,
                "status": "success" if comparison_result == "✅ 三方支付数据无异常, api返回数据与admin配置一致" else "fail",

                "data_comparison_result": comparison_result
            })

        except Exception as e:
            # 处理异常情况
            results.append({
                "bundle_id": bundle_id,
                "status": "error",
                "error_message": str(e)
            })

    # 返回总体处理结果
    success_count = sum(1 for r in results if r["status"] == "success")
    logging.info(f"Processed {len(results)} items, {success_count} succeeded.")
    return {
        "total_processed": len(results),
        "successful_processes": success_count,
        "results": results
    }


#http://127.0.0.1:4567/docs#
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=4567)