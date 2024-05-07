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
tables = [("StatusType", "STATUS_TYPE"), ("ZipCode", "ZIP_CODE"), ("TaxRate", "TAXRATE"), ("Sector", "SECTOR"), ("NewsItem", "NEWS_ITEM"), ("TradeType", "TRADE_TYPE"), \
          ("Address", "ADDRESS"), ("Industry", "INDUSTRY"), ("Charge", "CHARGE"), ("Broker", "BROKER"), \
          ("Company","COMPANY"), ("Customer","CUSTOMER"), ("Exchange","EXCHANGE"), \
          ("CustomerAccount","CUSTOMER_ACCOUNT"), ("CustomerTaxrate","CUSTOMER_TAXRATE"), ("CommissionRate","COMMISSION_RATE"), ("CompanyCompetitor","COMPANY_COMPETITOR"), ("Financial","FINANCIAL"), ("NewsXRef","NEWS_XREF"), ("Security","SECURITY"), ("WatchList","WATCH_LIST"), \
          ("AccountPermission","ACCOUNT_PERMISSION"), ("HoldingSummary","HOLDING_SUMMARY"), ("WatchItem","WATCH_ITEM"), ("Trade", "TRADE"), ("DailyMarket", "DAILY_MARKET"), ("LastTrade", "LAST_TRADE"), \
          ("Holding", "HOLDING"), ("HoldingHistory", "HOLDING_HISTORY"), ("CashTransaction", "CASH_TRANSACTION"), ("Settlement", "SETTLEMENT"), ("TradeHistory", "TRADE_HISTORY")]

def create_insert_query(table_name, data):
    return f'INSERT INTO {table_name} VALUES ("{str.join("\", \"", data)}")'

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

    for ddl_query in reversed(ddl_queries):
        cursor.execute(f"DROP TABLE IF EXISTS {ddl_query.split()[2].strip()}")
    for ddl_query in ddl_queries:
        cursor.execute(ddl_query)
    
    # # Execute a insert query
    results = cursor.fetchall()
    batch = 0
    for (file_name, table_name) in tables:
        data = open(f"tpce/flat_out/{file_name}.txt", "r").readlines()
        insert_queries = map(lambda x: create_insert_query(table_name, split_by_delimeter(x.strip())), data)
        for insert_query in insert_queries:
            try:
                cursor.execute(insert_query)
            except Exception as er:
                print(insert_query)
                print(er)
                exit()
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
