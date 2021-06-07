"""Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""

import json
import numpy
my_file = open("for Task5-7.txt", "r")
profit = {}
full_profit = []
total_data = []

for line in my_file:
    name, firm, earning, damage = line.split()
    profit[name] = int(earning) - int(damage)
    if profit.setdefault(name) > 0:
        full_profit.append(profit.setdefault(name))
    average_profit = numpy.mean(full_profit)

profit_average = {"average_profit": average_profit}
total_data.append(profit)
total_data.append(profit_average)

with open("for Task5-7.json", "w") as json_file:
    json.dump(total_data, json_file)

json_str = json.dumps(total_data)
