# concaténation

mot1 = "trente "
mot2 = "jours "
mot3 = "de "
mot4 = "python"
print(mot1 + mot2 + mot3 + mot4)
print("codage","pour","tous")
societe = "codage pour tous "
print(societe)
societe = societe.upper()
print(societe)
societe = societe.lower()
print(societe)
print("Coding For All".capitalize())
print("Coding For All".title())
print("Coding For All".swapcase())
phrase = "Coding For All"
print(phrase.split()[0])

# Vérifie si "Coding" est dans la chaîne
try:
    index = phrase.index("Coding")
    print(f'"Coding" trouvé à l’index {index}')
except ValueError:
    print('"Coding" non trouvé')

print("Coding" in phrase)

chaine = "codage pour tous"
chaine2 = "python pour tous le momnde"
print(chaine.replace("codage", "python"))
print(chaine2.replace("tout le monde", "tous"))
print(chaine.split())
chaine3 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(chaine3.split(","))
mots = "Coding For All"
print(mots[0])
mots1 = "codage pour toutes"
print(mots1[10])
phrase = "Python pour tout le monde"
lines = chaine2.split()
acronyme = ''.join([mot[0].upper() for mot in lines])
print(acronyme)

lines2 = chaine.split()
abreviation = ''.join([mot[0].upper() for mot in lines2])
print(mots1.find('c'))
print(mots1.find('F'))
print(mots1.rfind('L'))
phrase3 = "Vous ne pouvez pas mettre fin à une phrase avec parce que parce que c'est une conjonction"
print(phrase3.find("parce que"))
try:
    position = phrase.rindex("car")
    print("Dernière occurrence à l'index :", position)
except ValueError:
    print(f"Le mot '{"car"}' n'a pas été trouvé dans la phrase.")

#
phrase6 = "Vous ne pouvez pas mettre fin à une phrase avec parce que parce que parce que c'est une conjonction"
expression = "parce que parce que"
index = phrase6.find(expression)

# Extraire la portion
tranche = phrase[index:index + len(expression)]
print(tranche)
# position
print(phrase6.find('parce que'))
#
print(phrase6.replace("parce que", ""))
#
print(mots1.startswith("conding"))
#
print(mots1.endswith("coding"))
print(mots1.strip())

print("ofpython o Thirty_days_of_python".isidentifier())

libs = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
result = " # ".join(libs)
print(result)
print("j'apprécie cd défi .\n Je me demande juste quelle est la prochaine étape")
#
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")
#
radius = 10
pi = 3.14
area = pi * radius ** 2

message = "La zone d'un cercle avec le rayon {} est de {:.0f} mètres carrés.".format(radius, area)
print(message)
#
a = 8
b = 6
result = a + b

print("{} + {} = {}".format(a, b, result))