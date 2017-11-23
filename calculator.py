#!/usr/bin/env python3
# -*- conding: utf-8 -*-

import sys
from collections import namedtuple

TaxRateQuickDeductionItem = namedtuple(
    'TaxRateQuickDeductionItem',
    ['start_point','tax_rete','qucik_deduction']
)

TAX_RATE_START_POINT = 3500

TAX_QUICK_LOOKUP_TABLE = [
    TaxRateQuickDeductionItem(80000,0.45,13505),
    TaxRateQuickDeductionItem(55000,0.35,5505),
    TaxRateQuickDeductionItem(35000,0.3,2755),
    TaxRateQuickDeductionItem(9000,0.25,1005),
    TaxRateQuickDeductionItem(4500,0.2,555),
    TaxRateQuickDeductionItem(1500,0.1,105),
    TaxRateQuickDeductionItem(0,0.03,0)
]

def calc_income_tax(income):
    taxtable_part = income - TAX_RATE_START_POINT
    if taxtable_part <= 0:
        return '0.00'
    for item in TAX_QUICK_LOOKUP_TABLE:
        if taxtable_part  > item.start_point:
            tax = taxtable_part * item.tax_rete -item.qucik_deduction
            return '{:.2f}'.format(tax) 

def main():
    if len(sys.argv) != 2:
       print("paramter Error")
    try:
       income = int(sys.argv[1])
    except ValueError:
       print('parameter Error')
    print(calc_income_tax(income))

if __name__ == '__main__':
    main()
