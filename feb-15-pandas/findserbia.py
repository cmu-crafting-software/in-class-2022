import pandas as pd

dataset = pd.read_csv('data/gapminder_all.csv', index_col='country')
print(dataset.loc['Serbia'].gdpPercap_2007)
