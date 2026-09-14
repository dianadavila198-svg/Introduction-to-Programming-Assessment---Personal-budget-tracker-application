#Project 
Personal budget tracker application

##Objective of the program
**This program developed is a console application to help a user track their personal income and expenses. The programme stores transaction data in memory, presents a menu of
options, and provides reports such as financial balances and high level resume by category for expenses.**

## How to start?
**As a pre-requisite to execute this program, you need to have install Python 3 in your machine.**

## Download and execution of the program
**1. Save the main file (budget_tacker.py) in your machine**
2. Open terminal
3. ⁠type python budget_tracker.py 

##Structure of the code
Once the program is executed, it will display the main menu with the below options: 

1. Add Income (Inflow of money)
2. Add Expense (Outflow of money)
3. List Transactions (Total of transactions registered with details such as type, amount, description and category)
4. Delete Transaction (Allows to delete an specific transaction with index input)
5. View Overall Summary (Calculate and display the total balance calculating  (income- expenses))
6. View Summary by Category (Total of expenses grouped by unique category) **this option is available only for expenses
7. Exit (Close of application)

 ##How to use the program
 **Within the display menu please follow the below steps for correct functionality:**

 1. Isert an income selecting option 1.
 2. Insert an expense selecting option 2.
 3. Validate your transactions list selecting option 3. 
 4. Eliminate a transaction selecting option 4. A confirmation message will be display. If you want to double validate that is delete, execute again step 3. 
 5. View Overall summary by selecting option 5.
 6. View summary by category (available only for expenses) by selecting option 6. 
 7. Exit the program selec option 7.  

**This process can be repetead for as many income, expenses and final reports as you wish to execute within the application. 
 
##How this program was tested?
**I constructed the code in the order of the tasks (blocks), by hence is how the code was tested. 
**Once I completed each block I tested with the below one, for example block 1 + 2, etc. 
**After I completed the whole tasks(blocks) development, I tested a few times to validate the correct functionality of all the blocks together. 

Task 2: 
    1.Execute the program and validate the menu was display correctly, without any other actions. 

Task 3: Add_transaction (income and expense)
    1. Added multiple incomes and expenses to the global list, selecting option 1 and 2 of the menu. 

Task 4:list_transactions
    1. Added multiple incomes and expenses to the global list, selecting option 1 and 2 of the menu
    2. Selected the option 3 of the menu "list transaction".
    3. validated the expenses and incomes are being registered properly. 

Task 5: delete_transaction
    1. Added multiple incomes and expenses to the global list, selecting option 1 and 2 of the menu
    2. select option 3 to see list transactions.
    3. Selected option 4 to delete transactions and select the transaction to delete, confirmed the output message confirmation is showing. 
    4. Selected option 3 to see the list updated and validate the transaction has been deleted. 

Task 6 part 1 print_overall_summary:
1. Added multiple incomes and expenses to the global list, selecting option 1 and 2 of the menu.
2. Selected option 5 view overall summary and validate the output was showing correctly 

Task 6 part 2 print_summary_by_category:
    Escenario (expenses)
    1. I added a couple of expense items with option 1 and 2 of the menu, including different categories of products. 
    2. Selected option 6 view summary by category.
    3. validated that for expenses it was showing properly the summary by each category.

    Escenario (incomes)
    1. I added an additional message in the case of incomes, as this function is not available for incomes as part of the assessment requierements. 
    2. Once I add this additional print I validated it was printing properly in the case that the user don´t have any expenses and only incomes. 

**Menu display program handles invalid inputs such as str or higher number than 7 (as 7 is the last option available within the menu.)**
**Additional transaction 2,4 & 7 have a second round of validation to handle invalid inputs, such as str, negative or cero. And showing a message about inserting a valid number.**  
**The below mentioned, I tested for all the task inserting an invalida ammount (str, higher than 7, cero and negative number) to validate the "invalid input..." printing was showing correctly.

##Assumptions 
Task 6 bullet 2 (summary by category) the function is available only by expense type, as is the scope mentioned in the assessment. However I consider a resume by category for incomes might be needed for a better functionality. 

##Additional notes
**Task 6 bullet 3 (summary by category) the code for this task was implemented completely by myself. However, I would like to recognize that received guidance from a classmate on the method for accessing to the unique category values.**

## Author
**Diana Laura Davila Esparza 

 