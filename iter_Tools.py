# product
from itertools import product

a =[1,2]
b=[3,4]

prod= product(a,b, repeat=2)
print(prod)
print(list(prod))

# permutations
from itertools import permutations
c=[4,7,9, 8]

perm = permutations(c, 2)
print(list(perm))

# combinations
from itertools import combinations, combinations_with_replacement
comb=combinations(c,2)
print(list(comb))

comb_wr =combinations_with_replacement(c,2)
print(list(comb_wr))

# accumulate
from itertools import accumulate
import operator
acc= accumulate(c, func = operator.mul)
print(list(acc))

# groupby
# def smaller_than_8(x):
#     return x<8

from itertools import groupby

group_obj=groupby(c, key=lambda x: x<8)
for k, v in group_obj:
    print(k,list(v))


from itertools import count, cycle, repeat
aa =[1,2,3]
# for i in cycle(a):
#     print(i)

for i in repeat(1, 5):
    print(i)


for i in count(10):
    print(i)
    if i ==16:
        break

