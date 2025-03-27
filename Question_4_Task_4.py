class Session:
    """ User session handling with a Use-After-Free vulnerability """
    def __init__(self, user):
        self.user = user
        self.active = True

    def logout(self):
        """ Log out and free session memory """
        self.active = False
        del self.user   

    def get_username(self):
        """ Get username (Use-After-Free Vulnerability) """
        return self.user  

 
session = Session("alice")
session.logout()
print(session.get_username())   
