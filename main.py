import matplotlib.pyplot as plt

# 데이터 설정
categories = ['Other service industries', 'electical and electronics']
percentages = [35, 65]
colors = ['green', 'blue']

# 막대 그래프 생성
plt.bar(categories, percentages, color=colors)

# 그래프 제목과 축 레이블 설정
plt.title('programmer percentage')
plt.xlabel('Industrial classification')
plt.ylabel('percentage (%)')

# 그래프 출력
plt.show()
