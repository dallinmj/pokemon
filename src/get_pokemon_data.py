# This script collects Pokemon data from the PokeAPI and saves it as a CSV file.

import requests
import pandas as pd
import time

# Base API URL
BASE_URL = "https://pokeapi.co/api/v2/pokemon"

# List to store our Pokemon data
pokemon_list = []

# Collect the pokemon
for pokemon_id in range(1, 1025):

    url = f"{BASE_URL}/{pokemon_id}"

    response = requests.get(url)

    # Response to JSON
    data = response.json()

    # Extract the fields we want
    pokemon_info = {
        "id": data["id"],
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "primary_type": data["types"][0]["type"]["name"],

        "hp": data["stats"][0]["base_stat"],
        "attack": data["stats"][1]["base_stat"],
        "defense": data["stats"][2]["base_stat"],
        "special_attack": data["stats"][3]["base_stat"],
        "special_defense": data["stats"][4]["base_stat"],
        "speed": data["stats"][5]["base_stat"]
    }

    # Add Pokemon to list
    pokemon_list.append(pokemon_info)

    print(f"Collected data for {data['name']}")

    # Small delay
    time.sleep(0.03)

# Convert the list into a pandas DataFrame
df = pd.DataFrame(pokemon_list)

# Save the dataset to a CSV file
df.to_csv("data/pokemon.csv", index=False)

print("\nDataset saved to data/pokemon.csv")
print(f"Dataset shape: {df.shape}")
print(df.head())