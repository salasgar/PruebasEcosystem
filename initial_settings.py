# inviduals and biotope creation

from random import random

# Creation of biotope
BIOTOPE_SIZE_X = 100
BIOTOPE_SIZE_Y = 100

# Creation of inviduals
REPRODUCTION_FREQUENCY = 0.1
GLOBAL_LONGEVITY = 0.2
GLOBAL_PHOTOSYNTHESIS_CAPACITY = 5.0

initial_organisms = []

N = 10 # Number of initial organisms of the following kind:
organism_data = {'genes': {'attack_capacity':  random() * 5.0,
                           'defense_capacity': random() * 100.0,
                           'speed': 0.0,
                           'do_photosynthesis': True},
                 'status': {'energy_reserve': 100,
                            'age': 0}
                }
initial_organisms.append((N, organism_data))

N = 100 # Number of initial organisms of the following kind:
organism_data = {'genes': {'attack_capacity':  random() * 100.0,
                           'defense_capacity': random() * 30.0,
                           'speed': 4.0,
                           'do_photosynthesis': False},
                 'status': {'energy_reserve': 100,
                            'age': 0}
                }
initial_organisms.append((N, organism_data))
    
