import json


with open('working_json_files/countries.json', 'r') as json_file:
    json_datas = json.load(json_file)

my_lst = []
for country in json_datas:
    if 'A' in country.get('code'):
        my_lst.append(country)

print(my_lst)
print(len(my_lst))

data = {'name': 'Iraq', 'code': 'IQ'}
json_datas.append(data)

with open('working_json_files/countries.json', 'w') as json_file:
    json.dump(json_datas, json_file, indent=4)
