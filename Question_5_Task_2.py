@app.route('/profile', methods=['POST'])
def update_profile():
    user = session['user']
    bio = request.form['bio']  
    
    query = f"UPDATE users SET bio='{bio}' WHERE username='{user}'"
    db.execute(query)
    
    return "Profile updated!"
