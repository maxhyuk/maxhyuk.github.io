n=int(input())                             #출석 부를 횟수
                        
a=input().split()                          #호명한 번호

for i in range(n):                          #10 
     a[i]=int(a[i])                         #a 순서대로 저장  # [1, 3, 2, 2, 5, 6, 7, 4, 5, 9]
     
d=[]

for i in range(24):                         #d[0, 0, 0, 0, 0, .....0, 0, 0]  24
     d.append(0)

for i in range(n):                           #번호를 부를때 마다 그 번호에 대한 카운트 1씩 증가
     d[a[i]]+=1

for i in range(1, 24):                       #(1, 24)인 이유는 인덱스 번호상 0부터 시작하기때문에 +1을 안해도 된다
     print(d[i], end=' ')
