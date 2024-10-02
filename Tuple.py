tuple1 = (1,2,3,4,5,6,7)
print(tuple1)
print(len(tuple1))
for i in range(7):
    print(tuple1[i])
print(tuple1[0:3])
print(tuple1[::-1])
tuple2 = ("Aayan", "Tawseef", "Anaya")
print(tuple1 + tuple2)
tuple3 = (1,2,3, ("a", "b", "c"),4,5, ["nested", "tuple"])
print(tuple3[3])
print(tuple3[3][2])
print(tuple3[-1][1])
count = tuple1.count(3)
print(count)
def palind(tuple4):
    x = len(tuple4) - 1
    y = 0
    while y < x:
        if tuple4[y] != tuple4[x]:
            return False
        x -= 1
        y += 1
    return True
tuple4 = (1,2,3,4,5,5,4,3,2,1)
result = palind(tuple4)
if result == True:
    print(f"{tuple4} is a palindrome.")
else:
    print(f"{tuple4} is not a palindrome.")
weather = (1,0,1,0,1,0,1,0,0,1,1,1,1,1,0,0,0)
rainy = 0
sunny = 0
for i in range(len(weather)):
    if weather[i] == 1:
        rainy += 1
    elif weather[i] == 0:
        sunny += 1
if rainy > sunny:
    print("It might rain.")
elif rainy == sunny:
    print("It will be cloudy.")
else:
    print("It will be sunny.")