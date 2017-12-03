pin = 325489

x = 4
x_l = 3
count = 1
while x < pin:
    x_ll = x_l + 8
    x += x_ll
    x_l = x_ll
    count += 1
    print(x, count)
size = 285
middle = (size // 2) + 1
width = 1
matrix = [[-1 for x in range(size)] for y in range(size)]
x = middle
y = middle
matrix[x][y] = 1
while matrix[x][y] < pin:
    while x < (middle + width):
        x += 1
        sum1 = 0
        for x1 in range(x - 1, x + 2):
            for y1 in range(y - 1, y + 2):
                if matrix[x1][y1] != -1:
                    sum1 += matrix[x1][y1]
        matrix[x][y] = sum1
        print(matrix[x][y])
    while y < (middle + width):
        y += 1
        sum1 = 0
        for x1 in range(x - 1, x + 2):
            for y1 in range(y - 1, y + 2):
                if matrix[x1][y1] != -1:
                    sum1 += matrix[x1][y1]
        matrix[x][y] = sum1
        print(matrix[x][y])
    while x > (middle - width):
        x -= 1
        sum1 = 0
        for x1 in range(x - 1, x + 2):
            for y1 in range(y - 1, y + 2):
                if matrix[x1][y1] != -1:
                    sum1 += matrix[x1][y1]
        matrix[x][y] = sum1
        print(matrix[x][y])
    while y > (middle - width):
        y -= 1
        sum1 = 0
        for x1 in range(x - 1, x + 2):
            for y1 in range(y - 1, y + 2):
                if matrix[x1][y1] != -1:
                    sum1 += matrix[x1][y1]
        matrix[x][y] = sum1
        print(matrix[x][y])
    width += 1
print(width)
