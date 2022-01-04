'''
백준 1485번
https://www.acmicpc.net/problem/1485
'''

import sys

T = int(sys.stdin.readline())
x = [0]*4
y = [0]*4

# T번만큼 반족
for _ in range(T):

    # x, y 좌표 입력
    # dot=[list(map(int,line().split())) for _ in range(4)] 와 같이도 가능 (2차원 리스트)
    for i in range(4):
        x[i], y[i] = map(int, sys.stdin.readline().split())

    n_list=list()
    
    # 좌표가 중복되지 않도록 하여 각 변 / 대각선의 길이 구함
    for i in range(3):
        for j in range(i+1, 4):
           n_list.append( (x[i] - x[j])**2 + (y[i] - y[j])**2 )

    n_list.sort()

    # 변의 길이가 모두 같고, 대각선 길이 또한 같으면 정사각형
    if n_list[0] == n_list[1] and n_list[0] == n_list[2] and n_list[0] == n_list[3] and n_list[4] == n_list[5]:
        print(1)
    else:
        print(0)


'''
Example
2
1 1
1 2
2 1
2 2
2 2
3 3
4 4
5 5
'''