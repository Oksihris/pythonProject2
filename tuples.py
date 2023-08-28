import sys
import timeit

mytuple=("NAVC", 55,True, "Cris")
print(mytuple)

mytuple1= tuple(["Clare", "Sting", 18, 'j', 'j'])
print(mytuple1[-2])

for i in mytuple:
    print(i)

if 18 in mytuple1:
    print("Yes")
else:
    print("No")

print(mytuple1.count('j'))


a = (1,2,3,4,5,6,7,8,9,19)

b = a[3:8]
print(b)

tup= "Ksu", 19, 44

name, *age = tup

print(name)
print(age)

myylist2 = [1,2,3,4,5]
myytuple2 = (1,2,3,4,5)

print(sys.getsizeof(myylist2),"bytes")
print(sys.getsizeof(myytuple2),"bytes")

print(timeit.timeit(stmt="[1,2,3,4,5,6]", number=1000000))
print(timeit.timeit(stmt="(1,2,3,4,5,6)", number=1000000))