from may24.estd_connection import estd_connection

cursor = estd_connection()
def read(stident_id):

    sql = f"""
    SELECT * FROM INFO WHERE ID = '{student_id}'
    """

    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
    choice = input("Wish to continue? (y/n) ")
    return True if choice.lower() == 'y' else False