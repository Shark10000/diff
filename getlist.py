from solvesquare import *

class diffeq(object):
    def __int__(self, equat):
        self.equation = equat

    def simple(self, equat):
        signs = []
        flag = 0
        if '=-' in equat:
            flag = 1
        for sign in equat: #создаю список из знаков, чтобы потом добавлять в список уравнения
            if sign == '-' or sign == '+' or sign == '=':
                signs.append(sign)
        equat = equat.replace('=', '-') #это чтобы не делать третий сплит
        ans = equat.split('-') #делим по минусам
        ans2 = []
        for i in ans:
            helper = i.split('+') #делим по плюсам
            for j in helper:
                ans2.append(j)
                if len(ans2) > 1 and signs and ans2[-2] == '-':
                    ans2[-1] = ans2[-2] + ans2[-1]
                if signs: #добавляем знаки между слогаемыми
                    ans2.append(signs[0])
                    if signs[0] == '=' and flag:
                        ans2.append(signs[1])
                    signs.pop(0)
        return square(ans2)

# equat = input()
# diffeq = diffeq()
# ans = diffeq.simple(equat)
# print(ans) #функция для решения характерестического уравнения + с учетом корней делаем ответ
