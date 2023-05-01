triangle_width = int(input('Введить ширину трикутника '))
triangle_width += 1
symbol_ = '*'
space_ = ' '
print('Трикутник №1')
for i in range(1, triangle_width):
    print(symbol_ * (triangle_width - i))
print('Трикутник №2')
for i in range(1, triangle_width):
    print(symbol_ * i)
print('Трикутник №3')
for i in range(1, triangle_width):
    print(space_ * (i - 1) + symbol_ * (triangle_width - i))
print('Трикутник №4')
for i in range(1, triangle_width):
    print(space_ * (triangle_width - i - 1) + (symbol_ * i))
