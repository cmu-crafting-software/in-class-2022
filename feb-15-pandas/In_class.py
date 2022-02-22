import pandas as pd
data = pd.read_csv('data/gapminder_all.csv')
df = pd.DataFrame(data)
Serbia = data[data.country=='Serbia']['gdpPercap_2007']
#print(Serbia)
#print(Serbia['gdpPercap_2007'])
#print(df.head(5))

first = pd.read_csv('data/gapminder_all.csv', index_col='country')
df = pd.DataFrame(first)
second = first[first['continent'] == 'Americas']
third = second.drop('Puerto Rico')
fourth = third.drop('continent', axis = 1)
fourth.to_csv('result.csv')
print(fourth)
#print(df.head(5))