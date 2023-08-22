# myset={1,2,3, 1 ,4}
# print(myset)

# myset.add(0)
# myset.remove(3)

# print(myset)
# myset.discard(5)

# myset1=set("Hello")
# print(myset1)

# for i in myset:
#     print(i)

# if 1 in myset:
#     print("yes")

odds={1,3,5,7,9}
evens={0,2,4,6,8}
primes={2,3,5,7, 8}

u = odds.union(evens)
print("Union", u)

i = odds.intersection(primes)
print("Intersection",i)

diff = primes.difference(evens)
print("Difference", diff)

s_diff = primes.symmetric_difference(evens)
print("Symmetric Difference", s_diff)

i.update(u)
print(i)

u.intersection_update(evens)
print(u)

i.difference_update(u)
print(i)

setB=i.copy()
print(setB)


a = frozenset([1,2,3,4])
# a.add(2)
print(a)