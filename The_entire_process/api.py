from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from typing import List

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
            #调用Three payment
            Test_Query_goods().test_login()
            Test_Query_goods().test_goods()
            processed_items.append(item)

    return {
        "status": "success",
        "received_data": item_list.items,
        "data": processed_items,
        "message": "数据已成功接收"
    }



#  http://127.0.0.1:56988/docs
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=56988)