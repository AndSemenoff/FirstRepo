# -*- coding: utf-8 -*- 
# Рассчет аннуитетных платежей
import ipoteka
years = [ 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5]                                            # Количество лет 
annual_interest_rate = [12.25, 12.00, 11.75, 11.50, 11.25, 11.0, 12.25, 12.00, 11.75, 11.50, 11.25, 11.0, 12.25, 12.00, 11.75, 11.50, 11.25, 11.0]           # Проценты годовых
summa_kredita = [2000000] * len(years)                                    # Сумма кредита

ipo = []

count = 0
while count < len(years):
    ipo.append(ipoteka.Ipoteka(summa_kredita[count], annual_interest_rate[count], years[count], True))
    count += 1


out_str = ""
out_str +='<!DOCTYPE html><html><head><meta charset="utf-8"/><link rel="stylesheet" href="http://spbn.info/info/work/table.css"></head><body>'
out_str += '<table><tr><th>№</th><th>Кредит</th><th>Лет</th><th>Ставка</th><th>Платеж</th><th>Переплата</th>'
count = 0
while count < len(years):
    out_str += "<tr><td>" + str(count + 1) + "</td><td>" + str(ipo[count].summa) + "</td>" + \
        "<td>" + str(years[count]) + "</td><td>" + str(ipo[count].rate) + "</td>" + \
        "<td>" + str(round(ipo[count].payment, 0)) + "</td><td>" + str(round(ipo[count].overpayment, 0)) + "</td></tr>"
    count += 1


out_str += "</table></body><html>"
HTML_OUT_main = open("main.html", "w", encoding = 'utf-8')

HTML_OUT_main.write(out_str)
HTML_OUT_main.close()