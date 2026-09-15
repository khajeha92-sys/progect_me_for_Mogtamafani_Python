#IN THE NAME OF GOD
#MADE IN AMIRABAS KHAJEH FOR MR HAJAVI
#CLASS. 4

import requests

#1. Safe Bank Transaction System

class Bank:

    def process_bank_transaction(self, account_balance, amount, transaction_type):
        try:
            if account_balance is None:
                raise Exception("Account not found")

            if amount <= 0:
                raise ValueError("Invalid amount")

            if amount > 10000:
                raise Exception("Daily limit exceeded")

            if transaction_type == "withdraw":
                if amount > account_balance:
                    raise Exception("Insufficient balance")

                account_balance -= amount
                return "Success"

            elif transaction_type == "deposit":
                account_balance += amount
                return "Success"

            else:
                raise Exception("Invalid transaction type")

        except Exception as e:
            return e


##bank = Bank()
##
##print(bank.process_bank_transaction(5000, 1000, "withdraw"))
##print(bank.process_bank_transaction(5000, 6000, "withdraw"))
##print(bank.process_bank_transaction(5000, -100, "withdraw"))
##print(bank.process_bank_transaction(None, 1000, "withdraw"))
##print(bank.process_bank_transaction(5000, 11000, "withdraw"))

#2. Robust Calculator

class Calculator:

    def calculate(self, expression):
        try:
            if expression == "":
                raise Exception("Empty expression")

            answer = eval(expression)

            return answer

        except ZeroDivisionError:
            return "Error: Division by zero"

        except NameError:
            return "Error: Invalid number"

        except SyntaxError:
            return "Error: Invalid operator"

        except Exception:
            return "Error"


##calc = Calculator()
##
##print(calc.calculate("10+5"))
##print(calc.calculate("10/0"))
##print(calc.calculate("10+abc"))
##print(calc.calculate("10 ^ 5"))
##print(calc.calculate(""))

#3. Data Parser with Recovery

class DataParser:

    def parse_data_file(self, filename):

        data = []

        try:
            file = open(filename, "r")

            lines = file.readlines()

            if len(lines) == 0:
                return []

            for line in lines:

                try:
                    number = int(line.strip())
                    data.append(number)

                except:
                    print("Invalid data:", line.strip())

            file.close()

            return data

        except FileNotFoundError:
            return "Error: File not found"

        except PermissionError:
            return "Error: Permission denied"


##parser = DataParser()
##
##print(parser.parse_data_file("numbers.txt"))

#4. User Registeration System

class User:

    def register_user(self, username, password, email, age):

        try:

            if len(username) < 3 or len(username) > 20:
                raise Exception("Username must be 3-20 characters")

            if username.isalnum() == False:
                raise Exception("Username must be alphanumeric")

            if len(password) < 8:
                raise Exception("Password too short")

            has_number = False

            for i in password:
                if i.isdigit():
                    has_number = True

            if has_number == False:
                raise Exception("Password must contain number")

            if "@" not in email:
                raise Exception("Invalid email")

            if age < 13 or age > 120:
                raise Exception("Invalid age")

            return "Registration successful"

        except Exception as e:
            return e


##user = User()
##
##print(user.register_user("amir123", "Amir123!", "amir@gmail.com", 21))
##print(user.register_user("am", "12345678", "amir@gmail.com", 21))
##print(user.register_user("amir123", "abcdefgh", "amir@gmail.com", 21))
##print(user.register_user("amir123", "Amir123!", "gmail.com", 21))
##print(user.register_user("amir123", "Amir123!", "amir@gmail.com", 10))


#5. Safe API Call Handler

##import requests

class API:

    def call_api(self, url):

        try:

            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                return {
                    "success": True,
                    "data": response.json()
                }

            elif response.status_code == 404:
                return {
                    "success": False,
                    "error": "Not Found"
                }

            elif response.status_code == 403:
                return {
                    "success": False,
                    "error": "Forbidden"
                }

            elif response.status_code == 401:
                return {
                    "success": False,
                    "error": "Unauthorized"
                }

            elif response.status_code == 500:
                return {
                    "success": False,
                    "error": "Server Error"
                }

            else:
                return {
                    "success": False,
                    "error": "Unknown Error"
                }

        except requests.exceptions.Timeout:
            return {
                "success": False,
                "error": "Timeout"
            }

        except requests.exceptions.ConnectionError:
            return {
                "success": False,
                "error": "Connection Error"
            }

        except Exception:
            return {
                "success": False,
                "error": "Invalid JSON"
            }


##api = API()
##
##print(api.call_api("https://jsonplaceholder.typicode.com/todos/1"))


###Deriver Code###
def main():
    print('1. Bank')
    bank = Bank()
    print(bank.process_bank_transaction(5000, 1000, "withdraw"))
    print(bank.process_bank_transaction(5000, 6000, "withdraw"))
    print(bank.process_bank_transaction(5000, -100, "withdraw"))
    print(bank.process_bank_transaction(None, 1000, "withdraw"))
    print(bank.process_bank_transaction(5000, 11000, "withdraw"))

    print('*'*90)

    print('2. Robust Calculator')
    calc = Calculator()
    print(calc.calculate("10+5"))
    print(calc.calculate("10/0"))
    print(calc.calculate("10+abc"))
    print(calc.calculate("10 ^ 5"))
    print(calc.calculate(""))


    print('*'*90)

    print('3. Data Parser with Recovery')
    parser = DataParser()
    print(parser.parse_data_file("numbers.txt"))

    print('*'*90)

    print('4.User Registration System')
    user = User()
    print(user.register_user("amir123", "Amir123!", "amir@gmail.com", 21))
    print(user.register_user("am", "12345678", "amir@gmail.com", 21))
    print(user.register_user("amir123", "abcdefgh", "amir@gmail.com", 21))
    print(user.register_user("amir123", "Amir123!", "gmail.com", 21))
    print(user.register_user("amir123", "Amir123!", "amir@gmail.com", 10))

    
    print('*'*90)

    print('5. API')
    api = API()
    print(api.call_api("https://jsonplaceholder.typicode.com/todos/1"))

     
    print('THE END \n AMIRABAS KHAJEH')

### MAIN ###
main()
    

# AMIRABAS KHAJEH
