from model_user import User

class Admin(User):
    def __init__(self, user_id, user_name, user_password, user_register_time, user_role='admin'):
        super().__init__(user_id, user_name, user_password, user_register_time, user_role)

    def __str__(self):
        return super().__str__()

# Example usage
# admin = Admin(user_id='u_1234567890', user_name='Admin1', user_password='adminpass')
# print(admin)