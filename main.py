import pandas as pd
job=pd.read_csv('취업 데이터(2016-2021).csv')

electronic_engineering=job['학과']=='지능형전자시스템전공'
sub1=job.loc[electronic_engineering]
print(electronic_engineering)
print(sub1)