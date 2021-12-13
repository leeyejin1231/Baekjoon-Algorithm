week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
x, y = map(int, input().split())
day = 0

for i in range(1, x):
    if i == 4 or i == 6 or i == 9 or i == 11:
        day += 30
    elif i == 2:
        day += 28
    else:
        day += 31

print(week[(day+y)%7])