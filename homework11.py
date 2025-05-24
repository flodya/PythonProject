import requests
from bs4 import BeautifulSoup


def get_usd_rate():
    url = "https://coinmarketcap.com/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features="html.parser")
        soup_list = soup.find_all(class_="sc-142c02c-0 lmjbLF")
        # print(soup_list)
        res = soup_list[0]
        print(res.text)
        print(type(res.text))

def main():
        amount = float(input("Введіть кількість валюти  "))
        rate = get_usd_rate()
        result = amount / rate
        print(f"Це  {result:.2f} .")

if __name__ == "__main__":
    main()
