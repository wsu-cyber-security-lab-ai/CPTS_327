def get_user_profile(user_data):
    """ Access user profile (Null Pointer Dereference) """
    return user_data.get("profile").get("name")   
