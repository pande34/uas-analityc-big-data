import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


#df = sns.load_dataset('covid.xlsx')

df = pd.read_excel('covid.xlsx', sheet_name='kasus')

#lst=[]
#for i in df.index:
 #   data={}
  #  data['Provinsi_Asal'] = df['Provinsi_Asal'][i]
   # data['Kasus'] = df['Kasus'][i]
    #data['Sembuh'] = df['Sembuh'][i]
   # lst.append(data)
#print(lst)
grid = sns.FacetGrid(df, col="Provinsi_Asal", hue="Provinsi_Asal", palette="tab20c",
                     col_wrap=4, height=1.5)

# Draw a horizontal line to show the starting point
grid.map(plt.axhline, y=0, ls=":", c=".5")

# Draw a line plot to show the trajectory of each random walk
grid.map(plt.plot, "Sembuh", "Kematian", marker="o")

# Adjust the tick positions and labels
grid.set(xticks=np.arange(5), yticks=[-3, 3],
         xlim=(-.5, 4.5), ylim=(-3.5, 3.5))

# Adjust the arrangement of the plots
grid.fig.tight_layout(w_pad=1)


