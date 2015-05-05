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
