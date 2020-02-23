import pymysql
import pandas as pd

host="hackathon.cgbbgydmzqnb.us-east-2.rds.amazonaws.com"
port=3306
dbname="TrumpBot"
user="admin"
password="hackathon"

#connect to the mySQL data base 
def get_connection():
    return pymysql.connect(host, user=user, port=port, passwd=password, db=dbname)

#Returns true if added
def add_headline(cursor, text):
    text = text.replace("'", "''")
    doesnt_exist = not headline_exists(cursor, text)
    if doesnt_exist:
        sql = "INSERT INTO Headline (text, posted) VALUES ('{0}', 0)"
        cursor.execute(sql.format(text))
    return doesnt_exist

# should only be used internally
def headline_exists(cursor, text):
    sql = "SELECT text FROM Headline WHERE text='{0}'"
    result = cursor.execute(sql.format(text))
    return result != 0
    
def mark_headline_as_posted(cursor, text):
    text = text.replace("'", "''")
    sql = "UPDATE Headline SET posted=1 WHERE text='{0}'"
    cursor.execute(sql.format(text))

#returns empty string if no headlines
def get_a_headline(cursor):
    sql = "SELECT text FROM Headline WHERE posted=0 LIMIT 1"
    result = cursor.execute(sql)
    return '' if result == 0 else cursor.fetchone()[0]