from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from util.test_admin_search import TestSearchValue
from util.test_api_query_goods import TestApiQueryGoods
from util.test_data_comparison import TestDataComparison


class Logical_processing:

    def create_items():

        try:
            tance = TestSearchValue(bundle_id)
            TestSearchValue()
            test_instance.test_admin_search()
            print(f"TestSearchValue{test_instance}")

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
