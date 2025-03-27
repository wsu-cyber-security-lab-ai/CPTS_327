@app.route('/transfer', methods=['POST'])
def transfer_funds():
    recipient = request.form['recipient']
    amount = request.form['amount']
    
    # Directly process transfer without CSRF protection!
    db.execute(f"UPDATE accounts SET balance = balance - {amount} WHERE user='{session['user']}'")
    db.execute(f"UPDATE accounts SET balance = balance + {amount} WHERE user='{recipient}'")
    
    return "Transfer Successful!"
