import pandas as pd

fifa2019=pd.read_csv('fifa2019.csv')
korea_player=fifa2019['Nationality']=='Korea Republic'
sub5=fifa2019.loc[korea_player]
print(korea_player)
print(sub5)