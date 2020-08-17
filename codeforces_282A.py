# get n = total number of inputs
total_inputs = int(input())

# Set initial value of x to 0
x = 0

# Check if the input number is within given range
if total_inputs < 1 or total_inputs > 150:
    exit()

# getting input n times, asking for the operator
for i in range(total_inputs):
    operator = input()
    # Increase by 1 if ++ operator
    if operator.lower() == "++x" or operator.lower() == "x++":
        x += 1
    # Decrease by 1 if -- operator
    elif operator.lower() == "--x" or operator.lower() == "x--":
        x -= 1
# Print the result        
print(x)

