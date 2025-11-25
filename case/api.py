from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from util.test_admin_search import TestSearchValue
from util.test_api_query_goods import TestApiQueryGoods
from util.test_data_comparison import TestDataComparison

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
        # 将bundle_id设置为TestSearchValue的类属性，这样其他地方调用时不需要传递参数
        TestSearchValue.bundle_id = bundle_id
        # return bundle_id

        try:
            # 为每个 bundle_id 执行三个测试函数
            TestSearchValue().test_admin_search()
            print("TestSearchValue")

            TestApiQueryGoods().test_login()
            TestApiQueryGoods().test_api_goods()
            print("TestApiQueryGoods")

            comparison_result = TestDataComparison().test_data_comparison()
            print("TestDataComparison")

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
    return {
        "total_processed": len(results),
        "successful_processes": success_count,
        "results": results
    }


#http://127.0.0.1:4567/docs#
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=4567)