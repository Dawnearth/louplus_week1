#!/usr/bin/env python3
# -*- conding: utf-8 -*-

import sys
import csv
import os
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

class Args(object):
    """docstring for Args"""
    def __init__(self):
        self.args = sys.argv[1:]
    def _value_after_option(self,option):
        try:
            index = self.args.index(option)
            return self.args[index + 1]
        except(ValueError,IndexError):
            print("Parameter Error")
            os.exit()
    @property
    def config_path(self):
        return self._value_after_option('-c')

    @property
    def userdata_path(self):
        return self._value_after_option('-d')

    @property
    def export_path(self):
        return self._value_after_option('-o')
args = Args()

class Config(object):
    """docstring for Config"""
    def __init__(self):
        self.config = self._read_config()

    def _read_config(self):
        config_path = args.config_path
        config = {}
        with open (config_path) as path:
            for line in path.readlines():
                key,value = line.strip().split('=')
                try:
                    config[key]  = float(value)
                except ValueError:
                    print("Parameter Error")
                    os.exit()
        return config
    
    def _get_config(self,key):
        try:
            return self.config[key]
        except KeyError:
            print('Config Error')
            os.exit()  
    @property 
    def social_insurance_baseline_low(self):
        return self._get_config('JiShuL')
    @property
    def socail_insurance_baseline_high(self):
        return self._get_config('JiShuH')
    @property 
    def social_insurance_total_rate(self):
        return sum([
                self._get_config('YangLao'),
                self._get_config('YiLiao'),
                self._get_config('ShiYe'),
                self._get_config('GongShang'),
                self._get_config('ShengYu'),
                self._get_config('GongJiJin')
            ])

config = Config()

class UserData(object):
    """docstring for UserData"""
    def __init__(self):
        self.userdata = self._read_users_data()
    
    def _read_users_data(self):
        userdata_path = args.userdata_path 
        userdata = []
        with open(userdata_path) as user_money:
            for line in user_money.readlines():
                employee_id,income_string = line.strip().split(',')
                try:
                    income = int (income_string)
                except ValueError:
                    print("Parameter Error")
                    os.exit()
                userdata


def cncome_tax(income):
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
