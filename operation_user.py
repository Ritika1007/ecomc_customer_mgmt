import random
import string
import json
import ast
from model_customer import Customer
from model_admin import Admin


class UserOperation:
    def __init__(self):
        pass

    @staticmethod
    def generate_unique_user_id():
        user_id = ''.join(random.choices(string.digits, k=10))
        return f'u_{user_id}'

    @staticmethod
    def encrypt_password(user_password):
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=len(user_password) * 2))
        encrypted_password = ''
        for i, char in enumerate(user_password):
            encrypted_password += random_string[i*2:i*2+2] + char
        return f'^^{encrypted_password}$$'

    @staticmethod
    def decrypt_password(encrypted_password):
        decrypted_password = ''
        encrypted_password = encrypted_password[2:-2]  # Remove the "^^" and "$$" markers
        for i in range(0, len(encrypted_password), 3):
            decrypted_password += encrypted_password[i:i+2]
        return decrypted_password

    @staticmethod
    def check_username_exist(user_name):
        with open("data/users.txt", "r") as file:
            for line in file:
                user_data = ast.literal_eval(line)
                if user_data['user_name'] == user_name:
                    return True
        
        return False  # User not found


    @staticmethod
    def validate_username(user_name):
        if len(user_name) >= 5 and user_name.isalpha():
            return True
        return False

    @staticmethod
    def validate_password(user_password):
        has_letter = False
        has_number = False
        for char in user_password:
            if char.isalpha():
                has_letter = True
            elif char.isdigit():
                has_number = True
            if has_letter and has_number:
                return True
        return False

    def login(user_name, user_password):
        with open("data/users.txt", "r") as file:
            for line in file:
                # Split the line by ':' to extract the user data
                user_data = line.strip().split(":")
                
                # Extract the username, encrypted password, register_time, and user_role
                username = user_data[0]
                encrypted_password = user_data[1]
                register_time = user_data[2]
                user_role = user_data[3]
                
                # Check if the provided username matches the stored username
                if username == user_name:
                    # Decrypt the password
                    decrypted_password = UserOperation.decrypt_password(encrypted_password)
                    
                    # Check if the decrypted password matches the provided password
                    if decrypted_password == user_password:
                        if user_role == "customer":
                            # Return a Customer object
                            return Customer(username, decrypted_password, register_time)
                        elif user_role == "admin":
                            # Return an Admin object
                            return Admin(username, decrypted_password, register_time)
        
        return None  # User not found or incorrect username/password combination



# Example usage
# user_op = UserOperation()
# user_id = user_op.generate_unique_user_id()
# encrypted_password = user_op.encrypt_password('admin1')
# decrypted_password = user_op.decrypt_password(encrypted_password)
# username_exists = user_op.check_username_exist('JohnDoe')
# valid_username = user_op.validate_username('Jane_Doe')
# valid_password = user_op.validate_password('password123')
# user = user_op.login('JohnDoe', encrypted_password)

# print(user_id)
# print(encrypted_password)
# print(decrypted_password)
# print(username_exists)
# print(valid_username)
# print(valid_password)
# print(user)