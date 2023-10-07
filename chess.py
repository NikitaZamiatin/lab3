k, l = map(int, input('Введите номер вертикали первого поля, а через пробел номер горизонтали (2 числа от 1 до 8 через пробел): ').split())
m, n = map(int, input('То же самое для второго поля: ').split())
if 1<=k<=8 and 1<=l<=8 and 1<=m<=8 and 1<=n<=8:
    if (k+l)%2 == (m+n)%2:
        print('Выбранные поля одного цвета')
    else:
        print('Выбранные поля разного цвета')
    chessman = input('Ферзь, ладья, слон или конь? (Введите слово с маленькой буквы): ')
    if chessman == 'ферзь':
        if k == m or l == n or abs(k-m)==abs(l-n):
            print('Ферзь, находящийся на первом поле угрожает второму полю и может попасть туда за один ход')
        else:
            print('Ферзь, находящийся на первом поле не угрожает второму полю')
            print('Но попасть туда можно, совершив ход на поле (',m,',',l,'), а после на поле (',m,',',n,')',sep='')
    if chessman == 'ладья':
        if k == m or l == n:
            print('Ладья, находящаяся на первом поле угрожает второму полю и может попасть туда за один ход')
        else:
            print('Ладья, находящаяся на первом поле не угрожает второму полю')
            print('Но попасть туда можно, совершив ход на поле (',m,',',l,'), а после на поле (',m,',',n,')',sep='')
    if chessman == 'слон':
        if abs(k-m)==abs(l-n):
            print('Слон, находящийся на первом поле угрожает второму полю и может попасть туда за один ход')
        else:
            print('Слон, находящийся на первом поле не угрожает второму полю')
            if (k+l)%2 != (m+n)%2:
                print('И никогда не будет угрожать')
            else:
                for i in range(1,8):
                        if 1<=m+i<=8 and 1<=n+i<=8 and abs(k-m-i)==abs(l-n-i):
                            a=m+i
                            b=n+i
                            print('Попасть туда можно, совершив ход на поле (',a,',',b,'), а после на поле (',m,',',n,')',sep='')
                            a=0
                            b=0
                        elif 1<=m+i<=8 and 1<=n-i<=8 and abs(k-m-i)==abs(l-n+i):
                            a=m+i
                            b=n-i
                            print('Попасть туда можно, совершив ход на поле (',a,',',b,'), а после на поле (',m,',',n,')',sep='')
                            a=0
                            b=0
                        elif 1<=m-i<=8 and 1<=n+i<=8 and abs(k-m+i)==abs(l-n-i):
                            a=m-i
                            b=n+i
                            print('Попасть туда можно, совершив ход на поле (',a,',',b,'), а после на поле (',m,',',n,')',sep='')
                            a=0
                            b=0
                        elif 1<=m-i<=8 and 1<=n-i<=8 and abs(k-m+i)==abs(l-n+i):
                            a=m-i
                            b=n+i
                            print('Попасть туда можно, совершив ход на поле (',a,',',b,'), а после на поле (',m,',',n,')',sep='')
                            a=0
                            b=0                                         
    if chessman == 'конь':
        if (abs(k-m)==1 and abs(l-n)==2) or (abs(k-m)==2 and abs(l-n)==1):
            print('Конь, находящийся на первом поле угрожает второму полю')
        else:
            print('Конь, находящийся на первом поле не угрожает второму полю')
else:
    print('Числа должны быть не меньше 1 и не больше 8')