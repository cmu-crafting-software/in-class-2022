import pandas as pd

df=pd.read_csv('data/gapminder_all.csv')
serbia_df=df[df['country']=='Serbia']
print(serbia_df['gdpPercap_2007'])


first = pd.read_csv('data/gapminder_all.csv', index_col='country') #creates a dataframe that is indexed alphabetically by country
second = first[first['continent'] == 'Americas'] #creates a second data frame that only includes countries in the continent of America
third = second.drop('Puerto Rico') #removes puerto rico from the previous data frame and saves as a new dataframe
fourth = third.drop('continent', axis = 1) #removes the continent column 
fourth.to_csv('result.csv') #saves result to csv