def solution(arr):
    answer = [0, 0, 0]
    a = [1, 2, 3]
    num = 0
    for i in a:
        if num < arr.count(i):
            num = arr.count(i)
    for i in a:
        if arr.count(i) < num:
            for j in range(num-arr.count(i)):
                answer[i-1] += 1

    return print(answer)

arr = [3, 3, 3, 3, 3, 3]
solution(arr)