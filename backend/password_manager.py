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

    def generate_password(self,app_name, email, plaintext, user, link,length):
        """Generating new password to the account"""
       
        password = pg.password(plaintext,app_name,length)
        
        self.store_data(user, password, email, link, app_name)

        return password
           
       
    def find_password(self, app_name, email):
        """Find appropriate password to the account"""

        postgres_select_query = """SELECT password FROM accounts WHERE app_name='"""+app_name+"'"+ "AND email='"+email+"'"
        self.cursor.execute(postgres_select_query, app_name)
        self.connection.commit()
        result = self.cursor.fetchone()
        if result is None:
            print("There is not data in DB with entered parameters")
        else:
            print("This is your password for this account: " + result[0])
    
        return result
    
    def xd(self):
        return 'xd'
    def find_accounts(self, email):
        """Find accounts to connected email"""

        postgres_select_query = "SELECT * FROM accounts WHERE email='"+email+"'"
        self.cursor.execute(postgres_select_query, email)
        self.connection.commit()
        result = self.cursor.fetchall()
        
        return result
        
    def change_password(self, app_name, email, plaintext):
        """Change password to the account"""
        
        
        new_password = pg.password(plaintext,app_name,10)
        postgres_select_query = "UPDATE accounts SET password='"+new_password+"' WHERE email='"+email+"'AND app_name='"+app_name+"'"
        self.cursor.execute(postgres_select_query, (new_password,email,app_name))
        self.connection.commit()

        return new_password
            
    def delete_account(self,app_name, email):
        """Drop account from DB"""
      
        postgres_select_query = "DELETE FROM accounts  WHERE email='"+email+"'AND app_name='"+app_name+"'"
        self.cursor.execute(postgres_select_query, (email,app_name))
        self.connection.commit()
    

