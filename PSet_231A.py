# Get number of problems
number_problems = int(input())
# Variable to store the number of problems the kids can implement
# Initial value is 0
impl_problems = 0

if (number_problems >= 1) and (number_problems <= 1000):
    # Iterate n times to get 3 sure (1) or unsure (0) for every problem
    for i in range(number_problems):
        # Get three inputs in one line, separated by space
        num1, num2, num3 = input().split()
        # Convert input from initial str type into int type
        is_sure1, is_sure2, is_sure3 = int(num1), int(num2), int(num3)
        # Make sure the input values are only 1 or 0
        if (is_sure1 == 0 or is_sure1 == 1) and (is_sure2 == 0 or is_sure2 == 1) and (is_sure3 == 0 or is_sure3 == 1):
            # Sum of1 (sure) and 0 (not sure) and
            # Check if the sum is equal to or greater than 2
            if is_sure1 + is_sure2 + is_sure3 >= 2:
                # If True, increase implemented problems counter by 1
                impl_problems += 1
# Print result
print(impl_problems)
