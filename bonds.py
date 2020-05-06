import pandas as pd
import matplotlib.style as style
import matplotlib.ticker as mticker
import matplotlib.pyplot as plt
from functions import get_max_negative_years

style.use('seaborn-poster')
style.use('ggplot')
pd.plotting.register_matplotlib_converters()

df = pd.read_csv('csvs/bonds.csv')
df['year'] = pd.to_datetime(df['year'], format = '%Y')

corporate_bond_plot = []
t_bond_plot = []
corporate_bond_account = 1000
t_bond_account = 1000
for i in range(0, len(df)):
    corporate_bond_account += corporate_bond_account * (float(df['corporate_bond'][i][:-1])/100)
    corporate_bond_plot.append(corporate_bond_account)

    t_bond_account += t_bond_account * (float(df['t_bond'][i][:-1])/100)
    t_bond_plot.append(t_bond_account)


plt.plot(df['year'], corporate_bond_plot, label="BAA Corporate Bond", color='cornflowerblue')
plt.plot(df['year'], t_bond_plot, label="T Bond", color='lightsalmon')
plt.legend(loc="upper left")
plt.title('Growth of $1000')
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('$%d'))
plt.show()

corporate_drawdown = get_max_negative_years(corporate_bond_plot, df['year'])
plt.bar(df['year'], corporate_drawdown, width=200, color='cornflowerblue')
plt.ylabel('Years', fontsize=16)
plt.title('BAA Corporate Bond: Max Years From Entry With Negative Profits')
plt.show()

t_bond_drawdown = get_max_negative_years(t_bond_plot, df['year'])
plt.bar(df['year'], t_bond_drawdown, width=200, color='cornflowerblue')
plt.ylabel('Years', fontsize=16)
plt.title('T Bond: Max Years From Entry With Negative Profits')
plt.show()
