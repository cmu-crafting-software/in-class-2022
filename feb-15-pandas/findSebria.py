import pandas as pd

europe_gdp_data = pd.read_csv('data/gapminder_gdp_europe.csv')

europe_serbia = europe_gdp_data[europe_gdp_data['country'] == 'Serbia']
#print(europe_serbia)
gdpPercap_2007 = europe_serbia['gdpPercap_2007']
#print(gdpPercap_2007)

first = pd.read_csv('data/gapminder_all.csv', index_col='country')
second = first[first['continent'] == 'Americas']
#print(second)
third = second.drop('Puerto Rico')
print(third)
fourth = third.drop('continent', axis = 1)
#print(fourth)
#fourth.to_csv('result.csv')