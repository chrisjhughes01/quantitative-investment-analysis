def get_max_negative_years(equity_curve, date_list):
    max_negative_profit_days = []
    for i in range(0, len(equity_curve)):
        current_month_value = equity_curve[i]
        negative_profit_days = []
        for z in range(i, len(equity_curve)):
            following_months_value = equity_curve[z]
            if current_month_value > following_months_value:
                negative_profit_days.append(date_list[z]-date_list[i])
        if negative_profit_days != []:
            max_negative_profit_days.append(max(negative_profit_days).days/365)
        else:
            max_negative_profit_days.append(0)

    return max_negative_profit_days
