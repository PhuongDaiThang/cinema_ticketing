import json

# Tạo một đối tượng Python
data = {
  "name": "Alice",
  "age": 30,
  "city": "Hanoi",
  "hobbies": ["reading", "music", "travel"]
}

# Mã hóa đối tượng thành chuỗi JSON
print(type(data))  # Output: <class 'dict'>

json_str = json.dumps(data)
print(type(json_str))  # Output: <class 'str'>

# Ghi JSON ra file
with open("6_json_module/save.json", "w") as f:
  json.dump(data, f, indent=2)

# In chuỗi JSON ra màn hình
print(json_str)  # Output: {"name": "Alice", "age": 30, "city": "Hanoi", "hobbies": ["reading", "music", "travel"]}
