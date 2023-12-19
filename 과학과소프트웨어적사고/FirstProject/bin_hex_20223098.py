num_bin = "101010101101"
print(f"Binary number = {num_bin}")

BIT = 4
num_bin = num_bin[::-1]
num_hex = ""

cnt_bit = 0
while cnt_bit < len(num_bin):
    cnt, sum_ = 0, 0

    while cnt < BIT and cnt_bit < len(num_bin):
        sum_ += 2**cnt * int(num_bin[cnt_bit])
        cnt += 1
        cnt_bit += 1
        if sum_ >= 10:
            sum_ = str(chr(65 + (sum_ - 10)))

    num_hex = str(sum_) + num_hex
print(f"hexadcimal number = {num_hex}")
