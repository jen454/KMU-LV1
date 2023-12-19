BASE = 16
num_dec = int(input())
print(f"Decimal number = {num_dec}")

num_hex = ""

if num_dec < BASE:
    if num_dec >= 10:
        num_hex = str(chr(65+(num_dec - 10)))
    num_hex = num_dec

else:
    while num_dec > 0:
        num_dec, r = num_dec // BASE, num_dec % BASE
        if r >= 10:
            r = str(chr(65+(r - 10)))
        num_hex = str(r) + num_hex

print(f"hexadecimal number = {num_hex}")