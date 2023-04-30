
triangle_width = int(input('Введить ширину трикутника '))
triangle_width += 1
print('Трикутник №1')
for i in range(1, triangle_width):
    print('*' * (triangle_width - i))
print('Трикутник №2')
for i in range(1, triangle_width):
    print('*' * i)
print('Трикутник №3')
for i in range(1, triangle_width):
    print(' ' * (i - 1) + '*' * (triangle_width - i))
print('Трикутник №4')
for i in range(1, triangle_width):
    print(' ' * (triangle_width - i - 1) + ('*' * i))
