import pokebase as pb
import requests
import re

def print_location(data):
    if isinstance(data, dict):
        # If the data is a dictionary, iterate over the key-value pairs
        for key, value in data.items():
            # Recursively check nested dictionaries
            if isinstance(value, (dict, list)):
                print_location(value)
            elif value and key != "url":  # Print if value is not None or False
                if key == "chance":
                    print("\n")
                    print(f"{key}: {value}")
                else:
                    print(f"{key}: {value}")
                
    elif isinstance(data, list):
        # If the data is a list, iterate over each item
        for item in data:
            if key == "chance":
                print("\n")
                print_location(item)
            else:
                print_location(item)
            
def print_non_empty(data):
    if isinstance(data, dict):
        # If the data is a dictionary, iterate over the key-value pairs
        for key, value in data.items():
            # Recursively check nested dictionaries
            if isinstance(value, (dict, list)):
                print_non_empty(value)
            elif value and key != "url" and key != "slot":  # Print if value is not None or False
                print(f"{key}: {value}")

    elif isinstance(data, list):
        # If the data is a list, iterate over each item
        for item in data:
            print_non_empty(item)

def evolution(pokemon):
    url = "https://pokeapi.co/api/v2/pokemon-species/" + pokemon

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        url = data["evolution_chain"]["url"]

        response = requests.get(url)
    
        if response.status_code == 200:
            data = response.json()
            print_non_empty(data)

        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

    return url

def generation(pokemon):
    url = "https://pokeapi.co/api/v2/pokemon-species/" + pokemon

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(data["generation"]["name"])

def location(pokemon):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon + "/encounters"

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print_non_empty(data)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

def stats(pokemon):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print_non_empty(data["stats"])

def nature_lookup(nature):
    url = "https://pokeapi.co/api/v2/nature/" + nature

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Increased:  {data['increased_stat']['name']}")
        print(f"Decreased:  {data['decreased_stat']['name']}")

def pokemon_abilities(pokemon_ability):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_ability

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print_non_empty(data["abilities"])

def abilities(ability):
    url = "https://pokeapi.co/api/v2/ability/" + ability

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print_non_empty(data)


def menu():
    #natures = ['hardy','lonely','adamant','naughty','brave','bold','docile','impish','lax','relaxed','modest','mild','bashful','rash','quiet','calm','gentle','careful','quirky','sassy','timid','hasty','jolly','naive','serious']

    user_input = input("What do you want to know?\n\n1.Pokemon\n2.Abilities\n3.Nature: \n\n")

    if re.search(r'[^1-3]', user_input):
        menu()
    elif user_input == "1":
        pokemon = input("Enter Pokemon name: ")
        info = input("1. Evolution: \n2. Generation: \n3. Stats\n4. Location\n5. Ability\n\n")
        if re.search(r'[^1-5]', user_input):
            menu()
        elif info == "1":  
            (evolution(pokemon))
        elif info == "2":
            (generation(pokemon))
        elif info == "3":
            (stats(pokemon))
        elif info == "4":
            (location(pokemon))
        elif info == "5":
            (pokemon_abilities(pokemon))
    elif user_input == "2":
        ability = input("Enter an ability: \n\n")
        abilities(ability)
    elif user_input == "3":
        nature = input("Enter a nature: \n\n")
        nature_lookup(nature)
    else:
        menu()

menu()