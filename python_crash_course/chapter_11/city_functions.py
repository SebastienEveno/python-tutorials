def city_country(city_name, country_name, pop=0):
    if pop:
        return f"{city_name.title()}, {country_name.title()} - population {pop}"
    else:
        return f"{city_name.title()}, {country_name.title()}"