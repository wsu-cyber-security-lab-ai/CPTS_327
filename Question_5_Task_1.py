@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    
    result = db.execute(query)   
    
    if result.fetchone():
        return "Login Successful!"
    else:
        return "Invalid credentials"
