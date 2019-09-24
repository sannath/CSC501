import pandas as pd 
import matplotlib.pyplot as plt

moviesCSV = pd.read_csv("movies.csv")

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
              len(Documentary),len(Drama),len(Fantasy),len(FilmNoir),len(Horror),len(Musical),
              len(Mystery),len(Romance),len(SciFi),len(Thriller),len(War),len(Western),len(unspecified)]

x_axis = ['Action','Adventure','Animation','Childrens','Comedy','Crime',
          'Documentary','Drama','Fantasy','Film-Noir','Horror','Musical',
          'Mystery','Romance','Sci-Fi','Thriller','War','Western','no genres listed']

plt.barh(x_axis,movieCount)
plt.ylabel("GENRES")
plt.xlabel("# Movies")
plt.title("Count of Movies per Genre")
plt.show()

explode = (0,0,0,0,0,0,0,0.2,0,0,0,0,0,0,0,0,0,0,0)
plt.pie(movieCount,explode=explode,textprops={'fontsize': 10})
plt.axis('equal')

plt.legend(pie[0],x_axis, bbox_to_anchor=(1.5,0), loc="lower right", bbox_transform=plt.gcf().transFigure)

plt.show()

