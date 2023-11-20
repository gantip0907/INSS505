# Step 1: Use a for loop to ask users to enter 10 numbers

for num in range(10):
    user_input = int(input("Enter number: "))

# Step 2: An if statement to determine whether each number is even or odd

    if user_input % 2 == 0:
        print(user_input, " is even.")
    else:
        print(user_input, " is odd.")

