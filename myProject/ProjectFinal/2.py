import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
name=[]
df=pd.read_csv('/Users/ivan/Downloads/data-20141230-structure-20141230.csv')
df['Наименование ведомства']=df['agency_name']
df["Расходы(млн.руб.)"]=df['1912_y']
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
df['Расходы(млн.руб.)']=df['1913_y']
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

df['Расходы(млн.руб.)']=df['1914_y']
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

df['Расходы(млн.руб.)']=df['1915_y']
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