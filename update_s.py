from may24.estd_connection import estd_connection

cursor = estd_connection()

def update(student_id, to_change, changed_data):
    sql = f"""
    
    UPDATE INFO SET {to_change} = '{changed_data}' WHERE ID='{student_id}'
    
    
    """
    cursor.execute(sql)
    print("Value updated successfully!")
    choice = input("Wish to continue? (y/n) ")
    return True if choice.lower() == 'y' else False

