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
        if not UserOperation.validate_username(user_name):
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
        if attribute_name == 'user_name':
            if UserOperation.validate_username(value):
                if not UserOperation.check_username_exist(value):
                    customer_object.user_name = value
                else:
                    print('Username already exists! Choose a different one')
                    return False
            else:
                print('Username is  invalid!')
                return False
        elif attribute_name == 'user_password':
            if UserOperation.validate_password(value):
                customer_object.user_password = UserOperation.encrypt_password(value)
            else:

                return False
        elif attribute_name == 'user_email':
            if CustomerOperation.validate_email(value):
                customer_object.user_email = value
            else:
                return False
        elif attribute_name == 'user_mobile':
            if CustomerOperation.validate_mobile(value):
                customer_object.user_mobile = value
            else:
                return False
        else:
            return False
        
        with open("data/users.txt", "r") as file:
            user_data = file.readlines()

        for i in range(0,len(user_data)):
                user = eval(user_data[i])
                
                if user['user_id'] == customer_object.user_id:
                    user[attribute_name] = value
                    user_data[i] = str(user).replace(' ','')+"\n" 
                    with open('data/users.txt', 'w') as file:
                        file.writelines(user_data)
                    
                    return True

    @staticmethod
    def delete_customer(customer_id):
        file_path = 'data/users.txt'
        lines = []

        with open(file_path, 'r') as file:
            for line in file:
                if f"'user_id':'{customer_id}'" not in line:
                    lines.append(line)

        if len(lines) == 0:
            return False

        with open(file_path, 'w') as file:
            file.writelines(lines)

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
        with open('data/users.txt', 'w') as file:
            file.truncate()

# Example usage
customer_op = CustomerOperation()
# registered = customer_op.register_customer('JohnDoe', 'password123', 'john.doe@example.com', '0412345678')
# registered = customer_op.register_customer('Ritika', 'password123', 'ritika10arora@gmail.com', '0412345678')
# registered = customer_op.register_customer('RitikaA', 'password12345', 'ritikacsarora@gmail.com', '0412345678')

# customer = Customer()
# customer.user_id = 'u_9465399634'
# customer.user_name = 'Ritika'

# # Call the update_profile function
# success = CustomerOperation.update_profile('user_name', 'RitikaArora', customer)

# if success:
#     print("Profile updated successfully.")
# else:
#     print("Failed to update profile.")

# deleted = customer_op.delete_customer('u_9465399634')
# if deleted:
#     print("Customer deleted successfully.")
# else:
#     print("Customer not found in the file.")

# cust_list=customer_op.get_customer_list(2)
# print(cust_list)


# customer_op.delete_all_customers()