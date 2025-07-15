class Orders:
    
    def __init__(self,order_id,user_id,product_id,quantity,amount,shipping_address):
        
        self.order_id= order_id
        self.user_id = user_id
        self.product_id  = product_id 
        self.quantity = quantity
        self.amount = amount
        self.shipping_address = shipping_address