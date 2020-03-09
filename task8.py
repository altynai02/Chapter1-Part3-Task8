# 8. Напишите функцию где дан список целых чисел.
# Заменить отрицательные на -1, положительные - на число
# 1, ноль оставить без изменений.

def plus_minus(list_):
    new_list = []
    for i in list_:
        if i > 0:
            i = 1
            new_list.append(i)
        elif i < 0:
            i = -1
            new_list.append(i)
        else:
            i = 0
            new_list.append(i)
    return list_, new_list

print(plus_minus([2,3,4, 0 , -2,-33, 5, -100]))