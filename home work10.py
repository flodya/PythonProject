import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime


url = "https://www.timeanddate.com/weather/ukraine/dnipro"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")


temperature_tag = soup.find("div", class_="h2")
temperature = temperature_tag.text.strip() if temperature_tag else "N/A"


now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

conn = sqlite3.connect("weather.db")
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather (
        time TEXT,
        temperature TEXT
    )
''')


cursor.execute(" weather (datetime, temperature) VALUES (?, ?)", (now, temperature))
conn.commit()

for row in cursor.execute("SELECT * FROM weather"):
    print(row)

conn.close()
