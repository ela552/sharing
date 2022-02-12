favourite_places = {"liz": ["paris"],
                    "stellah": ["germany", "kenya"],
                    "vivian": ["zanzibar", "seychelles", "bali"],
                    }

for name, places in favourite_places.items():
    print("\n" + name.title() + "'s" + " " + "favourite places are:")
    for place in places:
        print("\t" + place.title())