# exercice 1
# controle d'age 
age = int(input("entrez votre age :"))
if age >= 18:
    print("Vous êtes assez vieux pour conduire")
else:
    print(f"vous avez besoins de {age - 18} ans de plus pour conduire")

# comparaisons d'age
My_age =  21
age = int(input("entrez votre age :"))
if My_age > age:
    print(f" vous avez {My_age - age} ans de moins que moi")
elif My_age < age:
    print(f" vous avez {age - My_age} ans de plus que moi")
elif My_age == age:
    print("nous avons le même age")

#comparaisons entre deux nombres 
a = int(input("entrez un numéro un:"))
b = int(input("entrez un numéro deux  :"))
if a > b:
    print(f"{a} est supérieur a  {b}")
elif a < b:
    print(f"{a} est plus petit que {b}")
else: 
    print(f"{a} et {b} sont égaux")

# exercice 2
# controle de la note
score = int(input("Entrez le score de l'élève : "))

if 80 <= score <= 100:
    note = "A"
elif 70 <= score <= 79:
    note = "B"
elif 60 <= score <= 69:
    note = "C"
elif 50 <= score <= 59:
    note = "D"
elif 0 <= score <= 49:
    note = "F"
else:
    note = "Score invalide"

print(f"La note de l'élève est : {note}")

#vérification de saison 

mois = input("Entrez un mois : ").lower()

if mois in ["septembre", "octobre", "novembre"]:
    saison = "automne"
elif mois in ["décembre", "janvier", "février"]:
    saison = "hiver"
elif mois in ["mars", "avril", "mai"]:
    saison = "printemps"
elif mois in ["juin", "juillet", "août"]:
    saison = "été"
else:
    saison = "mois invalide"

print(f"La saison est : {saison}")

# vérification dans  une liste 

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Entrez un fruit : ").lower()
if fruit in fruits:
    print("ce fruit existe déja dans la liste.")
else:
    print("la liste modifiéée:", fruits + [fruit])

# exercice 3

personne = {'first_name': 'ABALO', 'last_name': 'KOKOU', 'age': 24, 'country': 'Finland', 'is_married': True, 'compétences':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], 'Zipcode': '003448'}
if 'compétences' in personne:
    print(f"la personne a des compétences en {personne['compétences']}")
else:
    print("la personne n'a pas de compétences spécifiées.")
if 'compétences' in personne:
    if personne['compétences'] == 'Python':
        print("la personne est un développeur Python")
    else:
        print("la personne n'a pas de compétences en Python")
else:
    print("la personne n'a pas de compétences spécifiées.")

if set('compétences') == {'JavaScript', 'React'}:
     print("Il est un développeur frontend")
elif {'Node', 'Python', 'MongoDB'}.issubset('compétences'):
     print("Il est un développeur backend")
elif {'React', 'Node', 'MongoDB'}.issubset('compétences'):
    print("Il est un développeur Fullstack")
else:
    print("INCONNET TITME")
if personne['is_married'] and personne['country'] == 'Finland':
 print(f"{personne['first_name']} vit en Finlande et est marié.")
