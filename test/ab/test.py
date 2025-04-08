import json

# Python 字典转 JSON
python_dict = {"name": "Alice", "age": 25, "city": "Tokyo"}
json_data = json.dumps(python_dict, indent=4)  # 序列化为 JSON 字符串
print(json_data)