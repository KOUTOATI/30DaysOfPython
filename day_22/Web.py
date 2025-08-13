import requests
from bs4 import BeautifulSoup
import json
url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
print(soup.title)
print(soup.title.get_text())
print(soup.body)
facts = soup.body
data = [item.get_text(strip=True) for item in facts if item.get_text(strip=True)]

with open('scrap_file.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
#
url = 'https://archive.ics.uci.edu/ml/datasets.php'
response = requests.get(url)
status = response.status_code
if status == 200:
    
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'border': '1'})
    datasets = []
    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        if len(cols) >= 6:
            dataset = {
                'Name': cols[0].get_text(strip=True),
                'Data Types': cols[1].get_text(strip=True),
                'Default Task': cols[2].get_text(strip=True),'Attribute Types': cols[3].get_text(strip=True),
                'Instances': cols[4].get_text(strip=True),
                'Attributes': cols[5].get_text(strip=True)
            }
            datasets.append(dataset)
    with open('uci_datasets.json', 'w', encoding='utf-8') as f:
        json.dump(datasets, f, ensure_ascii=False, indent=4)
else:
 print('url not recheable ')

url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

response = requests.get(url)
response.raise_for_status()  # Vérifie que la requête a réussi
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', {'class': 'wikitable'})
presidents = []
for row in table.find_all('tr')[1:]:
    cols = row.find_all(['th', 'td'])
    if len(cols) >= 4:
        number = cols[0].get_text(strip=True)
        name = cols[1].get_text(strip=True)
        term = cols[2].get_text(strip=True)
        party = cols[3].get_text(strip=True)
        president = {
            'Number': number,
            'Name': name,
            'Term': term,
            'Party': party
        }
        presidents.append(president)
with open('us_presidents.json', 'w', encoding='utf-8') as f:
    json.dump(presidents, f, ensure_ascii=False, indent=4)
