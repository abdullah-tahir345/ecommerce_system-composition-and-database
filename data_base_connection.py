import pyodbc

def database_connection():
    connection_string = 'DRIVER={SQL Server};SERVER=DESKTOP-2C0TSUE;DATABASE=Store'
    # Connect to MSSQL database
    conn = pyodbc.connect(connection_string)
    return conn