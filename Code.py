molecules = [] #List that holds all the dictionaries of molecules of data
canvas_size = {'x':1000,'y':600}



scaling_factor = 1
density_scaling_factor = 4.0

#Molecule Radius, Density, and Mass based on real word nubmers

#Assigns dictionary 'methane' values
methane = {
    'x':0,
    'y':0,
    'vel':PVector(random(-5,5),random(-5,5)),
    'color':color(52, 237, 86),
    'radius':24.4*scaling_factor, 
    'density':0.657*density_scaling_factor, 
    'mass':16, 
    'reacts_with':'oxygen'
} 

#Assigns dictionary 'oxygen' values
oxygen = {
    'x':0,
    'y':0,
    'vel':PVector(random(-5,5),random(-5,5)),
    'color':color(234, 237, 52),
    'radius':22.39*scaling_factor, 
    'density':1.429*density_scaling_factor, 
    'mass':32, 
    'reacts_with':'methane'
} 

#Assigns dictionary 'carbon_dioxide' values
carbon_dioxide = {
    'x':0,
    'y':0,
    'vel':PVector(random(-5,5),random(-5,5)),
    'color':color(237, 173, 45),
    'radius':22.26*scaling_factor, 
    'density':1.977*density_scaling_factor,
    'mass':44,
    'reacts_with':'nothing'
} 

#Assigns dictionary 'water' values
water = {
    'x':0,
    'y':0,
    'vel':PVector(random(-5,5),random(-5,5)),
    'color':color(53, 64, 219),
    'radius':22.39*scaling_factor, 
    'density':0.804*density_scaling_factor, 
    'mass':18, 
    'reacts_with':'nothing'
} 
  

debug = False #True for debug mode 

#Space Partioning collsion needs to be added

def setup():  # setup() runs once

    size(canvas_size['x'], canvas_size['y']) #Sets canvas size based on predetermined value
    frameRate(30) #Sets framrate
    
    if debug == False: #Runs code as normal if debug is False
        for i in range(50):
            #molecule = {'x':random(0,canvas_size['x']),'y':random(0,canvas_size['y']),'vel':PVector(random(-5,5),random(-5,5)),'color':255,'radius':random(10,20), 'density':random(4,6), 'mass':0} #Assigns dictionary 'molecule' values
            #molecule = {'x':0,'y':0,'vel':PVector(random(-5,5),random(-5,5)),'color':255,'radius':173*scaling_factor, 'density':random(4,6), 'mass':0} #Assigns dictionary 'molecule' values
            create_molecule(oxygen,None)
            create_molecule(methane,None)
    elif debug == True: #Debug mode for code, creates head on collision between two circles
        molecule = dict(methane)
        molecule['vel']=PVector(5,0)
        molecule['mass'] = pow((molecule['radius'] * 4/3 * PI),3) * molecule['density']
        molecule['y']=canvas_size['y']/2
        molecules.append(molecule)
        molecule = dict(oxygen)
        molecule['y']=canvas_size['y']/2
        molecule['x']=canvas_size['x']
        molecule['vel']=PVector(-5,0)
        molecule['mass'] = pow((molecule['radius'] * 4/3 * PI),3) * molecule['density']
        molecules.append(molecule)
        

def draw(): #Function Draws Molecules to Canvas
    background(204)
    for molecule in molecules[:]: 
        #fill(255,molecule['color'],molecule['color']) #Colors Molecules based on assigned 'color' value
        fill(molecule['color'])
        ellipse(molecule['x'],molecule['y'],molecule['radius'],molecule['radius']) #Draws Ellipses 
        molecule['x']+=molecule['vel'].x #Moves Molecule's x cordinate based on vel.x
        molecule['y']+=molecule['vel'].y #Moves Molecule's y cordinate based on vel.y
        wall_collide(molecule) #Calls wall colliode function
        collision_detection(molecule) #Calls molecule collsion detection

def create_molecule(type, pos):
    #Creates a copy of the dictionary referenced by type
    molecule=dict(type)
    #Sets molecule x and y cord
    if pos is None:
        molecule['x']=random(0,canvas_size['x'])
        molecule['y']=random(0,canvas_size['y'])
    elif pos is not None:
        molecule['x']=pos.x
        molecule['y']=pos.y
    #Sets molecule Velocity
    molecule['vel']=PVector(random(-5,5),random(-5,5))
    #Recalculates mass to fit size
    molecule['mass'] = pow((molecule['radius'] * 4/3 * PI),3) * molecule['density'] #Calculates 'mass' based on 'density' and 'size'
    #molecule['color']-=20*molecule['density']
    molecules.append(molecule) #Adds the dictionary of the 'molecule' to the list of 'molecules'

def collision_physics(object1, object2): #Elastic (No energy lossed) collision
    initial_vel1 = object1['vel'] #Records initial velocity of object 1 for physics calculations
    initial_vel2 = object2['vel']#Records initial velocity of object 2 for physics calculations
    object2['vel']= ((2*object1['mass'])/(object1['mass']+object2['mass']) * initial_vel1) - (((object1['mass']-object2['mass'])/(object1['mass']+object2['mass']))*initial_vel2) #Calcs object2 velocity based on collision and mass
    object1['vel']= (((object1['mass']-object2['mass'])/(object1['mass']+object2['mass']))*initial_vel1) +((2*object2['mass'])/(object1['mass']+object2['mass']) * initial_vel2)#Calcs object1 velocity based on collision and mass
    #Prevent overlapping of atoms
    object1['x']+=(object1['x']-object2['x'])/10 #Divide by 10 to prevent jumpy collisions
    object1['y']+=(object1['y']-object2['y'])/10 #Divide by 10 to prevent jumpy collisions
    
    
def collision_detection(object):
    for molecule in molecules[:]:
        if molecule != object:
            dx = (object['x'] + object['radius']) - (molecule['x'] + molecule['radius']);
            dy = (object['y'] + object['radius']) - (molecule['y'] + molecule['radius']);
            distance = sqrt(dx * dx + dy * dy);
            if (distance < object['radius'] + molecule['radius']):
                if object in molecules: #Prevents crashing due to error
                    if 'nothing' in {object['reacts_with'], molecule['reacts_with']}:
                        #Collision physics and velocity calculations
                        collision_physics(molecule,object)
                    else:
                        if 'methane' in {object['reacts_with'], molecule['reacts_with']}:
                            if 'oxygen' in {object['reacts_with'], molecule['reacts_with']}:
                                molecules.remove(object)
                                molecules.remove(molecule)
                                create_molecule(water, PVector(object['x'],object['y'])) #Creates molecule from reaction in same pos
                                create_molecule(carbon_dioxide, PVector(object['x'],object['y'])) #Creates molecule from reaction in same pos
                            else:
                                #Collision physics and velocity calculations
                                collision_physics(molecule,object)
                        else:
                            #Collision physics and velocity calculations
                            collision_physics(molecule,object)

def wall_collide(object):   
    #Wall collision
    if object['x'] < 0 or object['x'] > canvas_size['x']:
        object['vel'].x*=-1
    if object['y'] < 0 or object['y'] > canvas_size['y']:
        object['vel'].y*=-1
