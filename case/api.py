"""
-  给出api调用的接口
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from util.test_admin_search import TestSearchValue
from util.test_api_query_goods import Test_API_Query_goods
from util.test_data_comparison import Test_Data_Comparison

app = FastAPI()
class Item(BaseModel):
    bundle_id: str

class ItemList(BaseModel):
    items: List[Item]

@app.post("/third_party_payment")
def create_items(item_list: ItemList):
    processed_items = []
    for item in item_list.items:
        if item.bundle_id == "com.Drift.cf.ios":
            TestSearchValue()
            Test_API_Query_goods()
            processed_items.append(item)

    if  Test_Data_Comparison().test_data_comparison() == "✅ 三方支付数据无异常, api返回数据与admin配置一致":
        return {
            "status": "success",
            "received_data": item_list.items,
            "message": f"✅三方支付接口返回数据无异常",
        }
    elif Test_Data_Comparison().test_data_comparison() != "✅ 三方支付数据无异常, api返回数据与admin配置一致":
        return {
            "status": "fail",
            "received_data": item_list.items,
            "data": Test_Data_Comparison().test_data_comparison(),
            "message": f"⚠️三方支付接口返回数据有异常"
        }
    else:
        return {
            "status": "fail",
            "received_data": item_list.items,
            "message": f"⚠️数据有异常"
        }


#  http://127.0.0.1:4567/docs
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=4567)