# Darren & Shilin

import pandas as pd

# 1
gapminder = pd.read_csv("data/gapminder_all.csv")
serbia_data = gapminder.query('country.str.startswith("Serbia")')
#print(serbia_data.filter(items=['gdpPercap_2007']))

# 2
first = pd.read_csv('data/gapminder_all.csv', index_col='country')
#print(first.at['Serbia','gdpPercap_2007'])

second = first[first['continent'] == 'Americas']

third = second.drop('Puerto Rico')

fourth = third.drop('continent', axis = 1)
fourth.to_csv('result.csv')

# 3
europe_gdp_data = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
#print(europe_gdp_data.iloc[0:2, 0:2])
#print(europe_gdp_data.loc['Albania':'Belgium', 'gdpPercap_1952':'gdpPercap_1962'])

# 4
gdp_1982 = gapminder['gdpPercap_1982']

denmark = gapminder[gapminder['country'] == 'Denmark']
denmark_gdp = denmark.filter(regex = 'gdp')

country_gdp = gapminder.loc[:,'gdpPercap_1987':'gdpPercap_2007']

gapminder['multiple_2007_1952'] = gapminder.gdpPercap_2007/gapminder.gdpPercap_1952
multiple = gapminder[['country','multiple_2007_1952']]
