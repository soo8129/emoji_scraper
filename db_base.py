import pyodbc

def news_tibero():
    db = pyodbc.connect(DSN='RGOUTSIGHT')
    db.setdecoding(pyodbc.SQL_CHAR, encoding='cp949')
    db.setdecoding(pyodbc.SQL_WCHAR, encoding='cp949')
    db.setencoding(encoding='cp949')
    return db

def community_tibero():
    db = pyodbc.connect(DSN='CDB')
    db.setdecoding(pyodbc.SQL_CHAR, encoding='cp949')
    db.setdecoding(pyodbc.SQL_WCHAR, encoding='cp949')
    db.setencoding(encoding='cp949')
    return db