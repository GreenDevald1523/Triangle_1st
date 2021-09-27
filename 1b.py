lst = []
for i in range(50):
    lst.append(i+1)

lst.sort(reverse=True)
first = lst[0]
second = lst[1]
s = 0
p = 0
s_max = 0
maximal = []
for i in range(2, len(lst)):
    if second + lst[i] > first and first + second > lst[i] and first + lst[i] > second:
        p = (first + second + lst[i]) / 2
        s = (p*(p-first)*(p-second)*(p-lst[i])) ** 0.5
        maximal = [first, second, lst[i]]
        break

print("Максимальная площадь - ", s)
print("Стороны при максимальной площади - ", maximal)