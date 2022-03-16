# 1) changing the file to include all the data for the year of 2018
# 2) change the titel to - Daily low and high temperatures - 2018
# 3) extract low temps from the file and add to chart
# 4) shade in the area between high and low


import csv
from datetime import datetime

open_file_sa = open("sitka_weather_2018_simple.csv","r")
open_file_dv = open("death_valley_2018_simple.csv","r")

csv_file_sa = csv.reader(open_file_sa, delimiter=",")
csv_file_dv = csv.reader(open_file_dv, delimiter=",")

header_row_sa = next(csv_file_sa)
header_row_dv = next(csv_file_dv)

tminsa = header_row_sa.index("TMIN")
tmaxsa = header_row_sa.index("TMAX")
tmindv = header_row_dv.index("TMIN")
tmaxdv = header_row_dv.index("TMAX")
sa_title = header_row_sa.index("NAME")
dv_title = header_row_dv.index("NAME")

lows_dv = []
lows_sa = []
highs_dv = []
highs_sa = []
dates_dv = []
dates_sa = []

for row in csv_file_sa:
    try:
        current_date = datetime.strptime(row[2],"%Y-%m-%d")
        high = int(row[tmaxsa])
        low = int(row[tminsa])
        sa_header = row[sa_title]           
    except ValueError:    
        print(f"Missing data for {current_date}")
    else:
        highs_sa.append(high)
        lows_sa.append(low)
        dates_sa.append(current_date)
for row in csv_file_dv:
    try:
        current_date = datetime.strptime(row[2],"%Y-%m-%d")
        high = int(row[tmaxdv])
        low = int(row[tmindv])
        dv_header = row[dv_title]            
    except ValueError:    
        print(f"Missing data for {current_date}")
    else:
        highs_dv.append(high)
        lows_dv.append(low)
        dates_dv.append(current_date)

import matplotlib.pyplot as plt

fig = plt.figure()

plt.title("Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)


plt.subplot(2,1,1)
plt.plot(dates_sa, highs_sa, c="red")
plt.plot(dates_sa, lows_sa, c="blue")
plt.fill_between(dates_sa, highs_sa, lows_sa, facecolor="blue", alpha=0.1)
plt.title(sa_header)

plt.subplot(2,1,2)
plt.plot(dates_dv, highs_dv, c="red")
plt.plot(dates_dv, lows_dv, c="blue")
plt.fill_between(dates_dv, highs_dv, lows_dv, facecolor="blue", alpha=0.1)
plt.title(dv_header)

fig.autofmt_xdate()

plt.suptitle("Temperature comparison between "+sa_header+" and "+dv_header)

plt.show()
