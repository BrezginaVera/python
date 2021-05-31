a = int(input("Первый день: "))
b = int(input("Нужно пробежать не менее: "))
t=1
i=0.1
s=a
while s<=b:
    s=s+s*i
    t=t+1
print(t)
