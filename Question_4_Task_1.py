import os
import time

def withdraw_money(user, amount):
    """ Withdraw money from an account after checking balance (TOCTOU Vulnerability) """
    balance_file = f"/tmp/{user}_balance.txt"
    
    
    if os.path.exists(balance_file):
        with open(balance_file, "r") as f:
            balance = int(f.read())
        
    
        time.sleep(2)

        
        if balance >= amount:
            with open(balance_file, "w") as f:
                f.write(str(balance - amount))
            print(f"Success: Withdrawn {amount}, New Balance: {balance - amount}")
        else:
            print("Error: Insufficient balance")
    else:
        print("Error: Balance file not found!")
