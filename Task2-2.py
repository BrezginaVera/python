a = [int(i) for i in input().split()]
b = len(a)
i = 0
while i <= (b-2):
    a[i], a[i+1] = a[i+1], a[i]
    i=i+2
print(a)

