lst = input('Введите числа')
lst = list(lst.split(','))
lst = [int(x) for x in lst]
lst.sort(reverse=True)
maximal = {'1': 0,'2': 0,'3': 0}
s = 0
p = 0
for i in range(2, len(lst)):
    if lst[-1] + lst[i] > lst[-2] and lst[-2] + lst[-1] > lst[i] and lst[-2] + lst[i] > lst[-1]:
        p = (lst[-2] + lst[-1] + lst[i]) / 2
        s = (p*(p-lst[-2])*(p-lst[-1])*(p-lst[i])) ** 0.5
        maximal['1'] = lst[-2]
        maximal['2'] = lst[-1]
        maximal['3'] = lst[i]
        break

if s > 0:
    print("Максимальная площадь - ", s)
    print("Стороны при максимальной площади - ", maximal)
else:
    print("К сожалению, операция не может быть выполнена :(")
