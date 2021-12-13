# h=list(map(int,open(0)))
h=list(map(int, input()) for _ in range(5))
print(min(h[:3])+min(h[3:])-50)