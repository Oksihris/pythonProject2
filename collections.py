# Counter

from collections import Counter

a="aaaaaabbbbccccc"
my_counter= Counter(a)
print(my_counter)

print(my_counter.most_common(1)[0][0])

print(list(my_counter.elements()))

# namedtuple

from collections import namedtuple

Point = namedtuple('Point', 'x,y')

pt = Point(1,-4)
print(pt)


# OrderedDict
from collections import OrderedDict

ordered_dict = OrderedDict()

ordered_dict['b']=2
ordered_dict['c']=3
ordered_dict['d']=4
ordered_dict['a']=1

print(ordered_dict)

# defaultdict
from collections import defaultdict

dif_dict = defaultdict(list)
dif_dict['b']=2
dif_dict['a']=1
dif_dict['c']=3
print(dif_dict['g'])

# deque
from collections import deque
d = deque()
d.append(1)
d.append(2)

d.appendleft(5)
print(d)
d.pop()
d.extend([7,8,9])
d.rotate(-1)
print(d)
