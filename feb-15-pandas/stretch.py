import pandas as pd

dataset = pd.read_csv('data/gapminder_all.csv', index_col='country')
print("GDP per capita for all countries in 1982")
print(dataset.loc[:,'gdpPercap_1982'])
print("GDP per capita for Denmark for all years")
print(dataset.loc['Denmark','gdpPercap_1952':'gdpPercap_2007'])
print("GDP per capita for all countries for years after 1985")
print(dataset.loc[:,'gdpPercap_1987':'gdpPercap_2007'])
print("GDP per capita for each country in 2007 as a multiple of GDP per capita for that country in 1952")
print(dataset.loc[:,'gdpPercap_2007']/dataset.loc[:,'gdpPercap_1952'])