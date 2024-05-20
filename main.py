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

def Distance(A,B):
    return np.sqrt(np.sum(np.power((A-B),2)))
C_old=np.zeros(C.shape) #중심의 좌표를 업데이트하기 위해 동일한 크기의 행렬을 선언한다.
clusters=np.zeros(len(X)) #모든 데이터의 클러스터 레이블을 저장하기 위해 행렬을 선언한다.
#이때 np.zeros()를 사용하여 초깃값을 0으로 하고, 훈련 데이터의 개수만큼이므로 len() 사용.
flag=Distance(C,C_old) #반복문의 종료 기준이 될 flag 변수를 정의한다.
print(C_old)
print(flag)

from copy import deepcopy

distances=[]
while flag!=0: #군집 중심의 좌표가 변화가 없을 때까지 while 문 안의 명령어 반복 실행한다.
    for i in range(len(X)):
        for j in range(3):
            temp=Distance(X[i],C[j])
            distances.append(temp)
        cluster=np.argmin(distances)
        clusters[i]=cluster
        distances=[]

    C_old=deepcopy(C)

    for i in range(K):
        points=[X[j] for j in range(len(X)) if clusters[j]==i]
        C[i]=np.mean(points)

    flag=Distance(C,C_old)

    import matplotlib.pyplot as plt
    plt.scatter(X[clusters==0,0],X[clusters==0,1],s=50,c='red', marker='o',edgecolor ='black',label='A')
    plt.scatter(X[clusters==1,0],X[clusters==1,1],s=50,c='yellow', marker='x',edgecolor ='black',label = 'B')
    plt.scatter(X[clusters==2,0],X[clusters==2,1],s=50,c='blue', marker='^',edgecolor ='black',label = 'C')
    plt.scatter(C[:,0],C[:,1],s=250, marker='*',c='black',edgecolor ='black',label='Centroids')
    plt.legend()
    plt.grid()
    plt.show()