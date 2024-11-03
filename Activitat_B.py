import pandas as pd
import matplotlib.pyplot as plt


file_path = 'List of world cities by population density.csv'
cities_data = pd.read_csv(file_path)

cities_data['Population'] = pd.to_numeric(cities_data['Population'].str.replace(r'\[.*\]', '', regex=True), errors='coerce')
cities_data['Area (km²)'] = pd.to_numeric(cities_data['Area (km²)'].str.replace(r'\[.*\]', '', regex=True), errors='coerce')

sample_cities_data = cities_data.head(10)

def show_total_population(cities_df):
    population_data = cities_df[['City', 'Population']].dropna()
    print(population_data)
    return population_data

def show_density_per_km2(cities_df):
    density_data = cities_df[['City', 'Density (/km²)']].dropna()
    print(density_data)
    return density_data

def show_density_per_m2(cities_df):
    cities_df['Density (/m²)'] = cities_df['Density (/km²)'] / 1e6
    density_m2_data = cities_df[['City', 'Density (/m²)']].dropna()
    print(density_m2_data)
    return density_m2_data

def main(cities_df):
    population_data = show_total_population(cities_df)
    density_km2_data = show_density_per_km2(cities_df)
    density_m2_data = show_density_per_m2(cities_df)
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    axes[0].pie(population_data['Population'], labels=population_data['City'], autopct='%1.1f%%')
    axes[0].set_title('Total Population by City')
    
    axes[1].pie(density_km2_data['Density (/km²)'], labels=density_km2_data['City'], autopct='%1.1f%%')
    axes[1].set_title('Population Density per km² by City')
    
    axes[2].pie(density_m2_data['Density (/m²)'], labels=density_m2_data['City'], autopct='%1.1f%%')
    axes[2].set_title('Population Density per m² by City')
    
    plt.tight_layout()
    plt.show()
main(sample_cities_data)
