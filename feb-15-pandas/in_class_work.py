# In class work Feb 15 by Nikole and Christine

import pandas as pd
# 1 
first = pd.read_csv('data/gapminder_all.csv', index_col='country')
# print(first)

print(first['gdpPercap_2007'].loc['Serbia'])


# 2 
first = pd.read_csv('data/gapminder_all.csv', index_col='country') # reads data 
second = first[first['continent'] == 'Americas'] # get all the americas rows 
# print(second)
third = second.drop('Puerto Rico') # got rid of puerto rico
# print(third)
fourth = third.drop('continent', axis = 1) # drops column continent
# print(fourth)
fourth.to_csv('result.csv') # made a csv

# 3 
europe_gdp_data = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
print(europe_gdp_data.iloc[0:2, 0:2])
print(europe_gdp_data.loc['Albania':'Belgium', 'gdpPercap_1952':'gdpPercap_1962'])
# not the same 0:2 gets columns 0 and 1 and rows 0 and 1 

# named slices are inclusive while number slices are not inclusive of the end value

# 4 
# GDP per capita for all countries in 1982.
print(first['gdpPercap_1982'])

# GDP per capita for Denmark for all years.
print(first.loc['Denmark', 'gdpPercap_1952':'gdpPercap_2007'])

# GDP per capita for all countries for years after 1985.
print(first.loc[:, 'gdpPercap_1987':'gdpPercap_2007'])

# GDP per capita for each country in 2007 as a multiple of GDP per capita for that country in 1952.