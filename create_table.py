from may24.estd_connection import estd_connection

cursor = estd_connection()

sql = """
CREATE TABLE INFO(
ID CHAR(20),
NAME CHAR(20),
EMAIL CHAR(20),
AGE INT
)

"""
cursor.execute(sql)
print("table created successfully!")