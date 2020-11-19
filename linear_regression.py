def col(matrix, i):
    return [row[i] for row in matrix]


def sqr(val):
    return val ** 2


def estimate(points):
    n = len(col(points, 1))

    sum_x_sqr = 0
    for point in points:
        sum_x_sqr += point[0] ** 2
    sum_x_sqr /= 3


    sum_xy = 0
    for point in points:
        sum_xy += point[0] * point[1]
    sum_xy /= 3

    sum_x = sum(col(points, 0)) / n
    sum_y = sum(col(points, 1)) / n

    num = sum_xy - sum_x * sum_y
    denom = sum_x_sqr - sum_x ** 2
    m = num / denom

    b = sum_y - m * sum_x    

    print(f'\nm: {m}\nb: {b}\n')


data1 = [[1, 2], [2, 1], [4, 3]]
data2 = [[-2, -3], [-1, -1], [1, 2], [4, 3]]

estimate(data1)
estimate(data2)
