count = 1
total = 0

# BUG: The while statement was missing a colon at the end.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: The original condition used < 5, which stopped at 4.
# BUG: total is an integer, so it cannot be concatenated directly to a string. An f-string fixes this.
print(f"Sum of 1 to 5 is: {total}")
