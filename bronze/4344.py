def average(list):
    cnt = 0
    n = list[0]
    del list[0]
    avg = sum(list)/n
    for i in list:
        if i>avg:
            cnt += 1
    print("{:.3f}%".format(cnt/n*100))

c = int(input())
list = [list(map(int, input().split())) for _ in range(c)]
for i in range(c):
    average(list[i])