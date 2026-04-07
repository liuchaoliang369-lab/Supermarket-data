# -*- coding:utf-8 -*-

import pandas as pd
from sqlalchemy import create_engine

#Data import
path = 'C:/Users/31141/Desktop/trainingdata/data/OnlineRetail.xlsx'
df = pd.read_excel(path)

#Cleaning and sorting of data

#Create a SQL connection
connect_str = 'mssql+pyodbc://sa:3114107190@localhost/MyDb?driver=ODBC+Driver+17+for+SQL+Server'
engine = create_engine(connect_str)
df.to_sql('mydata_1',engine,if_exists = 'replace',index=False)

print('Successfully inserted data into mydata_1')