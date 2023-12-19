num_a="1100"
num_b="101"

num_bin_a=[int(x) for x in num_a]
num_bin_b=[int(x) for x in num_b]

if len(num_bin_a) > len(num_bin_b):
    num_bin_b = [0] * (len(num_bin_a) - len(num_bin_b)) + num_bin_b
elif len(num_bin_a) < len(num_bin_b):
    num_bin_a = [0] * (len(num_bin_b) - len(num_bin_a)) + num_bin_a

num_bin = []
bit_index = len(num_bin_a) - 1

while bit_index >= 0:

    bit_a = num_bin_a[bit_index]
    bit_b = num_bin_b[bit_index]

    if bit_a<bit_b :
        sum_=bit_a + 2 - bit_b
        im=bit_index-1

        while im>=0 :
            if num_bin_a[im]==1 :
                num_bin_a[im]-=1
                break
            else:
                num_bin_a[im]+=1
                im-=1

    else:
        sum_ = bit_a - bit_b

    num_bin.insert(0, sum_)
    bit_index -= 1

while num_bin[0]==0 :
    del num_bin[0]

print(f"Binary number = {num_bin}")