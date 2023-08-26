messages = ["hi","hello","holla"]
numbers = [1,2,3]

for number,message in zip(numbers,messages):
    print(f"{number}-{message}")