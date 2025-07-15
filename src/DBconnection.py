import psycopg2
def get_connection():
    try:
        return psycopg2.connect(
            database="test",
            user="postgres",
            password="admin",
            host="localhost",
            port=5432,
        )
    except Exception as e:
        print("Error:", e)
        return False
conn = get_connection()
if conn:
    print("Connection to the PostgreSQL established successfully.")
else:
    print("Connection to the PostgreSQL encountered and error.")

