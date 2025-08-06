# #*map()*
# - Purpose: Transforms each item in an iterable.
# - Returns: A new iterable with the results.
# - Usage: When you want to apply a function to every element.

#  *filter()*
# - Purpose: Filters elements based on a condition.
# - Returns: Only the elements that meet the condition.
# - Usage: When you want to keep certain items.

# #reduce()
# - Purpose: Reduces a sequence to a single value.
# - Returns: One result by applying a function cumulatively.
# - Usage: When you want to combine all values into one.

# Higher-Order Function :Takes or returns a function 
# Closure    : Inner function that remembers the outer scope 
# Decorator  : Higher-order function to wrap/modify another function

#map 
def square(x):
    return x * x

numbers = [1, 2, 3, 4]
squared = map(square, numbers)
print(list(squared)) 

#filter
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
evens = filter(is_even, numbers)
print(list(evens))

#reduce
from functools import reduce
def add(x, y):
    return x + y

numbers = [1, 2, 3, 4]
total = reduce(add, numbers)
print(total)

# 
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark',
'Norway', 'Iceland']
for item in countries:
    print(item)
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for name in names:
    print(name)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)

from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
numbers = [1, 2, 3, 4, 5]
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

#to uppercase
countries_upper = list(map(str.upper, countries))

#Numbers to square
squares = list(map(lambda x: x**2, numbers))

#Names to uppercase
names_upper = list(map(str.upper, names))

#Countries with 'land'
countries_with_land = list(filter(lambda x: 'land' in x, countries))

#Countries with exactly six characters
six_char_countries = list(filter(lambda x: len(x) == 6, countries))

#Countries with six or more letters
six_or_more = list(filter(lambda x: len(x) >= 6, countries))

#Countries starting with 'E'
start_with_e = list(filter(lambda x: x.startswith('E'), countries))

#Chain map, filter, reduce (e.g., square even numbers and sum them)
chained = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, map(lambda x: x**2, numbers)))

#Function to return only string items
def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))

#Reduce to sum numbers
total_sum = reduce(lambda x, y: x + y, numbers)
#Reduce to create a sentence
sentence = reduce(lambda x, y: f"{x}, {y}", countries[:-1]) + f", and {countries[-1]} are north European countries"
#categorize_countries :
def categorize_countries(countries, pattern):
    return [country for country in countries if pattern.lower() in country.lower()]

categorize_countries(countries, 'land')  # ['Finland', 'Iceland', 'Switzerland', ...]

#Dictionnaire par lettre :
def countries_by_letter(countries):
    result = {}
    for country in countries:
        key = country[0].upper()
        result[key] = result.get(key, 0) + 1
    return result
#get_first_ten_countries :
def get_first_ten_countries(countries):
    return countries[:10]

#et_last_ten_countries :
from countries_data import countries_data

def get_last_ten_countries(countries):
    return countries[-10:]
countries_sorted_by_name = sorted(countries_data, key=lambda x: x['name'])
countries_sorted_by_capital = sorted(countries_data, key=lambda x: x['capital'] or '')
                                     
countries_sorted_by_population = sorted(countries_data, key=lambda x: x['population'], reverse=True)

# 10 most spoken languages :

from collections import Counter

def most_spoken_languages(data, top_n=10):
    langs = []
    for c in data:
        langs.extend(c['languages'])
    return Counter(langs).most_common(top_n)

#10 most populated countries :

def most_populated_countries(data, top_n=10):
    return sorted(data, key=lambda x: x['population'], reverse=True)[:top_n]