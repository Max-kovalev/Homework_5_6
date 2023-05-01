program_repeat = 'y'
while program_repeat == 'y':
    print('Програма знаходить усі числа кратні 3 в діапазоні від 1 до N де N - ціле число')
    n = int(input('Введить число N '))
    multiple_of = 3
    while n > 1:
        if n % multiple_of == 0:
            print(n, end=' ')
        n -= 1
    print('\nПрограма знаходить сумму усіх чисел кратніх 3 в діапазоні від 1 до N де N - ціле число')
    n = int(input('Введить число N '))
    summ_multiple_of = 0
    while n > 1:
        if n % multiple_of == 0:
            if n == multiple_of:
                print(n, end=' = ')
            else:
                print(n, end=' + ')
        summ_multiple_of += n
        n -= 1
    print(summ_multiple_of)
    program_repeat = input('Бажаєте перезапустити програму? y/n ')
