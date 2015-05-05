Experiment_1 = {'experiment name': "Strength vs photosyntesis capacity",
 'organisms': [{'category': 'Plants',
                               'number_of_organisms': 50,
                               'genes': {
                                     'strength': {
                                         'type': 'built-in function',
                                         'name': 'gaussian',
                                         'mean': 10, 
                                         'variance': 2},
                                     'photosynthesis_capacity': {
                                         'type': 'built-in function',
                                         'name': 'uniform distribution',
                                         'interval': [10, 30] }},
                               'status': {
                                     'energy_reserve': 100.0} 
                              },
               {'category': 'Animals',
                               'number_of_organisms': 50,
                               'genes': {
                                     'strength': 10,
                                     'speed': {
						'type': 'built-in function',
						'name': 'discrete distribution',
						'values': [
							{'value': 0.0, 'probability': 0.25},
							{'value': 1.0, 'probability': 0.70},
							{'value': 5.0, 'probability': 0.05}] }	},  
                               'status': {
                                     'energy_reserve': 100}
                               }
              ],

  'outlays': {
              'hunting': {
			'type': 'built-in function',
			'name': 'linear function',
			'terms': [
				{'parameter': 'strength', 'coefficient': 3.0}, 
                 		{'parameter': 'speed', 'coefficient': 0.2}, 
                       	{'parameter': None, 'coefficient': 5.0}]},
              'moving': {
			'type': 'built-in function',
			'name': 'linear function',
			'terms': [
				{'parameter': 'strength', 'coefficient': 1.0}, 
                         	{'parameter': 'photosynthesis_capacity', 'coefficient': 25.0}, 
                       	{'parameter': 'speed', 'coefficient': 5.0}, 
                       	{'parameter': None, 'coefficient': 1.0}]},
              'procreating': {
			'type': 'built-in function',
			'name': 'linear function',
			'terms': [
				{'parameter': 'strength', 'coefficient': 3.0}, 
                      	{'parameter': 'photosynthesis_capacity', 'coefficient': 3.0}, 
                       	{'parameter': 'speed', 'coefficient': 3.0}, 
                         	{'parameter': None, 'coefficient': 5.0}]},
	        'living': {
			'type': 'la vida loca',
			'name': 'linear function',
			'terms': [
				{'parameter': 'strength', 'coefficient': 1.0}, 
                        	{'parameter': 'photosynthesis_capacity', 'coefficient': -1.0},
                      	{'parameter': 'speed', 'coefficient': 2.0}, 
                      	{'parameter': None, 'coefficient': 5.0}]}
              },

  'constraints': {
   	'procreating': {
		'type': 'interpreted function',
		'name': 'organism constraint',
		'a': 'energy_reserve',
		'r': ('random number', 'uniform_distribution [0, 1]'),
		'expression': "a*r > 100.0"  },
 	'hunting': {
		'type': 'interpreted function',
		'name': 'compare_predator_vs_prey',
		'a': ('predator', 'strength'),
		'b': ('prey', 'strength'),
		'r1': ('random number', 'uniform_distribution [0, 1]'),
		'r2': ('random number', 'uniform_distribution [0, 1]'),
		'expression': "a*r1 > b*r2"  },
	'dying': {
		'type': 'built-in function',
		'name': 'death_because_of_low_energy',
		'minimun_level_of_energy': 10.0
		} },

  'mutability': {
	'strength': {
		'increments': {
			'type': 'built-in function',
			'name': 'gaussian',
			'mean': 0.0, 
			'variance': 0.01},
		'mutation_frequency': 0.05,
		'allowed_interval': [0, 'infinity']
		
		},
	'photosynthesis_capacity': {
		'increments': {
			'type': 'built-in function',
			'name': 'gaussian',
			'mean': 0.0, 
			'variance': 0.15},
		'mutation_frequency': 0.001
		}  
  	}
}


# Default experiment		(Estos son los valores por defecto)											
Default_experiment = {'experiment name': "Experiment name",
 'biotope': {
	'size': (100, 200),
	'substances': None },
 'organisms': [{'category': 'General_category',
       'number_of_organisms': 10,
       'genes': {
		'speed': 0.0,
		'mutation_frequency': 1.0
		},
    	'status': {
  		'coordinates': {
			'type': 'Biotope call',
			'name': 'seek_free_position'}
		} }],
  'outlays': { },
  'constraints': { },
  'mutability': { }
}



