#13.8.19
tickets_number = int(input("введите количество билетов "))
print("Введите возраст посетителей ")
ages = [int(input()) for i in range(tickets_number)]
summ = 0
for i in range(len(ages)):
    if 18 < ages[i]:
        summ += 0
    if 18 <= ages[i] < 25:
        summ += 990
    if ages[i] >= 25:
        summ += 1390

if tickets_number > 3:
    summ = summ * 0.9
    print("Скидка 10%. Итого: ", summ)
else:
    print("Без скидки. Итого: ", summ)





