class User:
    
    first_name = 'Name'
    last_name = 'Surname'
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def print_name(self):
        print('Имя User - ', self.first_name)
    
    def print_surname(self):
        print('Фамилия User - ', self.last_name)
    
    def print_all_name(self):
        print('Имя и Фамилия User - ', self.first_name, self.last_name)