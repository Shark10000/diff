import math

def answers(lambda1, lambda2): #тут чисто из двух корней делаем ответ диффуру
    general_solution = ''
    if lambda1 == lambda2 and lambda1 != 0:
        general_solution = "C1" + "e" + "^" + "(" + str(lambda1) + "x" + ")" + ' + ' + "C2" + "x" + "e" + "^" + "(" + str(lambda1) + "x" + ")"
    elif lambda1 != lambda2 and lambda1 != 0 and lambda2 != 0:
        general_solution = "C1" + "e" + "^" + "(" + str(lambda1) + "x" + ")" + ' + ' + "C2" + "e" + "^" + "(" + str(lambda2) + "x" + ")"
    elif lambda1 == 0 and lambda2 == 0:
        general_solution = "C1" + ' + ' + 'C2' + 'x'
    elif lambda1 == 0:
        general_solution = 'C1' + ' + ' + "C2" + 'e^' + str(lambda2) + 'x'
    elif lambda2 == 0:
        general_solution = 'C1' + ' + ' + "C2" + 'e^' + str(lambda1) + 'x'
    return general_solution

def square(equals):
    a = 0
    b = 0
    c = 0
    flag0 = False
    flag1 = False
    flag2 = False
    middle = equals.index('=')
    position = 1
    for i in range(len(equals)): #достаем все коэффициенты для характерестического уравнения
        sign = equals[i]
        if "y''" in sign and "y''" == sign[-3:len(sign)]:
            if i > middle:
                position = -1
            if flag2 and len(sign) != 3:
                a += int((sign[:-3])) * position
            elif len(sign) != 3:
                a = int((sign[:-3])) * position
            else:
                a += 1
            flag2 = True
        if "y'" in sign and "y'" == sign[-2:len(sign)]:
            if i > middle:
                position = -1
            if flag1 and len(sign) != 2:
                b += int((sign[:-2])) * position
            elif len(sign) != 2:
                b = int((sign[:-2])) * position
            else:
                b += 1
            flag1 = True
        if "y" in sign and "y" == sign[-1]:
            if i > middle:
                position = -1
            if flag0 and len(sign) != 1:
                c += int((sign[:-1])) * position
            elif len(sign) != 1:
                c = int((sign[:-1])) * position
            else:
                c += 1
            flag0 = True
        position = 1
    lambda1 = (-b + math.sqrt(b * b - 4 * a * c)) * (0.5 * a ** -1) #считаем два дискреминанта
    lambda2 = (-b - math.sqrt(b * b - 4 * a * c)) * (0.5 * a ** -1)
    return answers(lambda1, lambda2)



