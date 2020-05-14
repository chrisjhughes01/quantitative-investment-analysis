import pandas as pd
import matplotlib.style as style
import matplotlib.ticker as mticker
import matplotlib.pyplot as plt
from functions import get_max_negative_years

style.use('seaborn-poster')
style.use('ggplot')
pd.plotting.register_matplotlib_converters()

df = pd.read_csv('csvs/SPX.csv')
df['Date'] = pd.to_datetime(df['Date'])

dividends_reinvested = []
starting_price = 10
dividends_reinvested.append(starting_price)

for i in range(1, len(df['SP500'])):
    starting_price += starting_price * ((df['SP500'][i] - df['SP500'][i-1])/df['SP500'][i-1])
    if (i+1) % 3 == 0:
        starting_price += starting_price * ((df['Dividend'][i]/df['SP500'][i])/4)
    dividends_reinvested.append(starting_price)

plt.plot(df['Date'], dividends_reinvested, color='cornflowerblue')
plt.title('Growth of $10')
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('$%d'))
plt.show()

spx_max_negative_years = get_max_negative_years(dividends_reinvested, df['Date'])
plt.bar(df['Date'], spx_max_negative_years, width=125, color='cornflowerblue')
plt.title('S&P 500: Max Years From Entry With Negative Profits')
plt.ylabel('Years', fontsize=16)
plt.show()

max_negative_length = max(spx_max_negative_years)
max_negative_start_date = df['Date'][spx_max_negative_years.index(max_negative_length)]
print('The longest time period of negative profits was', round(max_negative_length, 2), 'years starting on', max_negative_start_date.date())
