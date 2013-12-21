# -*- coding: utf-8 -*- 
# Рассчет аннуитетных платежей
number_days_in_year = 360               # Количество дней в году
years = 7                               # Количество лет 
annual_interest_rate = 12.00            # Проценты годовых
n = years * 12                          # Количество периодов
i = annual_interest_rate / 12 / 100     # Месячная ставка
summa_kredita = 5500000                 # Сумма кредита
start_date = "15.01.2014"               # Дата первого платежа
days_in_month = 30                      # Дней в конкретном месяце

k = i*(1+i)**n/((1+i)**n-1)
month_payment = round(k * summa_kredita, 2)
payment = [month_payment] * (n+1)
payment[0] = 0 
payment_sum = sum(payment)
rest = []
summa = []
procenty = []
procenty.append(0)
body = []
body.append(0)
summa.append(summa_kredita)
count = 1
while count <= len(payment):
    rest.append(round(payment_sum - month_payment * (count -1), 2))
    c_procenty = summa[count-1] * annual_interest_rate * days_in_month / (100 * number_days_in_year)
    procenty.append(round(c_procenty, 2))
    d = month_payment - c_procenty    # сумма в погашение тела
    body.append(round(d, 2))
    # сумма основного долга
    summa.append(round(summa[count-1] - d, 2))    
    count += 1
print(k)
print(month_payment)
print(payment)
print(payment_sum)

# Основной долг = summa
#procenty = summa * annual_interest_rate * days_in_month / (100 * number_days_in_year)
#d = month_payment - procenty    # сумма в погашение тела
# сумма основного долга
#summa -= d



HTML_OUT = open("result.html", "w", encoding = 'utf-8')
 
result_HTML_string = '<!DOCTYPE html><html><head><meta charset="utf-8"/><link rel="stylesheet" href="table.css"></head><body>'
result_HTML_string += '<p>Сумма кредита: ' + str(summa_kredita)
result_HTML_string += '<br/>Процентная ставка: ' + str(annual_interest_rate) 
result_HTML_string += '<br/>Месячная ставка: ' + str(i) 
result_HTML_string += '<br/>Количество лет: ' + str(years) 
result_HTML_string += '<br/>Количество периодов: ' + str(n) + '</p>'
result_HTML_string += '<br/>Месячный платеж: ' + str(month_payment) + '</p>'
result_HTML_string += '<table><tr><th>№</th><th>Дата</th><th>Платеж</th><th>Проценты пог</th><th>Тело пог</th><th>Тело остаток</th><th>Общий остаток</th>'
count = 0
for iterator in payment:
    result_HTML_string += "<tr><td>" + str(count) + "</td><td></td><td>" + str(iterator) + "</td><td>" + str(procenty[count]) + "</td><td>" +\
        str(body[count])+ "</td><td>" + str(summa[count]) + "</td><td>" +\
        str(rest[count-1]) + "</td></tr>"
    count += 1

import datetime
today = datetime.datetime.now()
result_HTML_string += "</table>"
result_HTML_string += "Всего выплачено: " + str(payment_sum)
result_HTML_string += "<p>Время создания:</p>" + str(today) + "</body><html>"
HTML_OUT.write(result_HTML_string)
HTML_OUT.close()