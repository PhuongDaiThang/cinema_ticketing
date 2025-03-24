import json

# Giải mã chuỗi JSON thành đối tượng Python
with open("6_json_module/save.json", "rt") as f:
  data = json.loads(f.read())
  #or
  #data = json.load(f)

print(type(data))  # Output: <class 'dict'>

print(data)  # Output: {'name': 'Alice', 'age': 30, 'city': 'Hanoi', 'hobbies': ['reading', 'music', 'travel']}