molecules = []
canvas_size = {'x':1000,'y':600}

#Space Partioning collsion needs to be added

def setup():  # setup() runs once
    size(canvas_size['x'], canvas_size['y'])
    frameRate(30)
    
    for i in range(100):
        molecule = {'x':random(0,canvas_size['x']),'y':random(0,canvas_size['y']),'vel':PVector(random(-5,5),random-5,5)),'velx':1+random(-5,5),'vely':1+random(-5,5), 'color':255,'radius':random(10,20), 'density':random(1,10), 'mass':0}
        molecule['mass'] = pow((molecule['radius'] * 4/3 * PI),3) * molecule['density']
        molecules.append(molecule)

def draw():
    background(204)
    for molecule in molecules[:]: 
        fill(255,molecule['color'],molecule['color'])
        ellipse(molecule['x'],molecule['y'],molecule['radius'],molecule['radius'])
        molecule['x']+=molecule['velx']
        molecule['y']+=molecule['vely']
        wall_collide(molecule) #Calls wall colliode function
        collision_detection(molecule) #Calls molecule collsion detection

def collision_physics(object1, object2): #Elastic (No energy lossed) collision
    
    pass
    #m_{1} v_{1 i}+m_{2} v_{2 i}=m_{1} v_{1 f}+m_{2} v_{2 f}
    

def collision_detection(object):
    for molecule in molecules[:]:
        if molecule != object:
            x1=object['x'] #X cord of object1
            y1=object['y'] #Y cord of object1
            r1=object['radius'] #radius of object1
            x2=molecule['x'] #x cord of object2
            y2=molecule['y']#y cord of object2
            r2=molecule['radius'] #radius of object2
            if pow((x2-x1),2) + pow((y2-y1),2) <= pow((r1+r2),2):
                if object in molecules: #Prevents crashing due to error
                    #molecules.remove(molecule)
                    collision_physics(molecule,object)
                    object['color']-=50

def wall_collide(object):   
    #Wall collision
    if object['x'] < 0 or object['x'] > canvas_size['x']:
        object['velx']*=-1
    if object['y'] < 0 or object['y'] > canvas_size['y']:
        object['vely']*=-1
