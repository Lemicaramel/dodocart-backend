from src.DBconnection import get_connection
def create_user(user):

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
        curr.execute("insert into user_info (name,age,email_id,password,designation) values ( %s  , %s  , %s  , %s  , %s  );",(user.name,user.age,user.email_id,user.password,user.designation))

        conn.commit()
    except Exception as e:
        print("Error:", e)
        conn.rollback()

    finally:
        curr.close()
        conn.close()