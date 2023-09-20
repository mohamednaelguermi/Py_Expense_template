from PyInquirer import prompt
import csv

user_questions = [
    {
        "type": "input",
        "name": "name",
        "message": "Please enter your name: ",
    }
]

def add_user():
    user_info = prompt(user_questions)
    user_name = user_info['name']

    with open('users.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user_name])  # Wrap user_name in a list

    print("User Added!")
    return True
