# matplotlib_csv
Advanced Python - Matplotlib - using CSV files

this project is to teach students how to use CSV files in python
this project also teaches students how to visualize the data using matplotlib

sitka_1 prints the index and resukting header titles, appends the high temperatures for sitka in 7/2018 to its respective list, sets the graph color to red, adds a table title of "Daily high temperatures, July 2018", does not have an x-axis label, labels the y-axis as "Temperatures (F), and adds tick marks to the graph before displaying everything

sitka_2 does the same thing as sitka_1 except we now obtain the date for each temperature, format it appropriately, and replace it where the sitka_1 only had days as tickers. The x label is changed to "Month of July 2018" and the dates are displayed at a diagonal via fig.autofmt_xdate()

stika_3 uses all the temperatures, both highs and lows, for the entire 2018 year in Sitka. Highs and lows are pulled from their respective indices and appended to a lows and highs list along with the same date formatting we did in sitka_2. Highs are still noted as red as before but lows are now noted as blue. We add in plt.subplot() that allows us to specify the graph format of 2 rows and one column. This allows us to split the graph in two, with the top only noting the high temperatures and the bottom only noting the low temperatures. Finally, we add the title of "Highs and Lows of Sitka, Alaska 2018"

sitka_4 takes sitka_3 with its high and low temperatures for the year for 2018 for sitka and places it in one graph, creating an opaque blue shading between the high and low temperatures

sitka_5 does the same as sitka_4 but with sitka and death valley temperatures