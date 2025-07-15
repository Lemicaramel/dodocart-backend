from src.DBconnection import get_connection
def create_product(product):

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
        curr.execute("insert into product (product_id,product_name,mrp_price,description,color,size,category_id) values ( %s  , %s  , %s  , %s  , %s  , %s  , %s  );",(product.product_id,product.product_name,product.mrp_price,product.color,product.size,product.description_id))

        conn.commit()
    except Exception as e:
        print("Error:", e)
        conn.rollback()

    finally:
        curr.close()
        conn.close()