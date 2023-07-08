class Order:
    def __init__(self, order_id='o_00000', user_id='', pro_id='', order_time='00-00-0000_00:00:00'):
        self.order_id = order_id
        self.user_id = user_id
        self.pro_id = pro_id
        self.order_time = order_time

    def __str__(self):
        return f"{{'order_id':'{self.order_id}', 'user_id':'{self.user_id}', 'pro_id':'{self.pro_id}', 'order_time':'{self.order_time}'}}"

# Example usage
# order = Order(order_id='o_12345', user_id='u_98765', pro_id='p_456', order_time='12-06-2023_15:30:00')
# print(order)

# To reduce the program difficulty, we assume each order only has one product.