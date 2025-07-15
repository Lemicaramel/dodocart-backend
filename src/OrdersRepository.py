from src.DBconnection import get_connection
def create_orders(orders):

    conn = get_connection()
    if conn:
        print("Connection to the PostgreSQL established successfully.")
    else:
        print("Connection to the PostgreSQL encountered and error.")
        return 
   
    try:
        # CREATE A CURSOR USING THE CONNECTION OBJECT
        curr = conn.cursor()
        # EXECUTE THE SQL QUERY
        curr.execute("insert into orders (order_id,user_id,product_id,quantity,amount,shipping_address) values ( %s  , %s  , %s  , %s  , %s  , %s  );",(orders.order_id,orders.user_id,orders.product_id,orders.quantity,orders.amount,orders.shipping_address))

        conn.commit()
    except Exception as e:
        print("Error:", e)
        conn.rollback()

    finally:
        curr.close()
        conn.close()