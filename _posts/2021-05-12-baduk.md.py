d=[]

for i in range(20):                 #19개의 []생성
    d.append([])                    
    for j in range(20):             #19개의 0으로 채워넣은 리스트 19개 생성
        d[i].append(0)

n=int(input())
for i in range(n):                  #입력받은 숫자 = 입력 횟수
    x, y= input().split()           #좌표 입력 받고 찍는 곳은 1로 표시 
    d[int(x)][int(y)] =1            #x, y 좌표 위치 1로 변환

for i in range(1, 20):
    for j in range(1, 20):          #최종 바둑판 : 19*19 출력
        print(d[i][j], end=' ')
    print()
