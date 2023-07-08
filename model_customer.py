from model_user import User

class Customer(User):
    def __init__(self, user_id, user_name, user_password, user_register_time, user_role='customer', user_email='', user_mobile=''):
        super().__init__(user_id, user_name, user_password, user_register_time, user_role)
        self.user_email = user_email
        self.user_mobile = user_mobile

    def __str__(self):
        user_info = super().__str__()
        customer_info = f"'user_email':'{self.user_email}', 'user_mobile':'{self.user_mobile}'"
        return user_info[:-1] + ', ' + customer_info + "}"

# Example usage
# customer = Customer(user_id='u_1234567890', user_name='John', user_password='password123', user_email='john@example.com', user_mobile='0412345678')
# print(customer)