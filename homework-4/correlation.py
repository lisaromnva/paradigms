from statistics import mean
from math import sqrt

array_1 = [1, 2, 3, 4, 5]
array_2 = [2, 3, 4, 5, 6]

avg_1 = mean(array_1)
avg_2 = mean(array_2)

array_x_avg_1 = list(map(lambda x: x - avg_1, array_1))
array_x_avg_2 = list(map(lambda x: x - avg_2, array_2))

res_top = sum(list(map(lambda x, y: x * y, array_x_avg_1, array_x_avg_2)))

array_1_pow = sum(list(map(lambda x: x * x, array_x_avg_1)))
array_2_pow = sum(list(map(lambda x: x * x, array_x_avg_2)))

res_bottom = sqrt(array_1_pow * array_2_pow)

res = res_top / res_bottom
print(res)