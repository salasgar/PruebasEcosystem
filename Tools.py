import random
import math
import copy
import GUI
from Experiments import Experiment_1
from time import sleep

sRandom = lambda: 2*random() - 1  # Signed Random. From -1 to 1

class CoordinatesTupleClass:
    x, y = None, None
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __getitem__(self, key):
        if (key == 0) or (key =='x'): 
            return self.x
        else:
            return self.y
    def __setitem__(self, key, value):
        if (key == 0) or (key == 'x'): 
            self.x = value
        else:
            self.y = value
    def __str__(self):
        return u"({0}, {1})".format(self.x, self.y)

def coordinatesDict(coordTuple):
    return {'x': coordTuple[0], 'y': coordTuple[1]}
    
def coordinatesTuple(coordDict):
    return CoordinatesTupleClass(coordDict['x'], coordDict['y'])

def function_maker(operation):
    if operation['type'] == 'parameter':
        p = operation['value'] 
        return lambda organism: organism[p]
    elif operation['type'] == 'value':
        return lambda organism: operation['value']
    elif operation['type'] == 'operator':
        pass

    
def random_function_maker(function_dict):
    def choice_value(values, r):
        i = 0
        while r > values[i]['probability']:
            i += 1
        return values[i]['value']   
    if function_dict['type'] == 'built-in function':
        if function_dict['name'] == 'gaussian':
            mean = function_dict['mean']
            variance = function_dict['variance']
            return lambda: random.gauss(mean, variance)
        elif function_dict['name'] == 'uniform distribution':
            interval = function_dict['interval']
            return lambda: random.uniform(*interval)
        elif function_dict['name'] == 'discrete distribution':
            values = copy.deepcopy(function_dict['values'])
            total = 0
            for pair in values:
                total += pair['probability']
                pair['probability'] = total
            return lambda: choice_value(values, random.random())
        elif function_dict['name'] == 'chi-squared distribution':
            k = function_dict['k']
            coefficient = function_dict['coefficient']
            return lambda: coefficient * math.fsum(random.gauss(0, 1)**2 for i in range(k))
    return lambda: random.random()
    


print Experiment_1['experiment name']
strength_function_dict = Experiment_1['organisms'][0]['genes']['strength']
strength_function = random_function_maker(strength_function_dict)
photosynthesis_function_dict = Experiment_1['organisms'][0]['genes']['photosynthesis_capacity']
photosynthesis_function = random_function_maker(photosynthesis_function_dict)
speed_function_dict = Experiment_1['organisms'][1]['genes']['speed']
speed_function = random_function_maker(speed_function_dict)

print speed_function_dict
f = random_function_maker(speed_function_dict)
k0, k1, k5, Num = 0.0, 0.0, 0.0, 100000
for i in range(Num):
    k = f()
    if k == 0.0:
        k0 += 1
    if k == 1.0:
        k1 += 1
    if k == 5.0:
        k5 += 1
print k0/Num, k1/Num, k5/Num

def draw_things():
    gui = GUI.GUI_functions()

    f = lambda x: random.gauss(0, 5)
    gui.draw_function(f)
    timer = 0
    while timer < 100:
        gui.handle_events()
        timer += 0.01
        sleep(0.01)
    gui.delete()

draw_things()
print "Ya"

