# -*- coding: utf-8 -*-

import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
connect_str = 'mssql+pyodbc://sa:3114107190@localhost/MyDb?driver=ODBC+Driver+17+for+SQL+Server'
engine = create_engine(connect_str)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

'''
#年数据汇总，饼图
df_1 = pd.read_sql('country',engine)
df_1_2010 = df_1[df_1['year'] == 2011]



df_sorted = df_1_2010.sort_values('sum_unitprice', ascending=False)
top4 = df_sorted.head(4)
other = pd.DataFrame({
    'name': ['Others'],
    'sum_unitprice': [df_sorted.iloc[4:]['sum_unitprice'].sum()]
})
df_final = pd.concat([top4, other], ignore_index=True)
df_final = df_final.set_index('name')

df_final.plot(y='sum_unitprice', kind='pie', autopct='%1.1f%%', figsize=(10, 10))
plt.show()
'''

str2 = 'select * from counties_month order by year_month,sum_unitprice DESC'
df_2 = pd.read_sql(str2,engine)

df_2_wide = df_2.pivot(index='year_month', columns='country', values='sum_unitprice')
print(df_2_wide)
df_2_wide = df_2_wide.fillna(0).loc[:,['United Kingdom','Germany','EIRE','France','Portugal']]
df_2_wide.plot(kind='line')
plt.show()
