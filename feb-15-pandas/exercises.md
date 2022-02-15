



1. Write an expression to find the Per Capita GDP of Serbia in 2007.
* `print(data.loc["Serbia", "gdpPercap_2007"])`

2. Explain what each line in the following short program does: 
```python

first = pd.read_csv('data/gapminder_all.csv', index_col='country')
second = first[first['continent'] == 'Americas']
third = second.drop('Puerto Rico')
fourth = third.drop('continent', axis = 1)
fourth.to_csv('result.csv')
```
* First line: creates a data frame called first and loads GDP data of all countries. The second parameter `index_col='country'` selects what column to use to label rows

* Second line: selects data from the `first` data frame where the continent column is equal to 'Americas' and assigns it to the `second` variable

* Third line: drops Puerto Rico row from the `second` data frame and assigns it to `third`. This results in one less row than in the `second` data frame.

* Fourth line: drops a column with index **1** from the `third` data frame

* Fifth line: writes the fourth data frame to a csv file called `results.csv` 

3. 
a) Do the second and third lines below produce the same output? 

b) Based on this, what rule governs what is included (or not) in numerical slices and named slices in Pandas?

```python
europe_gdp_data = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
print(europe_gdp_data.iloc[0:2, 0:2])
print(europe_gdp_data.loc['Albania':'Belgium', 'gdpPercap_1952':'gdpPercap_1962'])
```
* No, the second and third lines do not produce the same output. The second line returns the GDP data with indexes 0 and 1 and stops before it reaches 2 thus, printing the GDP data for Albania and Austria for years 1952 and 1957. The third line returns the GDP data for Albania through Belgium (indexed 0, 1, 2)  and years 1952, 1957 and 1962

* To get the value specified in your numerical slice, it must include the index following the last piece of data you want to receive whereas named slices will include the last indexed row/column specified

4. Stretch Goal: 
Write an expression to select each of the following:
GDP per capita for all countries in 1982.
`print(data['gdpPercap_1982'])`
GDP per capita for Denmark for all years.
`print(data.loc['Denmark',:])`
GDP per capita for all countries for years after 1985.
`print(data.loc[:,'gdpPercap_1985':])`
GDP per capita for each country in 2007 as a multiple of GDP per capita for that country in 1952.
```python
data_07 = data['gdpPercap_2007']
data_52 = data['gdpPercap_1952']
print(data_07 / data_52)
```



\* Excercises borrowed from http://swcarpentry.github.io/python-novice-gapminder/08-data-frames/index.html