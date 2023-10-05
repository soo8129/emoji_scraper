import pyodbc
import sys

def rgoutsight_tibero():
    db = pyodbc.connect(DSN='RGOUTSIGHT', uid="ndb", upw="4C7C1E980897BCE3775821600D50F47874F3102E", database="tibero")
    db.setdecoding(pyodbc.SQL_CHAR, encoding='cp949')
    db.setdecoding(pyodbc.SQL_WCHAR, encoding='cp949')
    db.setencoding(encoding='cp949')
    return db

def tibero():
    db = pyodbc.connect(DSN='NDB', uid="ndb", upw="tibero", database="tibero")
    db.setdecoding(pyodbc.SQL_CHAR, encoding='cp949')
    db.setdecoding(pyodbc.SQL_WCHAR, encoding='cp949')
    db.setencoding(encoding='cp949')
    return db

def community_tibero():
    db = pyodbc.connect(DSN='CDB', uid="cdb", upw="4C7C1E980897BCE3775821600D50F47874F3102E", database="tibero")
    db.setdecoding(pyodbc.SQL_CHAR, encoding='cp949')
    db.setdecoding(pyodbc.SQL_WCHAR, encoding='cp949')
    db.setencoding(encoding='cp949')
    return db