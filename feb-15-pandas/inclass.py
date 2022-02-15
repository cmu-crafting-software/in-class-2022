import pandas as pd


#part 1
europe = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
europe = pd.DataFrame(europe)

#print(europe)

serbiaGDP_2007 = europe.at['Serbia', 'gdpPercap_2007']
#print(serbiaGDP_2007)


#Part 2
first = pd.read_csv('data/gapminder_all.csv', index_col='country') #loading csv file of data indexing by the country name
second = first[first['continent'] == 'Americas'] #creating subset of the dataframe of all the data having to do with the Americas
third = second.drop('Puerto Rico') #getting rid of puerto rico row, save as new df
fourth = third.drop('continent', axis = 1) # gets rid of the column listing countries as in the americas (continent)
fourth.to_csv('result.csv') #saving fourth as a csv file


#part 3
#a. no they will not print out the same thing
#b. numerical indices include the first row and col as index 0. names slices are inclusive for the labeles provided
europe_gdp_data = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
#print(europe_gdp_data.iloc[0:2, 0:2])
#print(europe_gdp_data.loc['Albania':'Belgium', 'gdpPercap_1952':'gdpPercap_1962'])


#part4
all = pd.read_csv('data/gapminder_all.csv', index_col='country')
GDPperCap1982 = all['gdpPercap_1982']
#print(GDPperCap1982)
GDPDenmark = europe.loc['Denmark',:]
#print(GDPDenmark)

GDP_all_from1985 = all.iloc[:,8:13]
#print(GDP_all_from1985)

#GPD_math = all['gdpPerca_2007']/all['gdpPercap_1952']
all['GPD_math'] = all['gdpPercap_2007']/all['gdpPercap_1952']
print(all)