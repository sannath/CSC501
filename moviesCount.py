import pandas as pd
import numpy as np
from matplotlib import  pyplot as plt

moviesCSV = pd.read_csv("movies.csv")
title = moviesCSV.title

tens = []
aughts = []
ninties = []
eighties = []
seventies = []
sixties = []
fifties = []
forties = [] 
thirties = []
twenties = []
 
for x in range(len(moviesCSV)):
    if title[x].find('(') != -1:
        year = title[x].split('(')[-1]
        yr = year[0:4]
        if int(yr)>2010 and int(yr)<2021 :
            tens.append(yr)
        elif int(yr)>2000 and int(yr)<2011 :
            aughts.append(yr)
        if int(yr)>1990 and int(yr)<2001 :
            ninties.append(yr)
        if int(yr)>1980 and int(yr)<1991 :
            eighties.append(yr)
        if int(yr)>1970 and int(yr)<1981 :
            seventies.append(yr)
        if int(yr)>1960 and int(yr)<1971 :
            sixties.append(yr)
        if int(yr)>1950 and int(yr)<1961 : 
            fifties.append(yr)
        if int(yr)>1940 and int(yr)<1951 :
            forties.append(yr)
        if int(yr)>1930 and int(yr)<1941 :
            thirties.append(yr)
        if int(yr)>1920 and int(yr)<1931 :
            twenties.append(yr)

count = []
count.append(len(twenties))
count.append(len(thirties))
count.append(len(forties))
count.append(len(fifties))
count.append(len(sixties))
count.append(len(seventies))
count.append(len(eighties))
count.append(len(ninties))
count.append(len(aughts))
count.append(len(tens))

x_axis = ['20s','30s','40s','50s','60s','70s','80s','90s','00s','10s']

plt.plot(x_axis,count)
plt.xlabel("Decades")
plt.ylabel("Number of Movies")
plt.title("Number of movies released per decade")
plt.show()

perChange = [0]
for x in range(len(count)):
   if x < (len(count)-1):
        percentage = (count[x+1]/count[x])*100
        perChange.append(percentage - 100)

#plt.plot(x_axis,perChange)
#plt.title("Percentage difference in number of movies")
#plt.xlabel("Percentage Change")
#plt.ylabel("Decades")
#plt.show()

greenBar = []
redBar = []
mag = []
for x in range(len(perChange)):
    mag.append(np.sign(perChange[x]))
mag
for x in range(len(mag)):
    if mag[x]==0 or mag[x]==1:
        greenBar.append(perChange[x])
        redBar.append(0)
    else: 
        redBar.append(abs(perChange[x]))
        greenBar.append(0)

plt.bar(x_axis,greenBar,label='Increasing rate',color='green')
plt.bar(x_axis,redBar,label='decreasing rate', color='red')
plt.legend()
plt.title("Percentage change in number of movies")
plt.xlabel("Percentage Change")
plt.ylabel("Decades")
plt.show()
