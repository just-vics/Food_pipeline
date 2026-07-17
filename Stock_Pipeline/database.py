import mysql.connector
from mysql.connector import Error
from config import DatabaseConfig

def get_connection():

    try:
        
        connection = mysql.connector.connect (
         host=DatabaseConfig.Host,
         user=DatabaseConfig.User,
         password=DatabaseConfig.Password,
         database=DatabaseConfig.DatabaseName
        )
        return connection
   
    except Error as err:
        print(f"Connection Error: {err}")
        return None