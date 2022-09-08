import argparse


def calc_regular_investment_result(
    investment_amount_per_month: int = 50000,
    investment_period_year: int = 20,
    return_on_investment_percent: int = 5,
):
    investment_amount_per_year = investment_amount_per_month * 12
    investment_amount, investment_result = 0, 0
    print()
    print("<year>", "<investment amount>", "<investment result>", "<profit amount>", "<ROI>")
    for i in range(investment_period_year):
        investment_amount += investment_amount_per_year
        investment_result += investment_amount_per_year
        investment_result *= 1 + return_on_investment_percent / 100
        profit_amount = investment_result - investment_amount
        roi = profit_amount / investment_amount * 100
        print(f"{i+1: >6}", f"{investment_amount: >19,.0f}", f"{investment_result: >19,.0f}", f"{profit_amount: >15,.0f}", f"{roi: >5.0f}")
    print()
    return investment_amount, investment_result


def calc_regular_investment_amount(
    investment_period_year: int = 10,
    target_amount: int = 100_000_000,
    return_on_investment_percent: int = 5,
):
    pass


parser = argparse.ArgumentParser()
parser.add_argument("-a", "--investment-amount-per-month", help="investment amount per month", type=int, required=True)
parser.add_argument("-p", "--investment-period-year", help="investment period year", type=int, required=True)
parser.add_argument("-r", "--return-on-investment-percent", help="return on investment percent", type=int, required=True)
args = parser.parse_args()

calc_regular_investment_result(
    args.investment_amount_per_month, args.investment_period_year, args.return_on_investment_percent
)

