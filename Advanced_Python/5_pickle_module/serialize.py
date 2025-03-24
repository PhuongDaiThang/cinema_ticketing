import pickle

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

person = Person("Alice", 25, "Ho Chi Minh City")

# Serialize dữ liệu thành binary
serialized_data = pickle.dumps(person)

# In chuỗi byte sau khi serialize
print("Serialized data (byte format):")
print(serialized_data)

# Ghi serialized data ra file
with open("5_pickle_module/person.pkl", "wb") as file:
    file.write(serialized_data)
    print("Serialized data has been written to '4_context manager/person.pkl'")
