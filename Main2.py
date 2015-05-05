import Tools
import actions
import initial_settings
from GUI import GUI
from time import sleep  # To remove
from copy import deepcopy
import Biotope
import Organism

# Creation of biotope
BIOTOPE_SIZE_X, BIOTOPE_SIZE_Y, REPRODUCTION_FREQUENCY, GLOBAL_LONGEVITY = initial_settings.BIOTOPE_SIZE_X, initial_settings.BIOTOPE_SIZE_Y, initial_settings.REPRODUCTION_FREQUENCY, initial_settings.GLOBAL_LONGEVITY



class Ecosystem(object):
    organisms = []
    newborns = []
    biotope = None

    def __init__(self, biotope_size_x, biotope_size_y):
        self.biotope = Biotope.Biotope(biotope_size_x, biotope_size_y)
        self.biotope.set_Ecosystem(self)
        
    def create_organisms(self, org_list):
        for (N, Data) in org_list:
            for i in range(0, N):
                new_loc = self.biotope.seek_free_pos()
                if new_loc != None:
                    new_org = Organism.Organism(deepcopy(Data))
                    new_org.setLocation(new_loc)
                    self.organisms.append(new_org)

    def evolve(self):
        # Biotope actions
        actions.BiotopeActions.change_temperature(self)  # Temporal

        # Organisms actions
        i = 0
        while i < len(self.organisms):
            organism = self.organisms[i]
            # Actions
            organism.move(self)
            organism.do_photosynthesis(self)
            # Procreation and death of organism:
            organism.procreate(self)
            org_status = organism.age(self)
            if org_status == 'Dead':
                self.organisms.remove(organism)
            
            # Get i pointing to right organism:
            i = i + 1
        self.organisms += self.newborns
        self.newborns = []
        # print 'Num of organisms + newborns: %d' % len(self.organisms)


def main():
    # create Ecosystem
    ecosystem = Ecosystem(BIOTOPE_SIZE_X, BIOTOPE_SIZE_Y)
    # Add initial organisms to the ecosystem:
    ecosystem.create_organisms(initial_settings.initial_organisms)
    
    gui = GUI(ecosystem)
    # Loop
    time = 0
    while (len(ecosystem.organisms) > 0) and (time < 300):  # TODO: Define correct condition
        ecosystem.evolve()
        gui.handle_events()
        gui.draw_ecosystem()
        sleep(0.1)  # To remove
        time += 1
        if time%10 == 0:
            print "time =", time, "Num of organisms =", len(ecosystem.organisms)
            #print "reproduction frequency =", REPRODUCTION_FREQUENCY, "global gongevity =", GLOBAL_LONGEVITY
    gui.delete()
    print "finished"
if __name__ == '__main__':
    main()
