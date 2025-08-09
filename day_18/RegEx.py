# the most frequent word in the following paragraph
import re
paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."
words = re.findall(r'\b\w+\b', paragraph.lower())
word_count = {}
for word in words:
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1
most_frequent_word = max(word_count, key=word_count.get)
print(f"({word_count}, {most_frequent_word})")
#positions 
text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

#Extraire tous les nombres entiers (positifs et négatifs)
positions = list(map(int, re.findall(r'-?\d+', text)))

#Trouver la distance entre les deux particules les plus éloignées
distance = max(positions) - min(positions)

print("Points:", positions)
print("sorted_points :", sorted(positions))
print("Distance :", distance)
# 
def is_valid_variable(var_name):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*'
    return bool(re.match(pattern, var_name))
print(is_valid_variable("first_name"))
print(is_valid_variable("first-name"))
print(is_valid_variable("1first_name"))
print(is_valid_variable("firstname"))
#cleaning text
from collections import Counter
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve
%tea@ching%;. There $is nothing; &as& mo@re rewarding as
educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching
m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s
mo@tivate yo@u to be a tea@cher!?'''
cleaned_sentence = re.sub(r'[%$@&#;]', '', sentence)
cleaned_sentence = re.sub(r'\s+', ' ', cleaned_sentence).strip()
print(cleaned_sentence)
word_counts = Counter(words)
most_common = word_counts.most_common(3)

print(most_common)
