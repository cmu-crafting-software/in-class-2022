



1. Write an expression to find the Per Capita GDP of Serbia in 2007.
    Value of GDP per cap of Serbia in 2007 = 9786.53
2. Explain what each line in the following short program does: 
```python
first = pd.read_csv('data/gapminder_all.csv', index_col='country')
    The first line takes all the data from the gapminder file and defines the indexing column based on the country
second = first[first['continent'] == 'Americas']
    This line pulls out all of the data that is labeled as 'Americas' in the 'continent' column.
third = second.drop('Puerto Rico')
    This removes the row for 'Puerto Rico' from the "second" data set
fourth = third.drop('continent', axis = 1)
    This removes the continent column from the data set
fourth.to_csv('result.csv')
    This creates a csv file with the "fourth" data frame inside of 'result.csv'
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
