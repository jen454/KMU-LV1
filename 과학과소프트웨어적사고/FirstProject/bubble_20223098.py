import time
import random
import copy

low = 1
high = 1000
iter = 1000
a = []

for i in range(iter):
    a.append(random.randint(low, high))

b = copy.deepcopy(a)

start = time.time()
a.sort()
print(a)
end = time.time()
print("Running sort(%d) takes %s" % (iter, end-start))

start = time.time()
for i in range(iter):
    for j in range(0, iter - i - 1):
        if b[j] > b[j+1]:
            b[j], b[j+1] = b[j+1], b[j]
print(b)
end = time.time()
print("Running sort(%d) takes %s" % (iter, end-start))

            