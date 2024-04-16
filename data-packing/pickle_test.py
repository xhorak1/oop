import pickle
from car import Car

numbers = [1, 2, 3, 4, 5]
c = Car ("audi", "black")

print("První auto:", c)

serialized_data = pickle.dumps(c)
print(f"Serialized data: \n{serialized_data}\n")
deserialized_data = pickle.loads(serialized_data)
print(f"Deserialized data: \n{deserialized_data}\n")
