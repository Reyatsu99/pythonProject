a = "1101"
b = "1010"

# Convert binary strings to integers
a_int = int(a, 2)
b_int = int(b, 2)

# Add the integers
sum_int = a_int + b_int
print(sum_int)

# Convert the sum back to a binary string
sum_str = bin(sum_int)[2:]# [2:] removes the '0b' prefix

print(sum_str) # Output: "10111"
