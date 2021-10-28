import psycopg2
import password_generator as pg
from secret import DB_PASSWORD
from psycopg2.errors import UniqueViolation

class Password_manager():
    
    def __init__(self):
        self.connection = psycopg2.connect(user='szymon',
                                        password=DB_PASSWORD,  
                                        host='127.0.0.1',
                                        port='5432',
                                        database='password_manager')
        self.cursor = self.connection.cursor()
          

    def store_data(self, user, password, email, link, app_name):
        """Store data to DB"""
        postgres_insert_query = """ INSERT INTO accounts(password,email,username, 
                                url, app_name) VALUES (%s,%s,%s,%s,%s)"""
        record_to_insert = (password,email,user,link,app_name)
        self.cursor.execute(postgres_insert_query, record_to_insert)
        self.connection.commit()
        count = self.cursor.rowcount
        print(count, 'record inserted!')
        

    def store_existing_account(self):
        """ Method store existing account to DB"""
        app_name = input('Enter application name: ').lower()
        email = input('Address email for this account: ')
        user = input('Enter username(if needed): ')
        if user is None:
            user = ''
        
        password = input('Enter password: ')
        link = input('Enter website link: ')

        try:
            self.store_data(user, password, email, link, app_name)
        except UniqueViolation:
            print('ERROR:Account for this email and application have already exist')

    def generate_password(self):
        """Generating new password to the account"""
        app_name = input('Enter application name: ').lower()
        email = input('Address email for this account: ')
        plaintext = input('Enter easy password for this site: ')
        user = input('Enter username(if needed): ')
        if user is None:
            user = ''

        link = input('Enter website link: ')

        question = input('Do you want enter password length? Default and minimum is 10 (y/n)')
        if question == 'y':
            length = int(input('Enter length: '))

        if question == 'n' or length <= 10:
            length = 10

        password = pg.password(plaintext,app_name,length)
        try:
            self.store_data(user, password, email, link, app_name)
           
            print('Your password for this account is ' + password)
        except UniqueViolation:
            print('ERROR:Account for this email and application have already exist')


    def find_password(self):
        """Find appropriate password to the account"""
        app_name = input('Enter application name: ').lower()
        email = input('Address email for this account: ')

        postgres_select_query = """SELECT password FROM accounts WHERE app_name='"""+app_name+"'"+ "AND email='"+email+"'"
        self.cursor.execute(postgres_select_query, app_name)
        self.connection.commit()
        result = self.cursor.fetchone()
        if result is None:
            print("There is not data in DB with entered parameters")
        else:
            print("This is your password for this account: " + result[0])
    
    def find_accounts(self):
        """Find accounts to connected email"""
        data = ('Password','Email','User','Link','App')
        email = input('Address email for this account: ')

        postgres_select_query = "SELECT * FROM accounts WHERE email='"+email+"'"
        self.cursor.execute(postgres_select_query, email)
        self.connection.commit()
        result = self.cursor.fetchall()
        if result is None:
            print("Email you entered is not in DB")
        for _,row in enumerate(result):
            for i, var in enumerate(row):
                print(data[i] +': ' + var,)
            print('##'*13)
    
    def change_password(self):
        """Change password to the account"""
        app_name = input('Enter application name: ').lower()
        email = input('Address email for this account: ')
        plaintext = input('Enter easy password for this site: ')
        new_password = pg.password(plaintext,app_name,10)
        sure = input('Are you sure of changing the password? y/n ')
        if sure == 'y':
            postgres_select_query = "UPDATE accounts SET password='"+new_password+"' WHERE email='"+email+"'AND app_name='"+app_name+"'"
            self.cursor.execute(postgres_select_query, (new_password,email,app_name))
            self.connection.commit()
            print('Your new password is:' + new_password)
        
        else:
            return
    
    def delete_account(self):
        """Drop account from DB"""
        app_name = input('Enter application name: ').lower()
        email = input('Address email for this account: ').lower()
        sure = input('Are you sure of changing the password? y/n ')

        if sure == 'y':
            postgres_select_query = "DELETE FROM accounts  WHERE email='"+email+"'AND app_name='"+app_name+"'"
            self.cursor.execute(postgres_select_query, (email,app_name))
            self.connection.commit()
            print('Account deleted properly from DB ')
        
        else:
            return

