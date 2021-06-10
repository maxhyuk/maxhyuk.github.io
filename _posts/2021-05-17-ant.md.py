board=[]

for i in range(10):
    board.append(list(map(int,input().split())))  #입력

x, y = 1, 1

board[x][y]=9                   
 
while True:
    if(board[x][y]==2):                           # 좌표가 2면 9로바꾸고 스탑 = 먹이를 먹음
        board[x][y]=9                             # 다음으로 넘어가 만약 y축으로 한칸 옮기고 
        break                                     # 1이 아닐 경우 9로 바꾸고 y+1
    if(board[x][y+1]!=1):                         # 2와 1 둘다 아닐 경우 x축으로 이동 1이 아닐경우
        board[x][y]=9                             # x축 +1
        y+=1                                      # 계속 진행하다보면 먹이를 먹고 9로 바꿔 스탑 
    else:                            
        if(board[x+1][y]!=1):
            board[x][y]=9
            x+=1
        else:
          board[x][y]=9
          break


for i in range(10):
    for j in range(10):
        print(board[i][j], end=' ')              #출력
    print()
