try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    calculate = value/total_value * 100
    print(f"That is {calculate}%")
except ValueError:
    print('Please enter number')
except ZeroDivisionError:
    print('Please enter number greater than 0')


colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    if color > 50:
        print(color)