a = int(input())
b = list(map(int, input()))

print(a*b[2])
print(a*b[1])
print(a*b[0])
print(a*b[2] + 10*a*b[1] + 100*a*b[0])
