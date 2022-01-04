'''
백준 2941번
https://www.acmicpc.net/problem/2941
'''

alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in alphabet:
    word = word.replace(i, '*')

print(len(word))