h, w= map(int,input().split())           #세로 가로 입력 
n=int(input())                           #막대 몇개 넣을건지 

board=[]                    

for i in range(h):                       #board=[[0]*w for _ in range(h)] 똑같이 0세팅
    board.append([])
    for j in range(w):
        board[i].append(0)

for i in range(n):                       #ex) 3번이면 정보 세번 
    l, d, x, y=map(int,input().split())  #막대라서 4개의 값이 범위를 묶여야됨 
    if (d==0):                           #가로일 경우
        for i in range(l):
           board[x-1][y-1+i] =1          #해당 행부분 1로 변경
    else:
        for i in range(l):
           board[x-1+i][y-1] =1          #해당 열부분 1로 변경

for i in range(h):
    for j in range(w):
        print(board[i][j],end= ' ')
    print()



    

