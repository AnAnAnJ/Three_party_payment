

# service/compute.py

def calculate_sum(a: int, b: int):
    result = a + b
    return {
        "a": a,
        "b": b,
        "sum": result
    }
# main.py
from fastapi import FastAPI
from service.compute import calculate_sum

app = FastAPI()

@app.get("/add")
def add_numbers(a: int, b: int):
    data = calculate_sum(a, b)
    return {
        "code": 0,
        "message": "success",
        "data": data
    }