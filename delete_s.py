from may24.estd_connection import estd_connection

cursor = estd_connection()

def delete(srudent_id):
    sql = """
    DELETE FROM INFO WHERE ID='{id}'
    """
    cursor.execute(sql)
    print("Value deleted successfully!")
    choice = input("Wish to continue? (y/n) ")
    return True if choice.lower() == 'y' else False

