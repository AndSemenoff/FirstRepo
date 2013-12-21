# -*- coding: utf-8 -*-
class Ipoteka:
    def __init__(self, summa, rate, period, period_flag = True):
        # Если период задан в годах, то флаг True
        self.summa = summa
        self.rate = rate
        self.period_flag = period_flag
        if self.period_flag:
            self.period = period * 12
        else:
            self.period = period
    @property        
    def month_rate(self):
        i = self.rate / 12 / 100
        return i
            
    @property
    def k_annuitet(self):
        n = self.period
        i = self.month_rate
        k = i*(1+i)**n/((1+i)**n-1)
        return k
    
    @property
    def payment(self):
        return round(self.k_annuitet * self.summa, 2)
    
    @property
    def overpayment(self):
        o = round(self.payment * self.period - self.summa, 2)
        return o