from datetime import datetime 

balance = 1000
transaction_history = []

def transactions(type, amount, receiver=None):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if receiver:
        transaction = f"{time} - {type} of RS {amount} to account {receiver}"
    else:
        transaction = f"{time} - {type} of RS {amount}"
    transaction_history.append(transaction)
def send_money():
    global balance
    time = datetime.now()
    receiver = int(input("Enter the account number to whom you want to transfer money: "))
    amount = int(input("Enter the amount: "))
    if amount > 0 and amount <= balance:
        balance -= amount
        transactions("Transfered", amount, receiver)
        print("Amount RS  {amount} sent successfully \n to ",  receiver, "on", time ,"\n your available balance amount is: " , balance )
    else:
        print(35*"-")
        print(8*" ", "Insufficient Funds")
        print(35*"-")

def deposit():
    global balance
    amount_deposited = int(input("Enter Amount: "))
    new_balance = balance + amount_deposited 
    if amount_deposited > 0:
        balance += amount_deposited
        transactions("Deposited", amount_deposited )
        print("Amount RS {amount_deposited} deposited successfully \n your available balance is ", balance )
    else:
        print("Please enter valid amount")

def withdraw_cash():
    global balance
    time = datetime.now()
    user = int(input("enter yor card number: "))
    amount= int(input("Enter amount: "))
    if amount > 0 and amount <= balance:
        balance -= amount
        transactions("Withdrawn", amount)
        print("Amount RS/-",  amount, " Withdrawn successfully from agency \n your available balance is ", balance )
    
    else:
        print("Sorry you don't enough money in your account")    

def check_balance():
    global balance
    print("Available balance in your account is: ", balance )
    if transactions:
        print("Transaction History: ")
        for trans in transaction_history:
            print(trans) 
    else:
        print("No transactions found")        

def pay_bills():
    global balance
    time = datetime.now()
    paybill =  int(input("Enter the bill number: "))
    amount = int(input("Enter amount: "))
    if amount >0 and amount < balance:
        balance -= amount
        print("RS ", amount, "paid to ", paybill, "on" , time, ".Your available balance is: ", balance )
    else:
        print("You dont have enough money to pay the bill.")     



while True:
    print(10*"-"," Welcome!!!",  10*"-",  "\n Have a happy and safe money transfer ")
    print("1.Send Money")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Check Balance")
    print("5.Pay Bills")
    
    by_user = int(input("Choose any one option: "))
    if by_user == 1 :
        send_money()
    elif by_user == 2:
        deposit() 
    elif by_user == 3:
        withdraw_cash()
    elif by_user == 4:
        check_balance() 
    elif by_user == 5:
        pay_bills()
    else :
        print("please enter valid option")                  

    