countries = [
    {"name": "Kazakhstan", "capital": "Astana"},
    {"name": "Qatar", "capital": "Doha"},
    {"name": "France", "capital": "Paris"},
]
def func(countries):
    for country in countries:
        if country["name"] == "Qatar":
            return country["capital"]
print(func(countries))
