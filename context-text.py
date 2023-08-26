with open('docs.txt') as file:
    print(file.read())

date = input("Enter Date : ")
mood = input("Mood 1 to 10 : ")
journal = input("let your thoughts :\n ")

with open(f"{date}.txt",'w') as file:
    file.write(mood)
    file.write(journal)

with open("file.txt", 'w') as file:
    file.write("Hello")

with open("file.txt", 'w') as file:
    file.write("Hi")