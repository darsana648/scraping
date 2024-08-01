import pandas as pd
import requests
from bs4 import BeautifulSoup


url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'


page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

data = {
    "country": [],
    "confirmed": [],
    "deaths": [],
    "continent": [],
}

data_iterator = iter(soup.find_all('td'))

while True:
    try:
        country = next(data_iterator).text.strip()
        confirmed = next(data_iterator).text.strip()
        confirmed_int = int(confirmed.replace(",", ""))
        deaths = next(data_iterator).text.strip()
        deaths_int = int(deaths.replace(",", ""))
        continent = next(data_iterator).text.strip()

        data["country"].append(country)
        data["confirmed"].append(confirmed_int)
        data["deaths"].append(deaths_int)
        data["continent"].append(continent)

    except StopIteration:
        break

df = pd.DataFrame(data)

print(df)
df.to_excel('covid_data.xlsx', index=False, engine='openpyxl')