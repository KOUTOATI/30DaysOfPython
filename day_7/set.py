#sets 
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26} 
B = {19, 22,20, 25, 26, 24, 28, 27} 
Âge = [22, 19, 24,25, 26, 24, 25, 24]
#
print("la longueur de l'ensemble it_companies : ",len(it_companies))
it_companies.add('Twitter')
print("le set apres le premier ajout :",it_companies)
it_companies.update(['Tesla', 'Meta', 'intel', 'Cisco'])
print("le set apres ajout :",it_companies)
it_companies.pop()
print("le set apres la suppression :",it_companies)
# la différence entre supprimé et rejeter est quand on rejete un élément on peut le renvoyé , alors que quand on supprime l'élément diqparait en même temps 

# rejoignons A et B

print("A ajouter a B donne:",A.union(B))
print("l'intersection de B et A donne :", A.intersection(B))
print("A est il un sous ensemble de B ? :",A.issubset(B))
print("A et  b sont ils disjoint ? :", A.isdisjoint(B))
print("rejoignons A avec B :", A.union(B))
print("rekoignons B avec A :",B.union(A))
print("la différence symétrique entre A et b :",A.symmetric_difference(B))
del A
del B

#
print("la a longueur de la liste  :",len(Âge))
set_Âge = set(Âge)
print("la longueur de l'ensemble :",len(set_Âge))
if (len(set_Âge) > len(Âge)):
    print("l'ensemble est plus grand")
elif((set_Âge) == len(Âge)):
    print("le deux ont les mêmes longueur ")
else:
    print("la liste est plus grand")

# une chaîne est tout type de donné écrit en texte
# une liste est une collection d'objet ordonnée, modifiable , indexé et qui permet des menbres en doublons
# un tuple est est collection d'objet ordonné , non modifiable , indexé et permet de menbres en doublons 
#un set est une collection d'objet non ordonné , non modifiable , non indexé et qui n'accepte pas des menbres en doubles 
phrase = 'i am a teacher and i love to inspire and teach people'
mots = phrase.split()
mots_uniques = set(mots)
print("le nombre de mots unique :",len(mots_uniques))
