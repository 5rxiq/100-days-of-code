travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇


def add_new_country(country_name, visit_count, city_names):

# my solution
  new_entry = {
    "country": country_name,
    "visits": visit_count,
    "cities": city_names
  }

# alternative solution
  new_country = {}
  new_country["country"] = country_name
  new_country["visits"] = visit_count
  new_country["cities"] = city_names

  travel_log.append(new_country)

# 🚨 Do not change the code below


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log[1])



