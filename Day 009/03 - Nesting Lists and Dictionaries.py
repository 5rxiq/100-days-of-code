captials = {
    "France": "Paris",
    "Germany": "Berline",
}

#nesting a list in a dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg","Stuttgart"],
}

#nesting dictionary in a dictionary 
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 14},
    "Germany": {"cities_visited": ["Berlin", "Hamburg","Stuttgart"], "total_visits": 87},
}

#nesting dictionary in a list
travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 14
    },

    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg","Stuttgart"], 
        "total_visits": 87
    },
]