class SpamDetector:
    def __init__(self):
        self.blacklist = ['spam@gmail.com', 'xyz@gmail.com','fraud@gmail.com','fake@yahoo.com']
    def search(self,email):
        if email in self.blacklist:
            print("Spam email detected.")
        else:
            print("Secure email.")

sd = SpamDetector()
sd.search('user@gmail.com')
sd.search('fake@yahoo.com')