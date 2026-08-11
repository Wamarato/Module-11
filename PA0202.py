#VERSION 1: range (1 , 6)
total=0

for number in range(1 , 6):   #loop for 1 to 5
    total = total +number
    
print("output with range(1 , 6):", total)

# 1. How many times will the loop execute?
# Answer: 5 times
# Reason: range(1, 6) gives numbers 1, 2, 3, 4, 5

# 2. Which numbers will be added?
# Answer: 1, 2, 3, 4, 5

# 3. What will be the final output?
# Answer: 15
# Reason: 1 + 2 + 3 + 4 + 5 = 15

# 4. What will happen if range(1, 6) is changed to range(1, 10)?
# Answer: The loop will execute 9 times and add numbers 1 to 9
# Final output will be: 45
# Reason: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45


total2 = 0

for number in range(1, 10): # Loop from 1 to 9
    total2 = total2 + number

print("Output with range(1, 10):", total2)    