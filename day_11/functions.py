# functions
def add_two_numbers(a, b):
   return a + b

# functions for circle area
def circle_area(rayon):
   return 3.14 * rayon * rayon

# functions 
def add_all_nums(*args):
   total = 0
   for num in args:
      total += num
   return total

def add_all_nums(*args):
    if all(isinstance(arg, (int, float)) for arg in args):
        return sum(args)
    else:
        return "tout les arguments ne sont pas des nombres"
    
    #
def covert_celcuis_to_fahrenheit(celcius):
    return (celcius * 9/5) + 32  

#

def checked_season(month):
    if month in [12, 1, 2]:
        return "Hiver"
    elif month in [3, 4, 5]:
        return "Printemps"
    elif month in [6, 7, 8]:
        return "Été"
    elif month in [9, 10, 11]:
        return "Automne"
    else:
        return "Mois invalide"
    
# function calculate_slope
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "La pente est indéfinie (division par zéro)"
    return (y2 - y1) / (x2 - x1)

# function to solve quadratic equations
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "Pas de solution réelle"
    elif discriminant == 0:
        x = -b / (2*a)
        return f"Une solution réelle: x = {x}"
    else:
        sqrt_discriminant = discriminant**0.5
        x1 = (-b + sqrt_discriminant) / (2*a)
        x2 = (-b - sqrt_discriminant) / (2*a)
        return f"Deux solutions réelles: x1 = {x1}, x2 = {x2}"

# function which take a list and print each element
def print_list_elements(lst):
    if not isinstance(lst, list):
        return "L'argument doit être une liste"
    for index, element in enumerate(lst):
        print(f"Élément {index + 1}: {element}")
    return "Tous les éléments ont été imprimés"

# function which takes listand return the inverse of the array
def reverse_list(lst):
    if not isinstance(lst, list):
        return "L'argument doit être une liste"
    return lst[::-1]

# function capiralize_list_elements
def capitalize_list_elements(lst):  
    if not isinstance(lst, list):
        return "L'argument doit être une liste"
    return [str(element).capitalize() for element in lst]

#function add_item_to_list
def add_item_to_list(lst, item):
    if not isinstance(lst, list):
        return "L'argument doit être une liste"
    print(lst.append(item))
    return lst

#function remove_item_from_list
def remove_item_from_list(lst, item):
    if not isinstance(lst, list):
        return "L'argument doit être une liste"
    if item in lst:
        print(lst.remove(item))
        return lst
    else:
        return "L'élément n'est pas dans la liste"
    
    #function sum_of_numbers
def sum_of_numbers(number):
    sum = 0
    for i in range(number):
        sum += i
    return sum
#function add_odd_numbers
def add_odd_numbers(number):
    sum = 0
    for i in range(number):
        if i % 2 != 0:
            sum += i
    return sum

#function sun_of_even_numbers
def sum_of_even_numbers(number):
    sum = 0
    for i in range(number):
        if i % 2 == 0:
            sum += i
    return sum

#function even_and_odd_numbers
def even_and_odd_numbers(number):
    even_numbers = []
    odd_numbers = []
    for i in range(number):
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
    return {"the number of evens are ": even_numbers, "the number of odds are ": odd_numbers}

#function factorial
def factorial(number):
    if number < 0:
        return "Le facteur n'est pas défini pour les nombres négatifs"
    elif number == 0 or number == 1:
        return 1
    else:
        result = 1
        for i in range(2, number + 1):
            result *= i
        return result
    
#function is_empty
def is_empty(param):
    if not param:
        return True
    return False

#functions
import statistics

def calculate_mean(data):
    return sum(data) / len(data)

def calculate_median(data):
    return statistics.median(data)

def calculate_mode(data):
    return statistics.mode(data)

def calculate_range(data):
    return max(data) - min(data)

def calculate_variance(data):
    return statistics.variance(data)

def calculate_std(data):
    return statistics.stdev(data)

## function is_prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True 

# function_unique_elements
def unique_elements(lst):
    return len(lst) == len(set(lst))
# function same type
def all_same_type(lst):
    if not lst:
        return True
    first_type = type(lst[0])
    return all(type(item) == first_type for item in lst)

# function check valid_python_variable
import re
def is_valid_python_variable(variable_name):
    if not isinstance(variable_name, str):
        return False
    if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', variable_name):
        return True
    return False

# data_file
from countries_data import countries_data
from collections import Counter

def most_spoken_languages(countries, top_n=10):
    language_counter = Counter()
    for country in countries:
        for lang in country['languages']:
            language_counter[lang] += 1
    return language_counter.most_common(top_n)

# function most_populated countries
def most_populated_countries(countries, top_n=10):
    sorted_countries = sorted(countries, key=lambda x: x['population'], reverse=True)
    return [{'country': c['name'], 'population': c['population']} for c in sorted_countries[:top_n]]
