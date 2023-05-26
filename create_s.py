from may24.estd_connection import estd_connection

cursor = estd_connection()

def create():
    id = input("Enter student id: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    email = input("Enter email: ")
    sql = f"""
    INSERT INTO INFO(ID, NAME, AGE, EMAIL) VALUES ('{id}', '{name}', {age}, '{email}')
    
    """
    cursor.execute(sql)
    print("Values added successfully!")
    choice = input("Wish to continue? (y/n) ")
    return True if choice.lower() == 'y' else False