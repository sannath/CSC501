import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

ratingsCSV = pd.read_csv("ratings.csv");

y_axis = []
zeroF_band_rating = ratingsCSV[(ratingsCSV.rating == 0.5)]
y_axis.append(len(zeroF_band_rating))
one_band_rating = ratingsCSV[(ratingsCSV.rating == 1.0)] 
y_axis.append(len(one_band_rating))
oneF_band_rating = ratingsCSV[(ratingsCSV.rating == 1.5)]
y_axis.append(len(oneF_band_rating))
two_band_rating = ratingsCSV[(ratingsCSV.rating == 2.0)] 
y_axis.append(len(two_band_rating))
twoF_band_rating = ratingsCSV[(ratingsCSV.rating == 2.5)]
y_axis.append(len(twoF_band_rating))
three_band_rating = ratingsCSV[(ratingsCSV.rating == 3.0)]
y_axis.append(len(three_band_rating))
threeF_band_rating = ratingsCSV[(ratingsCSV.rating == 3.5)]
y_axis.append(len(threeF_band_rating))
four_band_rating = ratingsCSV[(ratingsCSV.rating == 4.0)]
y_axis.append(len(four_band_rating))
fourF_band_rating = ratingsCSV[(ratingsCSV.rating == 4.5)]
y_axis.append(len(fourF_band_rating))
five_rating = ratingsCSV[(ratingsCSV.rating == 5.0)]
y_axis.append(len(five_rating))

x_axis = [0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]
x = range(0,10)

plt.xticks(x,x_axis)
plt.bar(x,y_axis)
plt.xlabel("Rating")
plt.ylabel("Number of Movies")
plt.title("Total count of movies for each rating")
plt.show()

