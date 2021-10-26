from time import perf_counter
import requests
from bs4 import BeautifulSoup


currencies = ["bitcoin", "dogecoin", "plantvsundead", "ethereum", "solana"]

for currency in currencies:
    url = "https://coinmarketcap.com/currencies/{}/".format(currency)

    # print(perf_counter(), "Downloading...")
    response = requests.get(url)
    # print(perf_counter(), "Downloaded.")
    soup = BeautifulSoup(response.text, features="html.parser")
    # print(perf_counter(), "Parsed.")

    class_name = "sc-16r8icm-0 nds9rn-0 dAxhCK"
    statistics_table = soup.find("div", class_=class_name).table

    table_data = statistics_table.find_all("td")

    price = table_data[0].text
    change = table_data[1].span.text
    print(f"{currency:<15}{price:<15}{change:<15}")
