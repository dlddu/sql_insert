import re
from dotenv import load_dotenv
import os 
import pymysql

# Load environment variables
load_dotenv()
config = {
    'user': os.environ.get('USERNAME'),
    'password': os.environ.get('PASSWORD'),
    'host': 'db',
    'db': os.environ.get('DATABASE'),
}

# Tables
tables = ["StatusType", "ZipCode"]

def camel_case_to_snake_case(text):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).upper()

def create_insert_query(table_name, data):
    return f'INSERT INTO {camel_case_to_snake_case(table_name)} VALUES ("{str.join("\", \"", data)}")'

def split_by_delimeter(text):
    return text.split("|")

# Connect to the MariaDB Server
try:
    db_connection = pymysql.connect(**config)
    print("Successfully connected to MariaDB!")
    
    # # Create a cursor object
    cursor = db_connection.cursor()
    
    # # Execute a ddl query
    ddl_queries = open("ddl.sql", "r").readlines()
    for ddl_query in ddl_queries:
        cursor.execute(f"DROP TABLE IF EXISTS {ddl_query.split()[2].strip()}")
        cursor.execute(ddl_query)
    
    # # Execute a insert query
    results = cursor.fetchall()
    batch = 0
    for table in tables:
        data = open(f"tpce/flat_out/{table}.txt", "r").readlines()
        insert_queries = map(lambda x: create_insert_query(table, split_by_delimeter(x.strip())), data)
        for insert_query in insert_queries:
            cursor.execute(insert_query)
            batch += 1
            if batch % 1000 == 0:
                db_connection.commit()
                print(f"Batch {batch} inserted")
                batch = 0

    
    # # Close the cursor and connection
    cursor.close()
    db_connection.commit()
    db_connection.close()
    
except pymysql.Error as e:
    print(f"Error connecting to MariaDB: {e}")
