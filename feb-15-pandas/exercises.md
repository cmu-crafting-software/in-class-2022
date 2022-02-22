
```python
#I have been able to run this outside a python environment?
```

1. Write an expression to find the Per Capita GDP of Serbia in 2007.
<!-- # csv_input = pd.read_csv("data\gapminder_all.csv")

# # serbia_gdp_2007 = csv_input.loc[csv_input["country"] == "Serbia", "gdpPercap_2007"]
# # print(serbia_gdp_2007) #why does it print row 132 when the row is 134? -->
2. Explain what each line in the following short program does: 
```python
first = pd.read_csv('data/gapminder_all.csv', index_col='country') #reads in the csv file and stores it as a DataFrame object variable named "first"; the index column (leftmost column to be displayed) will be "country"
second = first[first['continent'] == 'Americas'] #stores, as a DataFrame object named "second", the full table but filtered for data that is on the "Americas" continent 
third = second.drop('Puerto Rico') #drops the row with "Puerto Rico" from the table
fourth = third.drop('continent', axis = 1) #drop the "continent" column; 1 is column, 0 is row (default is 0)
fourth.to_csv('result.csv') #converts the fourth DataFrame back to a csv file
```
3. 
a) Do the second and third lines below produce the same output? no 
b) Based on this, what rule governs what is included (or not) in numerical slices and named slices in Pandas?
```python
europe_gdp_data = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country') 
print(europe_gdp_data.iloc[0:2, 0:2])
print(europe_gdp_data.loc['Albania':'Belgium', 'gdpPercap_1952':'gdpPercap_1962'])
```

4. Stretch Goal: 
Write an expression to select each of the following:
GDP per capita for all countries in 1982.
```python
#gdp_all_1982 = csv_input["gdpPercap_1982"]
#print(gdp_all_1982)
```
GDP per capita for Denmark for all years.
```python
# gdp_Denmark = csv_input.loc[csv_input["country"] == "Denmark","gdpPercap_1952":"gdpPercap_2007"]
# print(gdp_Denmark) why is the line count off by 2 like above?
```
GDP per capita for all countries for years after 1985.
```python
# gdp_all_after_1985 = csv_input.loc[:,"gdpPercap_1985":"gdpPercap_2007"]
# print(gdp_all_after_1985) #why does this work? 1985 is not a column??
```
GDP per capita for each country in 2007 as a multiple of GDP per capita for that country in 1952.
```python
# csv_input["GDP 2007/1952"] = csv_input["gdpPercap_2007"] / csv_input["gdpPercap_1952"]
# gdp_multiple = csv_input["GDP 2007/1952"]
# print(gdp_multiple)
```

\* Excercises borrowed from http://swcarpentry.github.io/python-novice-gapminder/08-data-frames/index.html