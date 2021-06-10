
n, k =map(int, input().split())  # 17 4 

res = 0

while True:
    tar = (n//k) * k        #n이 k로 나누어 떨어지는 수가 될때까지 빼기
    res += (n-tar)          
    n=tar               
    if n<k:                 #n이 k보다 작을 때 반복문 탈출 (더 이상 나눌수 없을때) 
        break

    res +=1
    n//=k

res += (n-1)                #마지막으로 남은 수 1씩 빼기
print(res)
