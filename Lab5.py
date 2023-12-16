import random

# Step 2
number = int(input('Enter a number: '))

# Step 3, 4, 5
if number % 3 == 0 and number % 5 == 0:
    print(number, 'Tic Tac')
elif number % 3 == 0:
    print(number, 'Tic')
elif number % 5 == 0:
    print(number, 'Tac')

# Step 6
count = 1
while count <= 20:
    print(count)
    count += 1

# Step 7
count = 1
while count <= 20:
    if count % 3 == 0 and count % 5 == 0:
        print(count, 'Tic Tac')
    elif count % 3 == 0:
        print(count, 'Tic')
    elif count % 5 == 0:
        print(count, 'Tac')
    count += 1

# Step 8
random_number = random.randint(1, 10)
print('Random Number:', random_number)

# Step 9
attempts = 0
while attempts < 5:
    user_value = int(input('Enter a value greater than 0: '))
    if user_value > 0:
        break
    else:
        print('Value must be greater than 0. Try again.')
    attempts += 1

# Step 10
random_generated = random.randint(1, 10)
if user_value == random_generated:
    print('Perfect Match!')
else:
    print('Numbers do not match. User Value:', user_value, 'Random Generated:', random_generated)
