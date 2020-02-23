import requests
import DatabaseInterface as db
from bs4 import BeautifulSoup

connection = db.get_connection()
cursor = connection.cursor()

response = requests.get('https://www.politico.com/politics')
parser = BeautifulSoup(response.text, "html.parser")

for a in parser.select('div.summary header h3 a'):
    headline = a.text
    if(len(headline) <= 400):
        db.add_headline(cursor, headline)

connection.commit()
cursor.close()
connection.close()