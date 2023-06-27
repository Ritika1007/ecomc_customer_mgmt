class Product:
    def __init__(self, pro_id='', pro_model='', pro_category='', pro_name='', pro_current_price=0, pro_raw_price=0, pro_discount=0, pro_likes_count=0):
        self.pro_id = pro_id
        self.pro_model = pro_model
        self.pro_category = pro_category
        self.pro_name = pro_name
        self.pro_current_price = pro_current_price
        self.pro_raw_price = pro_raw_price
        self.pro_discount = pro_discount
        self.pro_likes_count = pro_likes_count

    def __str__(self):
        return f"{{'pro_id':'{self.pro_id}', 'pro_model':'{self.pro_model}', 'pro_category':'{self.pro_category}', 'pro_name':'{self.pro_name}', 'pro_current_price':{self.pro_current_price}, 'pro_raw_price':{self.pro_raw_price}, 'pro_discount':{self.pro_discount}, 'pro_likes_count':{self.pro_likes_count}}}"

# Example usage
# product = Product(pro_id='p_123', pro_model='Model X', pro_category='Electronics', pro_name='Smartphone', pro_current_price=999.99, pro_raw_price=1299.99, pro_discount=23, pro_likes_count=50)
# print(product)
