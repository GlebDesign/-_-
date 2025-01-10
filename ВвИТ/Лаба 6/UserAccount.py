class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password): #изменить пароль 
        if self.__password == new_password:
            raise TypeError('пароль не должен совпадать со старым ')
        else:
            self.__password = new_password
        return self.__password
     
    def check_password(self, password):
        return True if password == self.__password else False
    
    def info(self):
        print('\n',self.username,'\n', self.email,'\n', self.__password)
    


user = UserAccount("Gleb", "gleb1245@gmail.com", 1234)
# user.info()
# print(user.check_password(124))
print(user.set_password(1245))
print(user.password)
    