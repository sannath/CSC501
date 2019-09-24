import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt

ratingsCSV = pd.read_csv("ratings.csv")
moviesCSV = pd.read_csv("movies.csv")

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

Action = []
Adventure = []
Animation = []
Childrens = []
Comedy = []
Crime = []
Documentary = []
Drama = []
Fantasy = []
FilmNoir = []
Horror = []
IMAX = []
Musical = []
Mystery = []
Romance = []
SciFi = []
Thriller = []
War = []
Western = []
unspecified = []

year = []

h_rated = []

for x in range(len(ratingsCSV)) : 
    if ratingsCSV.rating[x] == 4.0 or ratingsCSV.rating[x] ==4.5 or ratingsCSV.rating[x]== 5.0 :
        h_rated.append(ratingsCSV.movieId[x])

u_h_rated = list(dict.fromkeys(h_rated))
u_h_rated.sort()

y=0

for x in range(len(moviesCSV)):
    if moviesCSV.movieId[x] == u_h_rated[y] :
        y+=1
        title = moviesCSV.title[x]
        if title.find('(') != -1 :
            yr = title.split('(')[-1]
            year.append(yr[0:4])

for x in range(len(year)):
    if int(year[x])>2010 and int(year[x])<2021 :
        tens.append(year[x])
    elif int(year[x])>2000 and int(year[x])<2011 :
        aughts.append(year[x])
    elif int(year[x])>1990 and int(year[x])<2001 :
        ninties.append(year[x])
    elif int(year[x])>1980 and int(year[x])<1991 :
        eighties.append(year[x])
    elif int(year[x])>1970 and int(year[x])<1981 :
        seventies.append(year[x])
    elif int(year[x])>1960 and int(year[x])<1971 :
        sixties.append(year[x])
    elif int(year[x])>1950 and int(year[x])<1961 :
        fifties.append(year[x])
    elif int(year[x])>1940 and int(year[x])<1951 :
        forties.append(year[x])
    elif int(year[x])>1930 and int(year[x])<1941 :
        thirties.append(year[x])
    elif int(year[x])>1920 and int(year[x])<1931 :
        twenties.append(year[x])

count = [len(twenties),len(thirties),len(forties),len(fifties),len(sixties),len(seventies),
         len(eighties),len(ninties),len(aughts),len(tens)]

x_axis = [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010]

plt.bar(x_axis,count,color='green')
#plt.plot(x_axis,count,color='blue')
plt.xlabel("Decades")
plt.ylabel("Count of high rated movies")
plt.title("Number of movies with 4 and above rating per decade")
plt.show()

genres = moviesCSV.genres

for x in range(len(genres)) :
    g = genres[x].split('|')
    for y in range(len(g)) :
        if g[y]=="Action" : 
            Action.append(moviesCSV.title[x])
        elif g[y]=="Adventure" :
            Adventure.append(moviesCSV.title[x])
        elif g[y]=="Animation" :
            Animation.append(moviesCSV.title[x])
        elif g[y]=="Children" :
            Childrens.append(moviesCSV.title[x])
        elif g[y]=="Comedy" :
            Comedy.append(moviesCSV.title[x])
        elif g[y]=="Crime" :
            Crime.append(moviesCSV.title[x])
        elif g[y]=="Documentary" :
            Documentary.append(moviesCSV.title[x])
        elif g[y]=="Drama" :
            Drama.append(moviesCSV.title[x])
        elif g[y]=="Fantasy" :
            Fantasy.append(moviesCSV.title[x])
        elif g[y]=="Film-Noir" :
            FilmNoir.append(moviesCSV.title[x])
        elif g[y]=="Horror" :
            Horror.append(moviesCSV.title[x])
        elif g[y]=="IMAX" :
            IMAX.append(moviesCSV.title[x])
        elif g[y]=="Musical" :
            Musical.append(moviesCSV.title[x])
        elif g[y]=="Mystery" :
            Mystery.append(moviesCSV.title[x])
        elif g[y]=="Romance" :
            Romance.append(moviesCSV.title[x])
        elif g[y]=="Sci-Fi" :
            SciFi.append(moviesCSV.title[x])
        elif g[y]=="Thriller" :
            Thriller.append(moviesCSV.title[x])
        elif g[y]=="War" :
            War.append(moviesCSV.title[x])
        elif g[y]=="Western" :
            Western.append(moviesCSV.title[x])
        else :
            unspecified.append(moviesCSV.title[x])

movieCount = [len(Action),len(Adventure),len(Animation),len(Childrens),len(Comedy),len(Crime),
              len(Documentary),len(Drama),len(Fantasy),len(FilmNoir),len(Horror),len(IMAX),len(Musical),
              len(Mystery),len(Romance),len(SciFi),len(Thriller),len(War),len(Western),len(unspecified)]

x_axis = ['Action','Adventure','Animation','Childrens','Comedy','Crime',
          'Documentary','Drama','Fantasy','Film-Noir','Horror','IMAX','Musical',
          'Mystery','Romance','Sci-Fi','Thriller','War','Western','no genres listed']

plt.barh(x_axis,movieCount)
plt.ylabel("GENRES")
plt.xlabel("# Movies")
plt.title("Number of Movies per Genre")
plt.show()

z=0
genres = []
for x in range(len(moviesCSV)) :
    if moviesCSV.movieId[x] == u_h_rated[z] :
        z+=1
        genre = moviesCSV.genres[x]
        g = genre.split('|')
        for y in range(len(g)) :
            genres.append(g[y])

y = [genres.count("Action"),genres.count("Adventure"),genres.count("Animation"),genres.count("Children"),
     genres.count("Comedy"),genres.count("Crime"),genres.count("Documentary"),genres.count("Drama"),
     genres.count("Fantasy"),genres.count("Film-Noir"),genres.count("Horror"),genres.count("IMAX"),genres.count("Musical"),
     genres.count("Mystery"),genres.count("Romance"),genres.count("Sci-Fi"),genres.count("Thriller"),
     genres.count("War"),genres.count("Western"),genres.count("(no genres listed)")]

y_axis = []
for x in range(len(y)) :
    y_axis.append(y[x]/movieCount[x]*100)

x_axis = ['Action','Adventure','Animation','Childrens','Comedy','Crime','Documentary','Drama','Fantasy','Film-Noir',
          'Horror','IMAX','Musical','Mystery','Romance','Sci-Fi','Thriller','War','Western','(no genres listed)']

plt.barh(x_axis,y_axis)
plt.xlim(50,90)
plt.xlabel("Percentage")
plt.ylabel("Genres")
plt.title("% of movies within each genre which are rated 4 and above")
plt.show()
