def calc_regular_investment_result(
    investment_amount_per_month: int = 50000,
    investment_range_year: int = 20,
    return_on_investment_percent: int = 5,
):
    investment_amount_per_year = investment_amount_per_month * 12
    simple_result, regular_result = 0, 0
    for i in range(investment_range_year):
        simple_result += investment_amount_per_year
        regular_result += investment_amount_per_year
        regular_result *= 1 + return_on_investment_percent / 100
        print(f"{i+1: >3}:{simple_result: >12,.0f}{regular_result: >12,.0f}{regular_result-simple_result: >12,.0f}")
    return simple_result, regular_result


def calc_regular_investment_amount(
    investment_range_year: int = 10,
    target_amount: int = 100_000_000,
    return_on_investment_percent: int = 5,
):
    pass


if __name__ == "__main__":
    calc_regular_investment_result()
    calc_regular_investment_result(investment_amount_per_month=100000)

