# list
x = [i**2 for i in range(10)] # create list
_ = x.index(16) # find index of an element
del x[1] # delete element by index
x.remove(9) # delete element by value


# double-ended queue
from collections import deque
d = deque()
d.append(), d.appendleft()
d.pop(), d.popleft()


# priority queue / heap queue
import heapq
heap = list(range(5))
heapq.heapify(heap)
heapq.heappush(heap, item)
heapq.heappop(heap)


# caching
from functools import cache
@cache


# defaultdict
from collections import defaultdict
d = defaultdict(int) # 0
d = defaultdict(list) # []

# argsort
x = [1, 3, 2, 5, 4]
def argsort(a):
    sorted(range(len(a)), key=a.__getitem__)


# read file
with open('file.txt', 'r') as f:
    s = f.read()

# write file
with open('file.txt', 'w') as f:
    f.write(s)


# fibonacci number using Binet's formula
def fib(n):
    phi = (1 + math.sqrt(5)) / 2
    psi = 1 - phi
    return round((phi**n - psi**n) / math.sqrt(5))


# partial
from functools import partial
# the following two are equivalent:
y = f(a, b)
y = partial(f, b)(a)
# this is useful for decorators, eg:
@partial(jax.jit, static_argnums=1)


# flatten list of lists
sum([[1, 2], [3, 4], [5]], []) # = [1, 2, 3, 4, 5]


# namedtuple
from collections import namedtuple
Point = namedtuple("Point", "x y")
point = Point(2, 4)
print(point) # Point(x=2, y=4)

