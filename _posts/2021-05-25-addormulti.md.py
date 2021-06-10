# 곱 혹은 더하기

data= input()

result = int(data[0])            #data 리스트화

for i in range(1, len(data)):    #조건문 아래 리스트화 시킴으로서 len 함수를 이용해 전체를 돌게함
    num= int(data[i])

    if num <= 1 or result <=1 :  #for문 1부터 시작되며 조건 시작 입력수를 돌리면서 0을 찾을 경우 +0 실행 
        result += num            #곱하기는 순서 상관없고 0은 없앤다는 생각으로 더하기만 하면 된다

    else :
        result *= num

print(result)
