dict_list ={}
dict_chien = {'nom':'bolt', 'couleur':'noire', 'race':'rottweiler', 'jambes':'longue', 'âge':3}
dict_etudiant = {'first_name':'abalo', 'last_name':'FAFA', 'sexe':'masculain', 'âge':20, 'etat_matrimoniale':'célibataire', 'compétences':'dévéloppeur', 'pays':'Togo', 'ville':'Lome', 'adresse':'Djifa-kpota'}
print('la longueur de dictionnaire etudiant :',len(dict_etudiant))
print("la valeurs du dictionnaires etudiants comme une liste :",dict_etudiant.values()) 
print("la valeurs du dictionnaire chien comme une liste :",dict_chien.values())
print("le dictionnaires etudiants en liste de tuple :",dict_etudiant.items())
print("la dictionnaires chien en liste de tuples :",dict_chien.items())
print("suppression d'un des élément du dictionnaires etudiants :",dict_etudiant.popitem())
del dict_chien