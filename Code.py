molecules = []
canvas_size = {'x':1000,'y':600}

debug = False #True for debug mode 

#Space Partioning collsion needs to be added

def setup():  # setup() runs once
    size(canvas_size['x'], canvas_size['y'])
    frameRate(30)
    
    if debug == False:
        for i in range(115):
            molecule = {'x':random(0,canvas_size['x']),'y':random(0,canvas_size['y']),'vel':PVector(random(-5,5),random(-5,5)),'color':255,'radius':random(10,20), 'density':random(4,6), 'mass':0}
            molecule['mass'] = pow((molecule['radius'] * 4/3 * PI),3) * molecule['density']
            molecule['color']-=20*molecule['density']
            molecules.append(molecule)
    elif debug == True:
        molecule = {'x':0,'y':canvas_size['y']/2,'vel':PVector(5,0),'color':255,'radius':random(10,20), 'density':random(4,6), 'mass':0}
        molecule['mass'] = pow((molecule['radius'] * 4/3 * PI),3) * molecule['density']
        molecules.append(molecule)
        molecule = {'x':canvas_size['x'],'y':canvas_size['y']/2,'vel':PVector(-5,0),'color':255,'radius':random(10,20), 'density':random(4,6), 'mass':0}
        molecule['mass'] = pow((molecule['radius'] * 4/3 * PI),3) * molecule['density']
        molecules.append(molecule)
        

def draw():
    background(204)
    for molecule in molecules[:]: 
        fill(255,molecule['color'],molecule['color'])
        ellipse(molecule['x'],molecule['y'],molecule['radius'],molecule['radius'])
        molecule['x']+=molecule['vel'].x
        molecule['y']+=molecule['vel'].y
        wall_collide(molecule) #Calls wall colliode function
        collision_detection(molecule) #Calls molecule collsion detection

def collision_physics(object1, object2): #Elastic (No energy lossed) collision
    initial_vel1 = object1['vel']
    initial_vel2 = object2['vel']
object2['vel']= ((2*object1['mass'])/(object1['mass']+object2['mass']) * initial_vel1) - (((object1['mass']-object2['mass'])/(object1['mass']+object2['mass']))*initial_vel2)
    object1['vel']= (((object1['mass']-object2['mass'])/(object1['mass']+object2['mass']))*initial_vel1) +((2*object2['mass'])/(object1['mass']+object2['mass']) * initial_vel2)
    #pass
    #m_{1} v_{1 i}+m_{2} v_{2 i}=m_{1} v_{1 f}+m_{2} v_{2 f}
    

def collision_detection(object):
    for molecule in molecules[:]:
        if molecule != object:
            dx = (object['x'] + object['radius']) - (molecule['x'] + molecule['radius']);
            dy = (object['y'] + object['radius']) - (molecule['y'] + molecule['radius']);
            distance = sqrt(dx * dx + dy * dy);
            if (distance < object['radius'] + molecule['radius']):
                if object in molecules: #Prevents crashing due to error
                    #molecules.remove(molecule)
                    collision_physics(molecule,object)

def wall_collide(object):   
    #Wall collision
    if object['x'] < 0 or object['x'] > canvas_size['x']:
        object['vel'].x*=-1
    if object['y'] < 0 or object['y'] > canvas_size['y']:
        object['vel'].y*=-1
