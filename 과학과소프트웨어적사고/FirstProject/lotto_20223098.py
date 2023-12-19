import random

a = ""
b = ""
t = 0
while t < 5:
    cnt = 0
    r = random.randint(1,45)
    if len(str(r)) < 2:
        r = "0" + str(r)
    else:
        r = str(r)
        if a[0:2] != r and a[2:4] != r and a[4:6] !=r  and a[6:8] != r and a[8:10] != r:
            a = r + a
            b = r + " " + b
            t += 1
print(b)
