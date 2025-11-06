"""
### Task 02 - ATM Withdrawal System

- Ask the user for their account balance and the amount they want to withdraw.
  - If the withdrawal amount is greater than the balance → print "`Insufficient Balance`"
  - If the withdrawal amount is less than or equal to balance → print "`Transaction Successful`" and show the remaining balance.
"""

balance_amount = int(input("Enter account balance: "))
withdraw_amount = int(input("Enter withdraw amount: "))
remaining_amount = 0

if withdraw_amount>balance_amount:
    print("Insufficient Balance")
elif withdraw_amount<=balance_amount:
    print("Transaction Successful")
    remaining_amount = balance_amount - withdraw_amount
    print(f"Remaining Balance: {remaining_amount}")
