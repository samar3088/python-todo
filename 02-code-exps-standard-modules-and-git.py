import glob
import csv
import shutil
import webbrowser

text_files = glob.glob("*.txt")
# print(text_files)

for file in text_files:
    print(file)

with open("csv_file.csv",'r') as file:
    data = list(csv.reader(file)) # this csv.reader(file) gives a iterator

city = input("Enter a city : ")
for row in data[1:]:
    if row[0] == city:
        print(row[1])

print(data)

shutil.make_archive('output','zip')

user_input = input("Enter a search term")

webbrowser.open('https://www.google.com/search?q='+user_input)