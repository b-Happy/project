"""
Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
Далее запро сите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
"""
res = int(input("Введите выручку фирмы: "))
cost = int(input("Введите издержки фирмы: "))
prof = res - cost

if prof > 0:
    print(f'Финансовый результат - прибыль. Ее величина {prof}')
    print("Рентабельность выручки")
    ren = prof / res
    print(f'Рентабельность выручки: {ren}')

    staff = int(input("Введите численность сотрудников: "))
    cash = prof / staff
    print(f'Прибыль фирмы на одного сотрудника = {cash}')

elif prof < 0:
    print(f'Финансовый результат - убыток. Ее величина: {prof}')

else:
    print("Выручка равна издержкам")
