cities = {
    "nairobi":{
        "country": "Kenya",
        "population": "34 million",
        "funfact": "swahili is the main language spoken",
    },
    "kampala":{
        "country": "Uganda",
        "population": "42 million",
        "funfact": "the city is built in a swamp",
    },
    "dar es salaam":{
        "country": "Tanzania",
        "population": "52 million",
        "funfact": "it is the end point of the oil pipeline",
    },
}
for city, city_info in cities.items():
    print("\ncity:" + " " + city.title())
    country = city_info["country"]
    population = city_info["population"]
    funfact = city_info["funfact"]

    print("\tcountry:" + " " + country)
    print("\tpopulation:" + " " + population)
    print("\tfunfact:" + " " + funfact)