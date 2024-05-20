import pandas as pd
fifa2019=pd.read_csv('fifa2019.csv')
print(fifa2019.shape)
import matplotlib.pyplot as plt

fifa2019['Preferred Foot'].value_counts().plot(kind='pie',autopct='%1.f%%')
plt.legend()
plt.show()