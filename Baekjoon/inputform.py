import sys

# 한 줄의 문자열을 입력
input()

# map(): 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용
# 공백을 기준으로 구분된 데이터를 입력 받을 때
data = list(map(int, input().split()))

# 공백을 기준으로 구분된 데이터가 많지 않다면
a,b,c = map(int, input().split())

# sys.stdin.readline(): 입력 속도 향상, 한 줄 단위 입력(개행문자, 엔터 제거, str으로 저장되므로 형변환 필요)
# 공백으로 구분된 2개 숫자 입력 받기
N, M = map(int, sys.stdin.readline().split())

# 2차원 리스트 입력 받기
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 문자열 입력 받기
data = sys.stdin.readline().strip()

# 문자열 n줄 입력받아 리스트 저장
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]

