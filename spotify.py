import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np



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
