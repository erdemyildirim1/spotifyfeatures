import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np



data=pd.read_csv("Datasets/SpotifyFeatures.csv")
df=pd.DataFrame(data)
df["tempo_round"]=np.round(df["tempo"])
df["tempo_round"]=str(df["tempo_round"])
def tempo(track):
    result=[]
    for i in track:
        if i >=30 and i<=50:
            result.append("30-50 bpm")
        elif i >50 and i<=70:
            result.append("51-70 bpm")
        elif i >70 and i<=90:
            result.append("71-90 bpm")
        elif i >90 and i<=110:
            result.append("91-110 bpm")
        elif i >110 and i<=130:
            result.append("111-130 bpm")
        elif i >130 and i<=150:
            result.append("131-150 bpm")
        elif i >150 and i<=170:
             result.append("151-170 bpm")
        elif i >170 and i<=190:
            result.append("171-190 bpm")
        elif i >190 and i<=210:
            result.append("191-210 bpm")
        elif i >210:
            result.append("210+ bpm")
        else:
            pass

df["tempo_round"]=df["tempo_round"].apply(lambda i: tempo(i["tempo_rounds"]))
figure(figsize=(150, 150), dpi=40)
plt.subplots_adjust(bottom=0.25)
plt.title("Popularity of the Songs in Different Genres")
sns.color_palette("rocket",as_cmap=True)
sns.barplot(y="popularity",x="tempo_round",data=df)
plt.xlabel("Genres")
plt.xticks(rotation = 90)
plt.ylabel("Popularity")
plt.show()