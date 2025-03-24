import copy

original_list = [1, 2, [3, 4]]
shallow_copy = original_list[:]           # Shallow copy
deep_copy = copy.deepcopy(original_list)  # Deep copy

print(original_list)     # Output: [1, 2, [3, 4]]
print(shallow_copy)      # Output: [1, 2, [3, 4]]
print(deep_copy)         # Output: [1, 2, [3, 4]]

shallow_copy[2][0] = 10  # Thay đổi shallow copy
print(original_list)     # Output: [1, 2, [10, 4]]  # Thay đổi
print(shallow_copy)      # Output: [1, 2, [10, 4]]  # Thay đổi
print(deep_copy)         # Output: [1, 2, [3, 4]]   # Không thay đổi

deep_copy[2][0] = 20     # Thay đổi deep copy
print(original_list)     # Output: [1, 2, [10, 4]]  # Không thay đổi
print(shallow_copy)      # Output: [1, 2, [10, 4]]  # Không thay đổi
print(deep_copy)         # Output: [1, 2, [20, 4]]  # Thay đổi