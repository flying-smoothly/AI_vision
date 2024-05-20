import pandas as pd
fifa2019=pd.read_csv('fifa2019.csv')
df=pd.DataFrame.copy(fifa2019.sort_values(by='Overall',ascending=False).head(200))
test_features=['Name','Stamina','Dribbling','ShortPassing','Penalties']
test_df=pd.DataFrame(df,columns=test_features)

import numpy as np
XY=np.array(test_df)
X=XY[:,1:3]
K=3
C_x=np.random.choice(X[:,0],K)
C_y=np.random.choice(X[:,1],K)
C=np.array(list(zip(C_x,C_y)))

import matplotlib.pyplot as plt
Stamina=test_df['Stamina']
Dribbling=test_df['Dribbling']
plt.title('Stamina&Dribbling')
plt.xlabel('Stamina')
plt.ylabel('Dribbling')
plt.scatter(Stamina, Dribbling, marker='^',c='blue',s=10,label='player')
plt.scatter(C_x,C_y,marker='*',s=200,c='black',label='centroids')
plt.legend(loc='best')
plt.grid()
plt.show()