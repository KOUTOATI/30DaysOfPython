import math

age : int 
taille : float
nombre : complex

base = int(input("entrez la base de votre triangle : "))
height = int(input("entrez la hauteur de votre triangle : "))
print(" la zone du triangle :", 0.5 * base * height," m²")


print("veuillez entrez les cotés de vos triangle : ")
A = int(input("le côté A : "))
B = int(input("le côté B :"))
C = int(input("le côté C :"))
print(" le périmetre de votre triangle est:", A + B + C," m")

#rectangle 

largeur = int(input(" entrez la largeur de votre rectangle : "))
longeur = int(input("entrez la longeur de vote rectangle : "))
print("la surface de ce rectangle est égal à ", largeur * longeur," m²")
print("le périmetre de ce rectangle est  égal à ",2 * (longeur + largeur)," m")

# cercle 

r = int(input(" entrezz le rayon de votre cercle : "))
print(" la zone de ce cercle est égal à : ",math.pi * r * r," m²")
print("la circonférence de ce cercle est de : ", 2 * math.pi * r," m")

# les points
m1 = -2
def equation_point(x):
    return 2*x - 2

print("la pente  :", m1 )
print("ordonné x a l'origine : ",(2+0)/2)
print("y a l'origine : ", equation_point(0))
# pour les point (2,2) et ( 6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
m2 = ((y2 - y1)/(x2 - x1))
print("la pente de ces points est  :",m2)
print(" la distance euclidienne entre ces deux points : ",math.sqrt(pow((x2 - x1),2) + pow((y2 - y1),2)))
# comparaison des pentes 
print(" m1 > m2", m1 > m2)

# equation de second dégré 
a = 1
b = 6
c = 9
delta = (b*b) - (4*a*c)
if (math.sqrt(delta > 0)):
    x0 = (-b + (math.sqrt(delta))) / 2*a
elif(math.sqrt(delta) == 0):
    x0 = -b / 2 * a

print(" y = ",pow(x0 ,2) + (6 * x0) + 9)

for x in range(-10, 11):  # Valeurs de x de -10 à 10
    y = x**2 + 6*x + 9
    print(f"x = {x}, y = {y}")
    if y == 0:
        print(f"y est nul quand x = {x}")
        break

#comparaison 

long1 = len('python')
long2 = len('Dragon')
print("longueur de 'Python' : ",long1)
print("longueur de ' Dragon' : ",long2)
print(long1 == long2 and 'Python' in 'Dragon')

print('n' in 'python' and 'dragon')
print('jargon' in ' i hope this course is not full of jargon')
print('on' not in  'python' and 'dragon')
print("'Python converti en flotter :",float(len('Python')))
print(7 // 3 == int(2.7))
print(type('10') == type(10))
print(int(9.8) == 10)


# entrer au clavier 

h = int(input(" entrez les heures  : "))
th = int(input("entrez le taux d'heure : "))
print("votre gain hebdomadaire est de  ",h * th)

ans = int(input("entrez le nombre d'année que vous avez vécu : "))
print(" vous vivez pendant ",th *365 * 24 * 60 * 60 ," secondes ")

# tableau 
for i in range (1, 6):
    print(f"{i} {1} {i} {i * 2} {i * 3}") 