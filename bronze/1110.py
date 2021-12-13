N = int(input())
res = 0
num = 0
b = N%10
if N < 10:
    a = 0
else:
    a = N//10

if N == 0:
    num += 1

while(res != N):
    res = (a+b)%10 + b*10
    b = res%10
    if res < 10:
        a = 0
    else:
        a = res//10
    num += 1;

print(num)