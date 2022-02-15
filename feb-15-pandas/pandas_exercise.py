import pandas as pd
import numpy as np


#per capita GDP of Serbia in 07

data = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
print(data.loc["Serbia", "gdpPercap_2007"])

#Running lines from exercises.md file
europe_gdp_data = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
#print(europe_gdp_data.iloc[0:2, 0:2])
#print(europe_gdp_data.loc['Albania':'Belgium', 'gdpPercap_1952':'gdpPercap_1962'])

#Stretch Goal 
#print(data['gdpPercap_1982'])
#print(data.loc['Denmark',:])
#print(data.loc[:,'gdpPercap_1985':])
#GDP per capita for each country in 2007 as a multiple of GDP per capita for that country in 1952.
data_07 = data['gdpPercap_2007']
data_52 = data['gdpPercap_1952']
print(data_07 / data_52)