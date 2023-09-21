import math
from functools import reduce

def pearson_correlation(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(map(lambda a, b: a * b, x, y))
    sum_x_sq = sum(map(lambda a: a * a, x))
    sum_y_sq = sum(map(lambda a: a * a, y))

    numerator = n * sum_xy - sum_x * sum_y
    denominator = math.sqrt((n * sum_x_sq - sum_x ** 2) * (n * sum_y_sq - sum_y ** 2))

    if denominator == 0:
        return 0
    else:
        return numerator / denominator

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
correlation = pearson_correlation(x, y)
print(f"Pearson correlation coefficient: {correlation}")