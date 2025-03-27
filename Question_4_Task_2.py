def authenticate(username, password):
    """ Authenticate user (Unchecked Return Value) """
    user_db = {"alice": "password123", "bob": "qwerty"}
    
    if username in user_db and user_db[username] == password:
        return True  # Authentication successful
    else:
        print("Authentication failed")   

def transfer_funds(user, recipient, amount):
    """ Transfer funds only if user is authenticated """
    if authenticate(user, "wrongpassword"):  # Authentication failure 
        print(f"Transferring {amount} to {recipient}")
    else:
        print("Unauthorized transaction!")
