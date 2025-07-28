#Jour2: 30 Days of Python Programming
prenom = 'Kossi Paulin'
nom_de_famille = 'KOUTOATI'
nom_complet = 'KOUTOATI Kossi Paulin'
pays = 'Togo'
municipale = 'bê'
an = 21
est_Married = False
is_true = True
IS_light_on = True
a, b, c = 4, 5, 6
# vérificaation des types de données 
print(f"{prenom}",type(prenom))
print(f"{nom_de_famille}",type(nom_de_famille))
print(f"{nom_complet}",type(nom_complet))
print(f"{pays}",type(pays))
print(f"{municipale}",type(municipale))
print(f"{an}",type(an))
print(f"{est_Married}",type(est_Married))
print(f"{is_true}",type(is_true))
print(f"{IS_light_on}",type(IS_light_on))
print(f"{a,b,c}",type(a))
#trouvons la longueur 

print(f"la longeur de {prenom} est ",len(prenom))
print(f"la longeur de {prenom} est de {len(prenom)} et la lonngeur de {nom_de_famille} est de {len(nom_de_famille)}")

num_one = 5
num_two = 4
sum = num_one + num_two
soustraire = sum - num_one
produit = num_one * num_two
division = num_one / num_two
reste = num_two % num_one
floor_division = num_one // num_two
print(f"{num_one} + {num_two} = ",sum)
print(f"{num_one} - {num_two} = ",soustraire)
print(f"{num_one} * {num_two} = ",produit)
print(f"{num_one} / {num_two}", division)
print(f"{num_two} % {num_two} = ",reste)
print(f"{num_one} // {num_two} = ",floor_division)
# calcule sur un cercle 
import math
rayon = int(input("entrer le rayon de votre cercle : "))
area_of_circle = math.pi * pow(rayon, 2)
circum_of_circle = math.pi * rayon * 2 
print("la zone de votre cercle est de : ",area_of_circle)
print("la circonférence de votre cercle est de : ",circum_of_circle)


# entrer des données 

prenom = input("entrez votre prenom  : ")
nom_de_famille = input("entrer votre nom de famille : ")
pays = input("entrez votre pays : ")
an = input(" entrez votre âge : ")
# affichage 
print(f"vous vous appelez {nom_de_famille} {prenom} , vous avez {an} ans et votre pays est {pays}")

import keyword
print(keyword.kwlist)