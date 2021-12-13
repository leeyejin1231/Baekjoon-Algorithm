score = [int(input()) for _ in range(5)]

sum=0
for i in score:
    if i < 40:
        sum += 40
    else:
        sum += i
print(sum//5)