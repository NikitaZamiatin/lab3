k, l = map(int, input('Введите номер первого поля по вертикали, а через пробел номер по горизонтали: ').split())
m, n = map(int, input('То же самое для второго поля: ').split())
if (k+l)%2 == (m+n)%2:
    print('Выбранные поля одного цвета')
else:
    print('Выбранные поля разного цвета')
chessman = input('Ферзь, ладья, слон или конь? (Введите слово с маленькой буквы): ').split()
if chessman == 'ферзь':
    if k == m or l == n or abs(k-m)==abs(l-n):
        print('Ферзь, находящийся на первом поле угрожает второму полю')
    else:
        print('Ферзь, находящийся на первом поле не угрожает второму полю')
if chessman == 'ладья':
    if k == m or l == n:
        print('Ладья, находящаяся на первом поле угрожает второму полю')
    else:
        print('Ладья, находящаяся на первом поле не угрожает второму полю')
if chessman == 'слон':
    if abs(k-m)==abs(l-n):
        print('Слон, находящийся на первом поле угрожает второму полю')
    else:
        print('Слон, находящийся на первом поле не угрожает второму полю')
if chessman == 'конь':
    if (abs(k-m)==1 and abs(l-n)==2) or (abs(k-m)==2 and abs(l-n)==1):
         print('Конь, находящийся на первом поле угрожает второму полю')
    else:
        print('Конь, находящийся на первом поле не угрожает второму полю')