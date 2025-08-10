#a 
def count_words(text):
    count_number = 0
    counter_lines = 0
    for word in text:
     if word.isalpha():
         count_number += 1
     for line in text:
        counter_lines += 1
        count_number += len(line.split())
    print(f"Total number of words: {count_number}")
    print(f"Total number of lines: {counter_lines}")
count_words('obama_speech.txt')
count_words('michelle_obama_speech.txt')
count_words('donald_speech.txt')
count_words('melina_trump_speech.txt')

import json
from collections import Counter
def most_spoken_languages(filepath, top_n):
    with open(filepath, 'r', encoding='utf-8') as f:
        countries = json.load(f)

    language_counter = Counter()

    for country in countries:
        languages = country.get('languages', [])
        language_counter.update(languages)

    return language_counter.most_common(top_n)
print(most_spoken_languages('day_19/countries_data.json', 3))

def most_populated_countries(filepath, top_n):
    with open(filepath, 'r', encoding='utf-8') as f:
        countries = json.load(f)

    population_counter = Counter()

    for country in countries:
        name = country.get('name')
        population = country.get('population', 0)
        population_counter[name] = population

    return population_counter.most_common(top_n)
print(most_populated_countries('day_19/countries_data.json', 10))
import re

def extract_emails(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    emails = re.findall(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', content)
    return emails
print(extract_emails('day_19\email_exchanges_big.txt'))

def find_most_common_words(data, num_words):
    # Vérifie si c'est un fichier
    try:
        with open(data, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        text = data  # si ce n'est pas un fichier, on considère que c'est un texte brut

    # Nettoyage et découpage du texte
    words = re.findall(r'\b\w+\b', text.lower())  # convertit en minuscules et isole les mots

    # Compter les occurrences
    most_common = Counter(words).most_common(num_words)

    return most_common
text = "This is a test. This test is only a test. Just a test."
print(find_most_common_words(text, 3))

