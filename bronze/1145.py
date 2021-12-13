numbers = str(input())
arr = numbers.split(" ")
num = 1

while(1):
    c = 0
    for i in range(5):
        arrr = int(arr[i])
        if num%arrr == 0:
            c += 1
        if c == 3:
            print(num)
            exit(0)
    num += 1
