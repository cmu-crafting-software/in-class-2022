



1. Write an expression to find the Per Capita GDP of Serbia in 2007.
df=pd.read_csv('data/gapminder_all.csv')
serbia_df=df[df['country']=='Serbia']
print(serbia_df['gdpPercap_2007'])

2. Explain what each line in the following short program does: 
```python
first = pd.read_csv('data/gapminder_all.csv', index_col='country') #creates a dataframe that is indexed alphabetically by country
second = first[first['continent'] == 'Americas'] #creates a second data frame that only includes countries in the continent of America
third = second.drop('Puerto Rico') #removes puerto rico from the previous data frame and saves as a new dataframe
fourth = third.drop('continent', axis = 1) #removes the continent column 
fourth.to_csv('result.csv') #saves result to csv
```
3. 
a) Do the second and third lines below produce the same output? 

b) Based on this, what rule governs what is included (or not) in numerical slices and named slices in Pandas?
```python
europe_gdp_data = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
print(europe_gdp_data.iloc[0:2, 0:2])
print(europe_gdp_data.loc['Albania':'Belgium', 'gdpPercap_1952':'gdpPercap_1962'])
```

4. Stretch Goal: 
Write an expression to select each of the following:
GDP per capita for all countries in 1982.
GDP per capita for Denmark for all years.
GDP per capita for all countries for years after 1985.
GDP per capita for each country in 2007 as a multiple of GDP per capita for that country in 1952.


\* Excercises borrowed from http://swcarpentry.github.io/python-novice-gapminder/08-data-frames/index.html
