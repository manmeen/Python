# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 23:13:20 2016

@author: manmeensaini
"""
    
def Balance_func(balance, annualInterestRate, fixedMonthlyPayment):
    for m in range(1,13):    
        unpaidMonthly = balance - fixedMonthlyPayment
        balance = unpaidMonthly + ( (annualInterestRate / 12.0) * unpaidMonthly)
    return balance

def minFixedMonthly(balance, annualInterestRate):

  #  balance = 999999
    balance_Org = balance
   # annualInterestRate = 0.18
    monthlyInterestRate = annualInterestRate / 12.0
    lower = balance /12.0
    Upper = (balance * (1 + monthlyInterestRate)**12) / 12.0
    minPay = (lower+Upper)/2.0

    while (abs(balance) >= 0.01):   
        balance = balance_Org
        balance = Balance_func(balance, annualInterestRate, minPay)
        if (balance > 0):
            lower = minPay
        else:
            Upper = minPay
        minPay = (lower+Upper)/2.0
        
    return minPay

minPay1 = minFixedMonthly(3760, 0.1924)
print("Lowest monthly payment(chase): " + str(round(minPay1,2)))

minPay2 = minFixedMonthly(2500, 0.1614)
print("Lowest monthly payment(capitalone): " + str(round(minPay2,2)))

minPay3 = minFixedMonthly(3633, 0.1499)
print("Lowest monthly payment(Bofa): " + str(round(minPay3,2)))

minPay4 = minFixedMonthly(2584, 0.00)
print("Lowest monthly payment(Bofa2): " + str(round(minPay4,2)))

print("Total monthly lowest payments (all cc)): " + str(round(minPay1 + minPay2 + minPay3 +minPay4, 2)))



   
    
    



