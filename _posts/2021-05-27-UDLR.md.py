"""
# 동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 현재 위치 (5*5 일때 중간)
x, y = 2, 2

for i in range(4):
    # 다음 위치
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)
"""
n= int(input())
x, y = 1 ,1
plans = input().split()

dx = [0, 0, -1, 1]                        # L R U D 에 따른 이동 
dy = [-1, 1, 0, 0]

move_types = ['L','R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:           # 무브에 있는 방향이 입력된 plans와 같다면 변수 순서대로 x+, y+ 실행
             nx = x + dx[i]
             ny = y + dy[i]
    if nx < 1 or ny < 1 or nx> n or ny>n:   # 공간을 벗어나는 경우 무시 (순서가 어떻게 되던 진행 할 수 있음, continue로 오류 차단)
        continue
    x,y = nx, ny

print(x, y)
