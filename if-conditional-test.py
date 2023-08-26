password = input("Enter your password")

if len(password) > 7:
    print('Great password there')
elif len(password) == 7:
    print('Password is OK, but not too strong.')
else:
    print('Your password is weak')

day_temperatures = {'morning': '10.o','noon': '10.0','evening': '10.0'}

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[4:7])