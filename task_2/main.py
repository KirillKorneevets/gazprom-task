import numpy as np


m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]

total_count, total_sum, average_value, all_in_one_tuple = len(arr:=np.array([num for s in m for num in s])), np.sum(arr), np.mean(arr), tuple(arr)

print(total_count)
print(total_sum)
print(average_value)
print(all_in_one_tuple)
