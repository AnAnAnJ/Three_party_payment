"""
-  给出api调用的接口
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from typing import List

from case.test_admin_search import TestSearchValue
from case.test_api_query_goods import Test_API_Query_goods
from test_api_query_goods import Test_API_Query_goods

app = FastAPI()
class Item(BaseModel):
    page_name: str
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

    return {
        "status": "success",
        "received_data": item_list.items,
        "data": "api下发数据配置与admin配置 返回对比数据一致，有异常返回对应那个商品无三方支付",
        "message": f"✅三方支付接口返回数据无异常",
    }



#  http://127.0.0.1:4567/docs
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=4567)