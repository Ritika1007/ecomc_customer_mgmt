import re
from operation_user import UserOperation
from model_customer import Customer
from datetime import datetime

class CustomerOperation:
    def __init__(self):
        pass

    @staticmethod
    def validate_email(user_email):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, user_email) is not None

    @staticmethod
    def validate_mobile(user_mobile):
        mobile_regex = r'^(04|03)\d{8}$'
        return re.match(mobile_regex, user_mobile) is not None

    @staticmethod
    def register_customer(user_name, user_password, user_email, user_mobile):
        # Perform validations
        if not CustomerOperation.validate_email(user_email):
            return False
        if not CustomerOperation.validate_mobile(user_mobile):
            return False

        if not UserOperation.check_username_exist(user_name):
            user_id = UserOperation.generate_unique_user_id()
            user_register_time = datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
            encrypt_pass = UserOperation.encrypt_password(user_password)
            customer = Customer(user_id, user_name, encrypt_pass, user_register_time, 'customer', user_email, user_mobile)
            with open('data/users.txt', 'a') as file:
                file.write(str(customer) + '\n')

    @staticmethod
    def update_profile(attribute_name, value, customer_object):
        # Perform validations based on attribute_name
        if attribute_name == 'user_email':
            if not CustomerOperation.validate_email(value):
                return False
        elif attribute_name == 'user_mobile':
            if not CustomerOperation.validate_mobile(value):
                return False

        # Update the attribute value in the customer_object
        setattr(customer_object, attribute_name, value)

        # Update the changes in the data/users.txt file
        with open('data/users.txt', 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if line.strip() == str(customer_object):
                    file.write(str(customer_object) + '\n')
                else:
                    file.write(line)
            file.truncate()
        
        return True

    @staticmethod
    def delete_customer(customer_id):
        # Remove the customer from the data/users.txt file based on customer_id
        with open('data/users.txt', 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if not line.startswith("{'user_id':'" + customer_id + "'"):
                    file.write(line)
            file.truncate()
        
        return True

    @staticmethod
    def get_customer_list(page_number):
        page_size = 10  # Number of customers per page
        customers = []
        with open('data/users.txt', 'r') as file:
            lines = file.readlines()
            total_customers = len(lines)
            start_index = (page_number - 1) * page_size
            end_index = start_index + page_size
            for line in lines[start_index:end_index]:
                # Create customer objects and append them to the customers list
                customer_info = eval(line.strip())
                customer = Customer(
                    customer_info['user_id'], 
                    customer_info['user_name'], 
                    customer_info['user_password'], 
                    customer_info['user_register_time'], 
                    customer_info['user_role'], 
                    customer_info['user_email'], 
                    customer_info['user_mobile']
                )
                customers.append(customer)

        total_pages = total_customers // page_size + 1 if total_customers % page_size != 0 else total_customers // page_size
        return customers, page_number, total_pages

    @staticmethod
    def delete_all_customers():
        # Remove all customers from the data/users.txt file
        with open('data/users.txt', 'w') as file:
            file.truncate()

# Example usage
customer_op = CustomerOperation()
registered = customer_op.register_customer('JohnDoe', 'password123', 'john.doe@example.com', '0412345678')

