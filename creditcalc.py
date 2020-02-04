import math
import argparse


def de_parse(arg):
    return [arg.type_, arg.principal, arg.interest, arg.periods, arg.payment]


def n_of_month(credit_principal, monthly_payment, credit_interest):
    rate = credit_interest / (12 * 100)
    months = math.log((monthly_payment / (monthly_payment - rate * credit_principal)), 1 + rate)
    if months <= 12:
        print("You need 1 year to repay this credit!" if months > 11 else
              f"You need {math.ceil(months)} month to repay this credit!" if months == 1 else
              f"You need {math.ceil(months)} months to repay this credit!")
        print(f"Overpayment = {int(monthly_payment * months - credit_principal)}")
    else:
        years = int(months // 12)

        month = math.ceil(months % 12)
        if month == 12:
            years += 1
            month = 0

        print(f"You need {years} years and {month} months to repay this credit!" if years > 1 and month > 1 else
              f"You need {years} year and {month} months to repay this credit!" if month > 1 else
              f"You need {years} year and {month} month to repay this credit!" if month != 0 else
              f"You need {years} year to repay this credit!")
        print(f"Overpayment = {int(monthly_payment * math.ceil(months) - credit_principal)}")


def annuity_month(credit_principal, periods, credit_interest):
    rate = credit_interest / (12 * 100)
    annuity = credit_principal * ((rate * (pow((1 + rate), periods))) / (pow((1.0 + rate), periods) - 1))
    annuity = math.ceil(annuity)
    print(f"Your annuity payment = {annuity}!")
    print(f"Overpayment = {int(annuity * periods - credit_principal)}")


def credits_principal(monthly_payment, periods, credit_interest):
    rate = credit_interest / (12 * 100)
    credit_principal = monthly_payment / ((rate * (pow((1 + rate), periods))) / (pow((1.0 + rate), periods) - 1))
    print(f"Your credit principal = {math.floor(credit_principal)}!")
    print(f"Overpayment = {int(periods * monthly_payment - math.floor(credit_principal))}")


def diff_type(credit_principal, periods, credit_interest):
    rate = credit_interest / (12 * 100)
    all_diff = 0
    for m in range(1, periods + 1):
        diff_month = credit_principal / periods + rate * (credit_principal - (credit_principal * (m - 1)) / periods)
        diff_month = math.ceil(diff_month)
        all_diff += diff_month
        print(f"Month {m}: paid out {diff_month}")
    print()
    print(f"Overpayment = {int(all_diff - credit_principal)}")


def status():
    command, principal, interest, period, payment = de_parse(args)
    if command == 'diff' and principal > 0 and period > 0 and interest > 0:
        diff_type(principal, period, interest)
    elif command == 'annuity' and principal >= 0 and payment >= 0 and period >= 0 and interest != 0:
        if principal == 0 and payment != 0 and period != 0:
            credits_principal(payment, period, interest)
        elif payment == 0 and principal != 0 and period != 0:
            annuity_month(principal, period, interest)
        elif period == 0 and principal != 0 and payment != 0:
            n_of_month(principal, payment, interest)
    else:
        print("Incorrect parameters.")


parser = argparse.ArgumentParser(description="Try1")
parser.add_argument("--type", action="store", dest="type_")
parser.add_argument("--principal ", action="store", dest="principal", default=0, type=float)
parser.add_argument("--periods ", action="store", dest="periods", default=0, type=int)
parser.add_argument("--interest ", action="store", dest="interest", default=0, type=float)
parser.add_argument("--payment ", action="store", dest="payment", default=0, type=float)
args = parser.parse_args()

status()
