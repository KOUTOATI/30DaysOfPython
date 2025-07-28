list = []
list1 = ['item1', 'item2','item3', 'item4', 'item5','item6']
print(len(list1))
print("premier :",list1[0])
print("milieu :",list1[len(list1)//2])
print("Dernier : ",list1[-1])
mixtes_data_types = ['KOUTOATI', 21, '1m80', 'etudiant', 'Lome Djifa-kpota']
IT_COMPANIES = ['Facebook', 'Google', 'Microsoft', 'Apple' 'IBM', 'Oracle', 'Amazon']
print(IT_COMPANIES)
print("nombre d'entreprise : ",len(IT_COMPANIES))
print("la premier societe :",IT_COMPANIES[0])
print("la societe moyenne : ",IT_COMPANIES[len(IT_COMPANIES)//2])
print("la dernierre societe : ",IT_COMPANIES[-1])
IT_COMPANIES[1] = 'Tesla'
print("liste modifié :",IT_COMPANIES)
IT_COMPANIES.append('linux')
IT_COMPANIES.insert(len(IT_COMPANIES)//2, 'Sony')
IT_COMPANIES[0] = 'Up it'
print('tesla' in IT_COMPANIES)
print(IT_COMPANIES.sort())
print(IT_COMPANIES.reverse())
print("3 premier :", IT_COMPANIES[:3])
print(" 3 derniers retiré : ",IT_COMPANIES[-3:])
print("socités du milieux ", IT_COMPANIES[1:-1])
print("dernier retiré :", IT_COMPANIES.pop())

front_end = ['html', 'css', 'js', 'react', 'redux']
back_end = ['node', 'express', 'mongodb']

full_stack = front_end + back_end
print(full_stack)
print(full_stack.insert(len(full_stack)+ 1,'Python'))
print(full_stack.insert(len(full_stack)+ 2,'SQL'))
print(full_stack.insert(len(full_stack)+ 3,'Redux'))
#
#Liste d'âges
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Trier la liste
ages.sort()
print("Âges triés :", ages)

#Âge min et max
min_age = min(ages)
max_age = max(ages)
print("Min :", min_age, "Max :", max_age)

#Ajouter min et max à la liste
ages.append(min_age)
ages.append(max_age)
print("Liste après ajout :", ages)

#Médiane
ages.sort()
n = len(ages)
if n % 2 == 0:
    median = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median = ages[n//2]
print("Médiane :", median)

#Moyenne
average = sum(ages) / len(ages)
print("Moyenne :", average)

#Plage
age_range = max(ages) - min(ages)
print("Plage d'âge :", age_range)

#Différences absolues
print("Différence |moyenne - médiane| :", abs(average - median))
print("Différence |moyenne - min| :", abs(average - min_age))
print("Différence |moyenne - max| :", abs(average - max_age))


# Trouver le(s) pays du milieu
countries = ["Chine", "Russie", "États-Unis", "Finlande", "Suède", "Norvège", "Danemark"]
n = len(countries)
middle = n // 2
if n % 2 == 0:
    print("Pays du milieu :", countries[middle - 1: middle + 1])
else:
    print("Pays du milieu :", countries[middle])

#Diviser en deux listes
first_half = countries[:middle + 1] if n % 2 else countries[:middle]
second_half = countries[middle + 1:] if n % 2 else countries[middle:]
print("1ère moitié :", first_half)
print("2ème moitié :", second_half)

#Regrouper les 3 premiers comme non-scandinaves, le reste comme scandinaves
non_scandinaves = countries[:3]
scandinaves = countries[3:]
print("Non-scandinaves :", non_scandinaves)
print("Scandinaves :", scandinaves)