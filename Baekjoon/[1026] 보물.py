'''
백준 1026번
https://www.acmicpc.net/problem/1026
'''
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

################## 방법 1
index_list = []
result = [0]*len(a)

a_sort=sorted(a)

# [(value, index), ...]
for i, v in enumerate(b):
    index_list.append((v,i))

# index_list에서 최대값을 찾고, a_sort 에서 해당 값을 찾아 재배열
for _ in range(N):
    max_num = max(index_list)
    index_list.pop(index_list.index(max_num))
    result[max_num[1]] = a_sort.pop(0)
    
# a_sort, result index별 곱 리스트
product = [x*y for x,y in zip(result,b)]
print(sum(product))

################## 방법 2: a - 오름차순 정렬 / b - 역순 정렬 뒤 계산
result2 = 0
a.sort()
b.sort(reverse = True)
for i in range(N):
    result2 += a[i] * b[i]
print(result2)
