# 시 분 초에서 정해진 숫자가 들어가 있을시 카운트

n=int(input())

count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count+=1
print(count)
