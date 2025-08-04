#filters only negative numbers from a list
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_numbers = [ i for i in numbers if i < 0 ]
print(negative_numbers)
print("\n")
# flatten a list of lists

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [ numbers for row in list_of_lists for numbers in row ]
print(flattened_list)
print("\n")
# list of tuples 
list = [(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(list)
print("\n")
# flatten a list to a new list
countries = [[('Finland', 'Helsinki')], [('Sweden','Stockholm')], [('Norway', 'Oslo')]]
output = [[c.upper(), c[:3].upper(), cap.upper()] for [(c, cap)] in countries]
print(output)
print("\n")
#list to a list of dictionaries
countries = [[('Finland', 'Helsinki')], [('Sweden','Stockholm')], [('Norway', 'Oslo')]]
countries_dict = [{'country': c, 'city': cap} for [(c, cap)] in countries]
print(countries_dict)
print("\n")
# change a list of lists to a list of concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],[('Donald', 'Trump')], [('Bill', 'Gates')]]
names_concatenated = [f"{first} {last}" for [(first, last)] in names]
print(names_concatenated)
#lamda function 
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
print(slope(2, 3, 10, 8))