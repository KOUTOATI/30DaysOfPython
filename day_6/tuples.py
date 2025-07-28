list_tuple = ()
tuple_freres = ('komla', 'Kossi', 'Kodjo', 'kokou')
tuples_soeurs = ('Ayélé', 'Amélé', 'Adjo')
tuple_freres_soeurs = tuple_freres + tuples_soeurs
print(tuple_freres_soeurs)
print(" le nombres de frere et soeur que j'ai est de : ",len(tuple_freres_soeurs))
Family_Menbers = list(tuple_freres_soeurs)
print(type(Family_Menbers))
Family_Menbers.insert(len(Family_Menbers) + 1, "Ayawavi")
Family_Menbers.insert(len(tuple_freres_soeurs) + 2, "Koffi")
print(Family_Menbers)
#
print("freres et soeur : ",Family_Menbers[:7])
print("pere : ",Family_Menbers[-1])
print("mere : ",Family_Menbers[-2])

fruits = ('orange', 'mangue', 'banane', 'pomme', 'grenade')
legumes = ('salade', 'choux', 'laitue', 'poivre')
produits = ('saucice', 'sardines', 'paté')
Food_Stuff_TP = fruits + legumes + produits
Food_Stuff_LT = list(Food_Stuff_TP)
print(Food_Stuff_LT)
milieu = len(Food_Stuff_LT) // 2

if (milieu % 2 == 0):
    print("milieu :",Food_Stuff_LT[milieu - 1:milieu + 1])
else:
    print(Food_Stuff_LT[milieu])
print("les 3 premier :",Food_Stuff_LT[:3])
print("les 3 derniers :",Food_Stuff_LT[-3:])
del Food_Stuff_LT
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway','Sweden')
print('estonie' in nordic_countries)
print('Iceland' in nordic_countries)


