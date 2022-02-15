import pandas as pd

data = pd.read_csv('data/gapminder_all.csv')
serbia = data[data.country=='Serbia']
print(serbia['gdpPercap_2007'])

europe_gdp_data = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
print('line2')
print(europe_gdp_data.iloc[0:2, 0:2])
print('line3')
print(europe_gdp_data.loc['Albania':'Belgium', 'gdpPercap_1952':'gdpPercap_1962'])

#Write an expression to select each of the following:
#GDP per capita for all countries in 1982.
p41 = data['gdpPercap_1982']
#GDP per capita for Denmark for all years.
denmark = data[data.country=='Denmark']
p42 = denmark.filter(regex='gdp')
#GDP per capita for all countries for years after 1985.
p43 = pd.wide_to_long(data, stubnames=['gdpPercap_', 'lifeExp_', 'pop_'], i=['continent', 'country'], j='year')
print(p43.head())
#GDP per capita for each country in 2007 as a multiple of GDP per capita for that country in 1952.
