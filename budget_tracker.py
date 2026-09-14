#Personal budget tracker application

#Initialization of global list for transactions
transactions = []

#Store menu to display
def display_menu ():
    print ("--- Personal Budget Tracker ---")
    print ("1. Add Income")
    print ("2. Add Expense")
    print ("3. List Transactions")
    print ("4. Delete Transaction")
    print ("5. View Overall Summary")
    print ("6. View Summary by Category")
    print ("7. Exit")

#Creation of a single reusable function to add transactions that include a category
#current transactions (list to modify) and transaction type (income/expense) will be the 2 main parameters
def add_transaction (current_transactions, transaction_type):
   description = input ("Enter a description:")
   category = input ("Enter a category:")
   #capture errors converting the input of the amount to float
   try:
        amount = input("Enter expense amount:")
        amount = float (amount)
        if amount > 0: 
             #Store the transaction as dictionary in the global list
            current_transactions.append ({
                "type": transaction_type,
                "amount": amount, 
                "description" : description, 
                "category": category
                })
            print ("Thank you, transaction added successfully")
        #Handle invalid amounts (negative or cero)   
        else:
            print("Invalid amount. Please enter a positive number")
            return
   except ValueError:
       print ("Invalid amount. Please enter a positive number")
       return 

#display all recorded transactions
def list_transactions (transactions):
    if not transactions:
        print ("No transactions found")
    else:
        #Count of transactions according to their position
        print ("---All transactions---")
        for index, transaction in enumerate (transactions,1):
            print (f"{index} {transaction['type']} - £{transaction['amount']:.2f} - {transaction['description']} - {transaction['category']}")

#Function that allow user to remove a specific transaction
def delete_transaction (transactions):
    #handles scenario where there are non existent transactions
    if not transactions: 
        print ("You have no transactions yet, please select a transaction first before proceeding")
        return
    #Display list for user to select transaction to delete 
    list_transactions(transactions)
    transaction_to_delete = input ("Enter the transaction to be deleted")
    #Attempts to convert input to int and handle non-numeric/out-of-range numbers with error messages
    try:
        transaction_to_delete = int (transaction_to_delete) -1 #rest one, as positions start from 0
        if transaction_to_delete >= 0 and transaction_to_delete < (len(transactions)):
           delete_item= transactions.pop(transaction_to_delete) #list.pop to remove item by index
           print (f"{delete_item['description']} was deleted sucessfully")
        else: 
            print ("invalid input. Please enter a number between 1 and 6")      
    except ValueError:
        print ("Invalid input. Please enter a number")

#financial summaries
#Function that computes total income, total expenses, and net balance
def calculate_summary(transactions):
    total_income = 0.0
    total_expenses = 0.0
    #loop function to iterate in expense or income type of transaction in the global list 
    for transaction in transactions:
        if transaction ['type']== "Income":
            total_income = total_income + transaction ['amount']
        elif transaction ['type'] == "Expense":
             total_expenses = total_expenses + transaction ['amount']
    total_balance = total_income - total_expenses
    #return of dictionary with calculated values
    return ({
        "total income" : total_income, 
        "total expenses": total_expenses, 
        "total balance" : total_balance 
        })
#Report using values returned by calculate_summary
def print_overall_summary(summary_data):
        #function to access dictionary store variables 
        income = summary_data['total income']
        expense = summary_data['total expenses']
        total = summary_data['total balance']
        print ("---Overall Summary---\n")
        print (f"Total Income: £{income:.2f}")
        print (f"Total expense: £{expense:.2f}")
        print (f"Total net balance: £{total:.2f}")


def print_summary_by_category (transactions):
    #initialize empty dictionary to store transactions
    category_sum= {}
    for transaction in transactions:
        if transaction ['type']== "Expense":
            category_name = transaction['category']
            amount = transaction['amount']
            if category_name in category_sum: 
                category_sum[category_name] += amount #sums to existing category item
            else: 
                category_sum[category_name] = amount #create new category item for summarizing
            #ignore income transactions as stated the task, this is only for expenses    
                print ("---Expenses by Category---")
        else: 
            print ("This transaction is available only for expenses")
    #loop to iterate in each category item
    for name, total in category_sum.items():
        print (f"{name}: £{total:.2f}")

#Main loop to take users input for menu selection and handle input errors
while True: 
    display_menu()
    menu_chosed =input ("Please the number of the option in the menu you would like:")
    #Conversion to number, to avoid str inputs 
    try:
        menu_chosed = int (menu_chosed)
    #function to handle income or expense category
        if menu_chosed == 1:
            add_transaction(transactions, "Income")
        elif menu_chosed == 2:
            add_transaction(transactions, "Expense")
        #function to handle option 3 of menu, list transactions    
        elif menu_chosed == 3:
            list_transactions(transactions)
        #function to handle delete transactions    
        elif menu_chosed == 4:
            delete_transaction(transactions)
        #function to show summary data    
        elif menu_chosed == 5:
            summary_data = calculate_summary(transactions)
            print_overall_summary(summary_data)
        #function to show items by category    
        elif menu_chosed == 6:
            print_summary_by_category (transactions)
        elif menu_chosed == 7:
            break 
        else:
            print ("Function not available yet")
    except ValueError:
        print ("Invalid input. Please enter a number")

