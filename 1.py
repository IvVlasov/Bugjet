import pymongo
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
plt.close('all')
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['Project']
collection = db['mycoll']
df =pd.DataFrame()
simbols=['{','agency_name',':',"'",'}','1912_y','1913_y','1914_y','1915_y']



name=[]
a=db.mycoll.find({},{ "agency_name" :1, '_id': 0 })
for i in a:
    name.append(i)
df['Наименование ведомства'] = name
df['Наименование ведомства'] = df['Наименование ведомства'].astype(str)
for simbol in simbols:
    df['Наименование ведомства']= df['Наименование ведомства'].str.replace(simbol,'')


year=[]
a=db.mycoll.find({},{ "1912_y" :1, '_id': 0 })
for i in a:
    year.append(i)
df["Расходы(млн.руб.)"]=year
df["Расходы(млн.руб.)"]=df["Расходы(млн.руб.)"].astype(str)
for simbol in simbols:
    df["Расходы(млн.руб.)"]=df["Расходы(млн.руб.)"].str.replace(simbol,'')
df["Расходы(млн.руб.)"]=df["Расходы(млн.руб.)"].astype(float)//1000000


result=df.groupby(["Наименование ведомства"])["Расходы(млн.руб.)"].aggregate(np.median).reset_index().sort_values("Расходы(млн.руб.)",ascending=False)
plt.figure(figsize=(21,11),dpi=70.100,tight_layout =True)
plt.yticks(fontsize=13)
plt.xticks(fontsize=23)
plt.xlim (xmax=660)  # изменяем максимальное отображаемое число на оси
ax=sns.barplot( x="Расходы(млн.руб.)",y='Наименование ведомства',data=df,orient= 'h',ci=None,order=result['Наименование ведомства'])
for spine in plt.gca().spines.values(): spine.set_visible(False)
ax.grid(axis = 'x')
ax.text(-500,0 ,'1912 год',fontsize=30)
plt.show()


year=[]
a=db.mycoll.find({},{ "1913_y" :1, '_id': 0 })
for i in a:
    year.append(i)
df['Расходы(млн.руб.)']=year
df['Расходы(млн.руб.)']=df['Расходы(млн.руб.)'].astype(str)
year=[]
for simbol in simbols:
    df['Расходы(млн.руб.)']=df['Расходы(млн.руб.)'].str.replace(simbol,'')
df['Расходы(млн.руб.)']=df['Расходы(млн.руб.)'].astype(float)/1000000
plt.figure(figsize=(21,11),dpi=70.100,tight_layout =True)
plt.yticks(fontsize=13)
plt.xticks(fontsize=23)
plt.xlim (xmax=660)
ax=sns.barplot( x='Расходы(млн.руб.)',y='Наименование ведомства',data=df,orient= 'h',ci=None,order=result['Наименование ведомства'])
for spine in plt.gca().spines.values(): spine.set_visible(False)
ax.grid(axis = 'x')
ax.text(-500,0 ,'1913 год',fontsize=30)
plt.show()
del df['Расходы(млн.руб.)']

year=[]
a=db.mycoll.find({},{ "1914_y" :1, '_id': 0 })
for i in a:
    year.append(i)
df['Расходы(млн.руб.)']=year
df['Расходы(млн.руб.)']=df['Расходы(млн.руб.)'].astype(str)
year=[]
for simbol in simbols:
    df['Расходы(млн.руб.)']=df['Расходы(млн.руб.)'].str.replace(simbol,'')
df['Расходы(млн.руб.)']=df['Расходы(млн.руб.)'].astype(float)/1000000
plt.figure(figsize=(21,11),dpi=70.100,tight_layout =True)
plt.yticks(fontsize=13)
plt.xticks(fontsize=23)
plt.xlim (xmax=660)
ax=sns.barplot( x='Расходы(млн.руб.)',y='Наименование ведомства',data=df,orient= 'h',ci=None,order=result['Наименование ведомства'])
for spine in plt.gca().spines.values(): spine.set_visible(False)
ax.grid(axis = 'x')
ax.text(-500,0 ,'1914 год',fontsize=30)
plt.show()
del df['Расходы(млн.руб.)']

year=[]
a=db.mycoll.find({},{ "1915_y" :1, '_id': 0 })
for i in a:
    year.append(i)
df['Расходы(млн.руб.)']=year
df['Расходы(млн.руб.)']=df['Расходы(млн.руб.)'].astype(str)
year=[]
for simbol in simbols:
    df['Расходы(млн.руб.)']=df['Расходы(млн.руб.)'].str.replace(simbol,'')
df['Расходы(млн.руб.)']=df['Расходы(млн.руб.)'].astype(float)/1000000
plt.figure(figsize=(21,11),dpi=70.100,tight_layout =True)
plt.yticks(fontsize=13)
plt.xticks(fontsize=23)
plt.xlim (xmax=660)
ax=sns.barplot( x='Расходы(млн.руб.)',y='Наименование ведомства',data=df,orient= 'h',ci=None,order=result['Наименование ведомства'])
for spine in plt.gca().spines.values(): spine.set_visible(False)
ax.grid(axis = 'x')
ax.text(-500,0 ,'1915 год',fontsize=30)
plt.show()

