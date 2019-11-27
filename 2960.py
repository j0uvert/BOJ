n, k = map(int, input().split())

ll = list(range(n+1))   # ll: [0, 1, 2, 3, 4, ... , n]
deleted = []
ll[0] = -1
ll[1] = -1  ## ll : [-1, -1, 2, 3, 4, ... , n]

cnt = 0
while cnt < k:
    for i in range(n+1):
        if ll[i] != -1:
            j = i
            while j < n+1:
                if ll[j] != -1:
                    deleted.append(ll[j])
                    ll[j] = -1
                    cnt += 1
                j += i

print(deleted[k-1])
