import pickle

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

# Deseralize dữ liệu từ file
with open("5_pickle_module/person.pkl", "rb") as file:
    data = file.read()

deserialized_person = pickle.loads(data)
print(deserialized_person.name, deserialized_person.age, deserialized_person.city)