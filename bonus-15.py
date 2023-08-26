import json

with open('bonus-15.json','r') as file:
    content = file.read()

data = json.loads(content)

score = 0
for question in data:
    print(question['question_text'])
    for index,alternative in enumerate(question['alternatives']):
        print(f"{index+1}-{alternative}")
    user_choice = int(input("What is the correct answer : "))
    question['user_choice'] = user_choice
    if user_choice == question['correct_answer']:
        score = score + 1

for question in data:
    message = f"Your answer: {question['user_choice']}, Correct answer {question['correct_answer']}"

    print(message)