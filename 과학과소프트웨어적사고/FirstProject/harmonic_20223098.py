import math
sum_ = 0
for i in range(1, 101):
    sum_ += 1/i
print(sum_)

n = 100
k = math.log(n+1)
print(k)

print((k - sum_)/sum_)