Experiment_2	 = {
    'organisms': [
	{'category': 'Mutants',
		'genes': {
            		'strength': 'default',
                   	'photosynthesis_capacity': 20.0,
                 	'speed': {
				'type': 'built-in function',
				'name': 'discrete distribution',
				'value_list': [
					{'value': 0.0, 'frequency': 0.25},
					{'value': 1.0, 'frequency': 0.75}]},  
			'generation': 0 ,
                   	'mutation_frequency': 0.1},
		'status': {
                 	'energy_reserve': 100.0} },
	{'category': 'No_Mutants',
		'genes': {
            		'strength': 'default',
                   	'photosynthesis_capacity': 20.0,
                 	'speed': {
				'type': 'built-in function',
				'name': 'discrete distribution',
				'value_list': [
					{'value': 0.0, 'frequency': 0.25},
					{'value': 1.0, 'frequency': 0.75}]},  
			'generation': 0,
                   	'mutation_frequency': 0.0},
		'status': {
                    'energy_reserve': 100.0} }],
  'outlays': {
	'load outlays': "/Pepito/Experiments/cool experiment.exp" },
  'constraints': {},
  'mutability': {
	'strength': {
		'percentage_increments': {
			'type': 'built-in function',
			'name': 'gaussian',
			'mean': 0.0, 
			'variance': 0.01},
		'mutation_frequency': 0.05,
		'allowed_interval': [0, 'infinity']	
		},
	'speed': {
		'type': 'probabilistic_automaton',
		'states': {0.0, 1.0},
		'probabilities_matrix': [
			[0.99, 0.01],
			[0.02, 0.98]] },
	'generation': {
		'increments': 1},

	'mutability': {
		'percentage_increments': {
			'type': 'built-in function',
			'name': 'gaussian',
			'mean': 0.0, 
			'variance': 0.01},
		'allowed_interval': [0, 1]
		}
  	}
}

# Nota: En este experimento veremos si los mutantes ganan a los no mutantes en la 
# guerra por la supervivencia 


Experiment_3 = {
    'organisms': [
	{'genes': {
            	'attack_capacity': { 
			'type': 'built-in function',
			'name': 'chi-squared',
			'k': 3},
            	'defense_capacity': { 
			'type': 'built-in function',
			'name': 'chi-squared',
			'k': 3},
             	'photosynthesis_capacity': 20.0,
		'energy_reserve_at_birth': 100.0,
		'minimun_energy_reserve_at_procreation': 200.0},
	'status': { 'energy_reserve': 200.0} }],
'outlays': {
	'load outlays': "/Pepito/Experiments/cool experiment 2.exp",
	'living': {
		'type': 'built-in function',
		'name': 'n-linear function',
		'terms': [
			{'parameters': ['attack_capacity', 'defense_capacity'], 		'coefficient': 1.0}, 
                  	{'parameters': ['photosynthesis_capacity'], 				'coefficient': -1.0},
			{'parameters': ['attack_capacity', 'photosynthesis_capacity'], 	'coefficient': 25.0}, 
			{'parameters': [], 								'coefficient': 0.5}]} },
'constraints': {
   	'procreating': {
		'type': 'threshold',
		'parameter': 'energy_reserve',
		'threshold': 'minimun_energy_reserve_at_procreation'},
	'hunting': {
		'type': 'interpreted function',
		'name': 'compare_predator_vs_prey',
		'a': ('predator', 'attack_capacity'),
		'b': ('prey', 'defense_capacity'),
		'r1': ('random number', 'uniform_distribution [0, 1]'),
		'r2': ('random number', 'uniform_distribution [0, 1]'),
		'expression': "a*r1 > b*r2"  } },
  'mutability': {
	'all genes': {
		'percentage_increments': {
			'type': 'built-in function',
			'name': 'gaussian',
			'mean': 0.0, 
			'variance': 0.01},
		'mutation_frequency': 0.05,
		'allowed_interval': [0, 'infinity']	}
	}
}

# Nota: En este experimento veremos si los mutantes ganan a los no mutantes en la 
# guerra por la supervivencia 




def print_Experiment(Experiment, indent_level = 0):
    if type(Experiment) == dict:
        print "    "*indent_level, '{' # This line could be removed
        for key in Experiment.keys():
            if hasattr(Experiment[key], '__iter__'):
                print "    "*indent_level, str(key)+":"
                print_Experiment(Experiment[key], indent_level + 1)
            else:
                print "    "*indent_level, str(key)+": ", Experiment[key]  
        print "    "*indent_level, '}' # This line also could be removed
    elif hasattr(Experiment, '__iter__'):
        for element in Experiment:
            print_Experiment(element, indent_level + 1)
    else:
        print "   "*indent_level, Experiment
    
    
for E in (Default_experiment, Experiment_1, Experiment_2, Experiment_3):
    print "\n\n\n"
    print_Experiment(E)
    




