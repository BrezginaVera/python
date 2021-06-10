income = int (input("Ваша выручка: "))
costs = int (input("Ваши издержки: "))
if income > costs:
    print("У Вас прибыль")
else:
    print("У Вас убыток")
if income > costs:
    eff=(income-costs)/income
    print("Рентабельность выручки составляет:",eff)
    if income > costs:
        employe=int(input("Число сотрудников: "))
        print("Прибыль фирмы в расчете на одного сотрудника составляет:",eff/employe)
