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

# Connect to the MariaDB Server
try:
    db_connection = pymysql.connect(**config)
    print("Successfully connected to MariaDB!")
    
    # # Create a cursor object
    # cursor = db_connection.cursor()
    
    # # Execute a query
    # cursor.execute("SELECT * FROM your_table")
    
    # # Fetch results
    # results = cursor.fetchall()
    # for row in results:
    #     print(row)
    
    # # Close the cursor and connection
    # cursor.close()
    db_connection.close()
    
except pymysql.Error as e:
    print(f"Error connecting to MariaDB: {e}")
