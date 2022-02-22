import csv
import pandas as pd


csv_input = pd.read_csv("data\gapminder_all.csv")

# # serbia_gdp_2007 = csv_input.loc[csv_input["country"] == "Serbia", "gdpPercap_2007"]
# # print(serbia_gdp_2007) #why does it print row 132 when the row is 134? b/c starts count at 0 after header

# gdp_all_1982 = csv_input["gdpPercap_1982"]
# print(gdp_all_1982)

# gdp_Denmark = csv_input.loc[csv_input["country"] == "Denmark","gdpPercap_1952":"gdpPercap_2007"]
# print(gdp_Denmark)

# gdp_all_after_1985 = csv_input.loc[:,"gdpPercap_1985":"gdpPercap_2007"]
# print(gdp_all_after_1985) #why does this work? 1985 is not a column??

# csv_input["GDP 2007/1952"] = csv_input["gdpPercap_2007"] / csv_input["gdpPercap_1952"]
# gdp_multiple = csv_input["GDP 2007/1952"]
# print(gdp_multiple)