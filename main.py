first = input('Введите числo:')
second =input('Введите второе число:')
third = input('Введите третье число:' )
print(first,second,third)
if first == second == third:    # Если все числа равны между собой
    print(3)                  # Вывести 3
elif first == second or third == first or second == third:  #Условие (Или) какие-то два числа равны между собой
    print(2)    #Вывести 2
else:                         # (Иначе) если два условия выше не соблюдены
    print(0)           # Вывести 0
