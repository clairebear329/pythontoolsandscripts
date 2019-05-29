
##This file contains some example tools to do calculations with planets' information.


'''This function will generate the estimated mass of a Solar System planet given the name of the planet (first letter capitalized), a dictionary of planetary radii, and a dictionary of planet density'''

import numpy as np

planet_radii_km = {'Mercury': 2439.7, 'Venus': 6051.8, 'Earth': 6371.0, 'Mars': 3396.2, 'Jupiter': 69911, 'Saturn':60268, 'Uranus': 25559, 'Neptune': 24764}

planet_densities_kgpkm = {'Mercury': 5.427e12, 'Venus': 5.243e12, 'Earth': 5.51e12, 'Mars': 3.933e12, 'Jupiter': 1.326e12, 'Saturn': 6.87e11, 'Uranus': 1.271e12, 'Neptune': 1.638e12}

p_name = input("Enter a planet name to calculate mass:")

def get_planet_mass_from_dictionary(p_name, dictionary_of_radii, planet_density):
     radius_planet = dictionary_of_radii[p_name]
     p_mass = (4/3 * np.pi * radius_planet**3)*planet_density[p_name]
     new_planet_mass[p_name] = p_mass
     print(p_name,' is ',p_mass,' kg.')

print(get_planet_mass_from_dictionary(p_name, planet_radii_km, planet_densities_kgpkm))
