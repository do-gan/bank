from atm import Atm
from account import Account

card1 = None

while True:
    print("1. REGISTER YOUR ACCOUNT")
    print("2. FOR CREDIT")
    print("3. FOR DEBIT")
    print("4. TO DISPLAY YOUR DETAILS")
    print("5. STOP")
    
    choice = int(input("\nEnter your option for operation: "))

    if choice == 1:
        bankname = input("\nEnter the bank name: ")
        amount = int(input("\nEnter your amount for registration to bank: "))
        pin = int(input("\nEnter your pin for registration: "))
        
        account = Account(bankname, amount)  # Create an account
        card1 = Atm(account, pin)  # Create an ATM card
        print("\nThanks for registration")

    elif choice == 2:
        if card1 is None:
            print("\nYou need to register first!")
            continue
            
        cr = int(input("Enter the amount for credit: "))
        card1.credit(account, cr)  # Use the 'credit' method of the ATM
        print('\nAfter transaction:', account.getAmount())

    elif choice == 3:
        if card1 is None:
            print("\nYou need to register first!\n")
            continue
            
        dr = int(input("\nEnter the amount for debit: "))
        if card1.debit(account, dr):  # Use the 'debit' method of the ATM
            print('\nAfter transaction:', account.getAmount())
        else:
            print("\nDebit transaction failed.\n")

    elif choice == 4:
        if card1 is None:
            print("\nYou need to register first!")
            continue
            
        print(f"\nThe bank name is {account.getName()} and the amount is {account.getAmount()}.")

    elif choice == 5:
        print("\nThank you for using our service.")
        break

    else:
        print("\nInvalid option. Please try again.")
