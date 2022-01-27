# from english_words import english_words_set
import csv
places_list =[]
with open('places.txt','r',encoding='utf8') as p:
    places_list = p.read().lower().split('\n')

with open('world-cities_csv.csv', 'r',encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        places_list.append(line[0].lower())

animals_list = []
with open('animals.txt', 'r') as a:
    animals_list = a.read().lower().split('\n')

print('yavatmal' in places_list)
# print(len(places_list))