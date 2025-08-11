import re
import requests
from collections import Counter
def find_most_common_words(url, num_words):
    response = requests.get(url)
    text = response.text

    # Remove Project Gutenberg's header and footer
    start_marker = "*** START OF THIS PROJECT GUTENBERG EBOOK"
    end_marker = "*** END OF THIS PROJECT GUTENBERG EBOOK"
    start = text.find(start_marker)
    end = text.find(end_marker)
    if start != -1 and end != -1:
        text = text[start+len(start_marker):end]

    # Convert to lowercase and extract words
    words = re.findall(r'\b\w+\b', text.lower())

    # Count word frequencies
    word_counts = Counter(words)

    # Get the most common words
    return word_counts.most_common(num_words)
romeo_and_juliet_url = 'http://www.gutenberg.org/files/1112/1112.txt'
top_words = find_most_common_words(romeo_and_juliet_url, 10)
for word, count in top_words:
    print(f"{word}: {count}")


import statistics

def parse_range(range_str):
    """Convertit une chaîne de type '3 - 5' en une liste de deux floats."""
    try:
        parts = range_str.strip().split(' - ')
        return [float(p) for p in parts]
    except:
        return []

def fetch_cat_data():
    url = 'https://api.thecatapi.com/v1/breeds'
    response = requests.get(url)
    return response.json()

def compute_statistics(values):
    return {
        'min': min(values),
        'max': max(values),
        'mean': round(statistics.mean(values), 2),
        'median': round(statistics.median(values), 2),
        'std_dev': round(statistics.stdev(values), 2) if len(values) > 1 else 0.0
    }

def analyze_cats():
    data = fetch_cat_data()

    weight_values = []
    lifespan_values = []
    origins = []

    for breed in data:
      weight_range = parse_range(breed.get('weight', {}).get('metric', ''))
    if weight_range:
            weight_values.extend(weight_range)

        # Espérance de vie
    lifespan_range = parse_range(breed.get('life_span', ''))
    if lifespan_range:
            lifespan_values.extend(lifespan_range)

        # Origine
    origin = breed.get('origin', 'Unknown')
    origins.append(origin)

    weight_stats = compute_statistics(weight_values)
    lifespan_stats = compute_statistics(lifespan_values)
    origin_counts = Counter(origins)

    return weight_stats, lifespan_stats, origin_counts

weight_stats, lifespan_stats, origin_counts = analyze_cats()

print("Statistiques du poids (kg) :")
for key, value in weight_stats.items():
    print(f"{key.capitalize()} : {value}")

print("\n Statistiques de l'espérance de vie (années) :")
for key, value in lifespan_stats.items():
    print(f"{key.capitalize()} : {value}")

print("\n Nombre de races par pays d'origine :")
for country, count in origin_counts.items():
    print(f"{country} : {count}")

#


def fetch_countries_data():
    url = 'https://restcountries.com/v3.1/all'
    response = requests.get(url)
    countries = response.json()
    return countries

def get_largest_countries(countries, top_n=10):
    countries_with_area = [(country['name']['common'], country.get('area', 0)) for country in countries]
    sorted_by_area = sorted(countries_with_area, key=lambda x: x[1], reverse=True)
    return sorted_by_area[:top_n]

def get_most_spoken_languages(countries, top_n=10):
    language_counter = Counter()
    for country in countries:
        langs = country.get('languages', {})
        for lang in langs.values():
            language_counter[lang] += 1
    return language_counter.most_common(top_n)

def get_total_languages(countries):
    languages = set()
    for country in countries:
        langs = country.get('languages', {})
        for lang in langs.values():
       
         languages.add(lang)
         return len(languages)

countries = fetch_countries_data()

print("10 plus grands pays par superficie :")
for name, area in get_largest_countries(countries):
    print(f"{name}: {area} km²")

print("\n 10 langues les plus parlées :")
for lang, count in get_most_spoken_languages(countries):
    print(f"{lang}: parlé dans {count} pays")

print("\n Nombre total de langues uniques :")
print(get_total_languages(countries))
# 

from bs4 import BeautifulSoup

#URL de la page des ensembles de données de l'UCI
url = 'https://archive.ics.uci.edu/ml/datasets.php'

#Effectuer une requête HTTP GET pour obtenir le contenu de la page
response = requests.get(url)
response.raise_for_status()  # Vérifie que la requête a réussi

#Analyser le contenu HTML de la page avec BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

#Trouver tous les liens vers les ensembles de données
dataset_links = soup.find_all('a', href=True)

#Filtrer les liens qui mènent aux ensembles de données
datasets = []
for link in dataset_links:
    href = link['href']
    if href.startswith('datasets/') and 'ml/datasets/' not in href:
        dataset_name = link.text.strip()
        dataset_url = f"https://archive.ics.uci.edu/ml/{href}"
        datasets.append({'name': dataset_name, 'url': dataset_url})

#Afficher les 10 premiers ensembles de données
for dataset in datasets[:10]:
   print(f"Nom de l'ensemble de données : {dataset['name']}")
   print(f"URL : {dataset['url']}\n")
