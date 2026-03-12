# Pokémon Battle Stats Dataset

This repository contains code and data for a small data acquisition and analysis project using Pokémon battle statistics. The goal of the project is to collect Pokémon data from a public API and explore relationships between battle stats such as HP, attack, defense, and speed.

## Repository Structure

- **data/**
  - `pokemon.csv` — The final dataset containing Pokémon stats collected from the API.

- **src/**
  - `get_pokemon_data.py` — Python script used to request data from the PokéAPI and build the dataset.

- **notebook/**
  - `analysis.ipynb` — Jupyter notebook used for exploratory data analysis and visualizations.
  - `images/` — Saved plots used for analysis and reporting.

- **.gitignore**

## Data Source

All Pokémon data was collected from the public **PokéAPI**:

https://pokeapi.co/

## Project Overview

The project explores questions such as:

- How do Pokémon battle stats relate to one another?
- Do larger Pokémon tend to be stronger?
- Are certain Pokémon types faster or stronger on average?

The dataset contains over **1000 Pokémon** with attributes including height, weight, HP, attack, defense, special attack, special defense, and speed.
