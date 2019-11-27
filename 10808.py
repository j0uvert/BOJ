inp = list(input())
res = [0]*26

for i in inp:
    res[ord(i) - ord('a')] += 1

for i in range(25):
    print(res[i], end = " ")
print(res[25])
