positions = [1,2, 5,6, 9,12, 14,  15, 17, 19, 23, 24, 26, 27, 29]
# positions = [1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1]
syndrome = 0
for pos in positions:
    syndrome ^= pos
print(syndrome)