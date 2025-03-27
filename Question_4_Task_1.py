import os
import time

def withdraw_money(user, amount):
    """ Withdraw money from an account after checking balance (TOCTOU Vulnerability) """
    balance_file = f"/tmp/{user}_balance.txt"
    
    # Time-of-Check: Read balance
    if os.path.exists(balance_file):
        with open(balance_file, "r") as f:
            balance = int(f.read())
        
        # Simulating delay (an attacker can modify balance here)
        time.sleep(2)

        # Time-of-Use: Write new balance
        if balance >= amount:
            with open(balance_file, "w") as f:
                f.write(str(balance - amount))
            print(f"Success: Withdrawn {amount}, New Balance: {balance - amount}")
        else:
            print("Error: Insufficient balance")
    else:
        print("Error: Balance file not found!")
