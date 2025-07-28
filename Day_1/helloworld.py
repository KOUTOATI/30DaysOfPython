# version de python
import sys
print(" la version de votre python est ",sys.version)

# quelques opération 

print("3 + 4 = ",3 + 4)
print("3 - 4 = ",3 - 4)
print("3 % 4 = ",3 % 4)
print("3 / 4 = ",3 / 4)
print("3 ** 4 = ",3 ** 4)
print("3 / 4 = ",3 // 4)
# Présentation 

print("Je me nome paulin kossi KOUTOATI je suis  togolais et je viens du Togo, je profite de 30 jours de python")

#vérification des types de données 

print("10 est de type",type(10))
print("9.8 est de type",type(9.8))
print("3.14 est de type",type(3.14))
print("4 - 4j est de type",type(4 - 4j))
print("['As abeneh','Python','Finlande'] est de type ",type([' As abeneh','Python','Finlande']))
print("'kossi Paulin 'est de type de ",type('Kossi paulin'))
print("'KOUTOATI' est de type ",type('KOUTOATI'))
print("'Togo' est de type ",type('Togo'))

# donnons des exemple pour les différents type de données Python

print("entier : 10, float = 6.22, complexe =  2 + 5j , String : ' python' , Boolean: True , List : ['python ', 'est' , 'un' ,'language ','de','programtion'],Tuple : (1,4,6,9), Set:{10.5, 4.5, 2.7}, dict : {'matiere' :'programation'}")

# distance euclidienne 
import math

print(f"distance entre (2,3) et (10,8) est de {math.sqrt(pow((10 - 2),2) + pow((8 - 3), 2)):.2f}")