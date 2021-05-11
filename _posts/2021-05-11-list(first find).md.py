"""
n=int(input())

k=map(int,input().split())

a=min(k)

print(a)
"""
n = int(input())                    #횟수 입력

k = list(map(int,input().split()))  #입력 된 수들을 리스트로 정리
 
a=k[0]                              #k리스트 첫번째 수를 a

for i in range(n):                  #리스트 하나씩 검사
    if(a>k[i]):                     #0~9인 i를 k리스트에 넣어 k[i] 형태로 만들면 
                                          인덱스 번호로 0~9 위치에 숫자랑 비교 
        a=k[i]                      #만약 a(10)이 리스트 i숫자들 보다 클경우
                                         #비교당한 숫자가 a
print(a) 
