import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np


## Popularity of the Songs in Different Genres
data=pd.read_csv("Datasets/SpotifyFeatures.csv")
df=pd.DataFrame(data)

figure(figsize=(150, 150), dpi=40)

plt.subplots_adjust(bottom=0.25)
plt.title("Popularity of the Songs in Different Genres")
sns.color_palette("rocket",as_cmap=True)
sns.barplot(y="popularity",x="genre",data=df)

plt.xlabel("Genres")
plt.xticks(rotation = 90)
plt.ylabel("Popularity")
plt.show()

## Popularity of the Songs in Different Tempo

data=pd.read_csv("Datasets/SpotifyFeatures.csv")
df=pd.DataFrame(data)
df["tempo_round"]=np.round(df["tempo"])

figure(figsize=(150, 150), dpi=39)
plt.subplots_adjust(bottom=0.25)
plt.title("Popularity of the Songs in Different Tempo")
sns.color_palette("rocket",as_cmap=True)
sns.barplot(y="popularity",x="tempo_round",data=df)

plt.xlabel("Tempo")
plt.xticks(rotation = 90)
plt.ylabel("Popularity")
plt.show()
