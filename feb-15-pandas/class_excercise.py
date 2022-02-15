import pandas as pd

df=pd.read_csv('data/gapminder_all.csv')
serbia_df=df[df['country']=='Serbia']
print(serbia_df['gdpPercap_2007'])

