import requests
import json

# file_path = 'country.json'

# file = open()
url = "https://raw.githubusercontent.com/awasekhirni/jsondata/9f3fa44f8350374a3ef1a9405175e2054ed3a96e/100books.json"

json_data = requests.get(url)
result = json_data.json()
# print(result)
# json_string = json.dumps(result)
# print(type(result))
# print(type(result[4]))
# x = list(result)

country_list={}

for i in result:
    country = i.pop("country")
    if country not in country_list:
        country_list[country] = [i]
    else:
        country_list[country].append(i)

con = list(country_list.keys())
con.sort()
sorted_country = {i : country_list[i] for i in con}
print(sorted_country)
# print(sorted(country_list))

# file_path = "country.json"

# with open(file_path, 'w') as json_file:
#     json.dump(sorted_country, json_file, indent=4)

# x = filter(lambda a: a["country"] == "denmark", result)