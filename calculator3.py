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

SOCIAL_INSURANCE_MONEY_RATE = {
    'endowment_insurance':0.08,
    'medical_insurance':0.02,
    'unemployment_insurance':0.005,
    'employment_injury_insurance':0,
    'maternity_insurance':0,
    'public_accumulation_funds':0.06
}

def calc_income_tax(income):
    total_rate = sum(SOCIAL_INSURANCE_MONEY_RATE.values())
    after_rate_money = income * (1 - total_rate )
    taxtable_part = after_rate_money - TAX_RATE_START_POINT
    if taxtable_part <= 0:
        return '{:.2f}'.format(after_rate_money)
    for item in TAX_QUICK_LOOKUP_TABLE:
        if taxtable_part  > item.start_point:
            tax = taxtable_part * item.tax_rete -item.qucik_deduction
            return '{:.2f}'.format(after_rate_money - tax)

def main():
    for item in sysy.argv[1:]:
        worker_id,income_money = item.split(':')
        try:
            income = int( income_money )
        except ValueError:
            print('Parameter Error')
        remain = calc_income_tax(income)
        print('{}:{}'.format(worker_id,remain))

if __name__ == '__main__':
    main()
