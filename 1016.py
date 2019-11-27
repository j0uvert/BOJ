min, max = map(int, input().split())
res = [True] * (max - min + 1)
cnt = 0
num = 1

while num ** 2 <= max:
    num += 1
    sq = num ** 2
    i = min // sq

    while sq * i <= max:
        idx = sq * i - min

        if idx >= 0 and res[idx]:
            cnt += 1
            res[idx] = False
        i += 1

print(len(res) - cnt)