month = int(input("Month: "))
winter = [12,1,2]
spring = [3,4,5]
summer = [6,7,8]
autumn = [9,10,11]
if month in winter:
    print("Winter")
elif month in spring:
    print("Spring")
elif month in summer:
    print("Summer")
else:
    print("Autumn")
