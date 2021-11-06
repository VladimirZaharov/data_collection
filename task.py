import pandas as pd
from requests import get
import matplotlib.pyplot as plt

url = 'https://data.gov.ru/opendata/7710914971-demograph/data-20151002T0951-structure-20151002T0951.csv'
df = pd.read_csv(url,sep=',')
#Хотел сделать динамику "родившихся к умершим" за 2013 и 2012 годы
df_2012 = df.loc[:,['born_2012','dead_2012']]
df_2013 = df.loc[:,['born_2013','dead_2013']]
born_2012 = df['born_2012'].map(lambda a: a.replace(',','.'))
born_2013 = df['born_2013'].map(lambda a: a.replace(',','.'))
dead_2012 = df['dead_2012'].map(lambda a: a.replace(',','.'))
dead_2013 = df['dead_2013'].map(lambda a: a.replace(',','.'))
born_2012 = born_2012.astype(float)
born_2013 = born_2013.astype(float)
dead_2012 = dead_2012.astype(float)
dead_2013 = dead_2013.astype(float)

my_df = pd.DataFrame({
    'born_2012': born_2012,
    'born_2013': born_2013,
    'dead_2012': dead_2012,
    'dead_2013': dead_2013
})

#df_2012.plot()
my_df.plot()
plt.show()