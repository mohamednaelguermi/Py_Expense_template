from PyInquirer import prompt
import csv

expense_questions = [
    {
        "type": "input",
        "name": "amount",
        "message": "New Expense - Amount: ",
    },
    {
        "type": "input",
        "name": "label",
        "message": "New Expense - Label: ",
    },
    {
        "type": "confirm",
        "name": "split_expense",
        "message": "Do you want to split this expense ?",
        "default": False,
    }
]

def load_users():
    users = []
    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # Ensure the row is not empty
                users.append(row[0])
    return users

def new_expense(*args):
    
    users = load_users()
    user_question = {
        "type": "list",
        "name": "spender",
        "message": "Select the user who spent this amount:",
        "choices": users,
    }

    user_info = prompt(user_question)

    # Demander les détails de la dépense
    expense_info = prompt(expense_questions)

    if expense_info['split_expense']:
        # CheckBox 
        involved_question = {
            "type": "checkbox",
            "name": "involved_users",
            "message": "Select users involved in the expense:",
            "choices": [{'name': user, 'checked': True if user == user_info['spender'] else False} for user in users],
        }

        involved_info = prompt(involved_question)
        amount_per_user = float(expense_info['amount']) / len(involved_info['involved_users'])

        with open('expense_report.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            for user in involved_info['involved_users']:
                writer.writerow([amount_per_user, expense_info['label'], user])

    print("Expense Added!")
    return True

