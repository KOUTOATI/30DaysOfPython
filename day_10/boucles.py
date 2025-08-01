 #itérration 

for i in range(11):
    print(i)
print("\n")
# Boucle for avec range pour afficher les nombres de 0 à 10
i = 0
while i < 11:
    print(i)
    i += 1
print("\n")
# Boucle for avec range pour afficher les nombres de 10 à 0
for i in range(10, -1, -1):
    print(i)
print("\n")
# Boucle for avec range pour afficher les nombres de 10 à 0
i = 10
while i >= 0:
    print(i)
    i -= 1  
print("\n")
# triangle de #
for i in range(1, 8):
    print("#" * i)
print("\n")
for i in range(6):  # 6 lignes
    for j in range(13):  # 13 symboles #
        print("#", end=" ")
    print()  
print("\n")
# table de multiplication
for i in range (11):
    print(f"{i} * {i} = {i*i}")
print("\n")
# itération sur une liste
list = ['python', 'numpy', 'pandas', 'django', 'flask']
for mot in list:
    print(mot)
print("\n")
#itération sur les chiffres pairs de 0 à 100
for i in range(101):
    if i % 2 == 0:
        print(i, end=" ")
print("\n")
#itération sur les chiffres impairs de 0 à 100
for i in range(101):
    if i % 2 != 0:
        print(i, end=" ")
print("\n")
#iteeration sur les chiffres de 0 à 100  et afficher la somme
somme = 0
for i in range(101):
    somme += i
print(f"\nLa somme des chiffres de 0 a 100 est : {somme}")
print("\n")
# pour les chiffres pairs et impairs de 0 à 100
somme_paire = 0
somme_impair = 0
for i in range(101):
    if i % 2 == 0:
        somme_paire += i
    else:
        somme_impair += i
print(f"La somme des chiffres pairs de 0 a 100 est : {somme_paire}")
print(f"La somme des chiffres impairs de 0 a 100 est : {somme_impair}")
print("\n")
# interation sur des fichiers
from countries import countries
# afficher les pays contenant le mot 'land'
for pays in countries:
    if 'land' in pays.lower():
        print(pays)
print("\n")
# iteration sur une liste 
liste  = ['banana', 'orange', 'mango', 'lemon']
for i in range(len(liste) - 1, -1, -1):
    print(liste[i])
print("\n")
# itération sur les données des pays
from countries_data import countries_data
from collections import Counter

all_languages = set()
for country in countries_data:
    all_languages.update(country['languages'])
print("Total languages:", len(all_languages))

#
language_counter = Counter()
for country in countries_data:
    for lang in country['languages']:
        language_counter[lang] += 1
most_spoken = language_counter.most_common(10)
print("\nTen most spoken languages:")
for lang, count in most_spoken:
    print(f"{lang}: {count} countries")
#
sorted_by_population = sorted(countries_data, key=lambda c: c['population'], reverse=True)
print("\nTen most populated countries:")
for country in sorted_by_population[:10]:
    print(f"{country['name']}: {country['population']}")