import os,time,random
from pynput import keyboard
import sys

pixels=[" ","=","$","#","*","@","O"]
size=[96,24]

class entity(object):
    def __init__(self,position,shape,name):
        self.position=position
        self.shape=shape
        self.name=name
    def set_position(self,position):
        self.position=position

class screen(object):
    def __init__(self,size):
        self.size=size
        self.screen=[[0 for x in range(size[0])] for y in range(size[1])]
        self.dscreen=self.screen.copy()
    def update(self):
        global objects
        self.screen=[[0 for x in range(size[0])] for y in range(size[1])]
        flag=False
        for i in objects:
            for y in range(len(i.shape)):
                for x in range(len(i.shape[y])):
                    try:
                        if (i.position[1]+y>=0 and i.position[0]+x>=0) and (i.position[1]+y<=self.size[1] and i.position[0]+x<=self.size[0]):
                            if (i.shape[y][x]==5 and self.screen[i.position[1]+y][i.position[0]+x]==4) or (i.shape[y][x]==4 and self.screen[i.position[1]+y][i.position[0]+x]==5 ):
                                flag=True
                                er=entity([int(size[0]/2),int(size[1]/2)],retry,"retry")
                                for y2 in range(len(er.shape)):
                                    for x2 in range(len(er.shape[y2])):
                                        self.screen[er.position[1]+y2][er.position[0]+x2]=er.shape[y2][x2]
                                self.show()
                                for i,k in enumerate(objects):
                                    if k.name=="dino":
                                        objects=[k]
                                    break
                                os.system("pause")
                                os.sytem("cls")
                            if flag:
                                break
                            self.screen[i.position[1]+y][i.position[0]+x]=i.shape[y][x]
                    except:
                        pass
                if flag:
                    break
            if flag:
                break
    def show(self):
        string=""
        #os.system("cls")
        for y in range(len(self.screen)):
            for x in range(len(self.screen[y])):
                if y==0 or x==0 or y==len(self.screen)-1 or x==len(self.screen[y])-1:
                    #print("+",end="")
                    string+="+"
                else:
                    #print(pixels[self.screen[y][x]],end="")
                    string+=pixels[self.screen[y][x]]
            string+="\n"
        sys.stdout.write(string)

global objects
objects=[]

cloud=[[0,0,3,3,3,0]
       ,[0,3,3,3,3,0]
       ,[3,3,3,3,3,3]
       ,[0,0,3,3,3,0]
       ,[0,0,0,3,3,0]
       ]

cactus=[[4,0,4,4,0,0]
        ,[4,4,4,4,0,4]
        ,[0,0,4,4,4,4]
        ,[0,0,4,4,0,0]
        ,[0,0,4,4,0,0]
        ]

dino_1=[[0,0,0,5,5,5,5,5]
        ,[0,0,0,5,6,5,5,5]
        ,[0,0,5,5,5,5,0,0]
        ,[5,5,5,5,5,0,0,0]
        ,[0,0,0,5,5,0,0,0]
        ]

dino_2=[[0,0,0,5,5,5,5,5]
        ,[0,0,0,5,6,5,5,5]
        ,[0,0,5,5,5,5,0,0]
        ,[5,5,5,5,5,0,0,0]
        ,[0,0,5,0,5,0,0,0]
        ,[0,0,0,0,0,0,0,0]
        ]

retry=[[3,3,3,3,0,0,3,3,3,0,3,3,3,3,3,0,3,3,3,3,0,0,3,3,3,3,3,0,3,0,0,0,3]
       ,[3,0,0,3,0,0,3,0,0,0,0,0,3,0,0,0,3,0,0,3,0,0,0,0,3,0,0,0,0,3,0,3,0]
       ,[3,3,3,0,0,0,3,3,3,0,0,0,3,0,0,0,3,3,3,0,0,0,0,0,3,0,0,0,0,0,3,0,0]
       ,[3,0,0,3,0,0,3,0,0,0,0,0,3,0,0,0,3,0,0,3,0,0,0,0,3,0,0,0,0,3,0,0,0]
       ,[3,0,0,0,3,0,3,3,3,0,0,0,3,0,0,0,3,0,0,0,3,0,3,3,3,3,3,0,3,0,0,0,0]]


display=screen(size)
cactus_counter=0
objects.append(entity([20,size[1]-6],dino_1,"dino"))
dino_step=0
up=False
up_height=0
down=True

def restart():
    global objects
    for i,k in enumerate(objects):
        if k.name=="dino":
            objects=[k]
            break

def on_press(key):
    global up
    global up_height
    global down
    try:
        if key.char=="w" and not up and down and not up_height:
            up=True
            down=False
    except:
        pass
listener = keyboard.Listener(on_press=on_press)
listener.start()
while 1:
    if up_height>0 and down:
        up_height-=1
    if not down:
        up_height+=1
    if up_height>10:
        down=True
        up=False

    if random.randint(0,10)==10:
        objects.append(entity([size[0],random.randint(-3,3)],cloud,"cloud"))
    if random.randint(0,15)==10 and cactus_counter>=25:
        objects.append(entity([size[0],size[1]-6],cactus,"cactus"))
        cactus_counter=0
    else:
        cactus_counter+=1
    for k,i in enumerate(objects):
        if i.name=="cloud":
            i.position=[i.position[0]-1,i.position[1]]
            if i.position[0]<0:
                del objects[k]
        elif i.name=="cactus":
            i.position=[i.position[0]-1,i.position[1]]
        elif i.name=="dino":
            dino_step=not dino_step
            i.shape=[dino_1,dino_2][dino_step]
            i.position=[20,size[1]-6-up_height]
    display.update()
    #print(display.screen)
    display.show()
    time.sleep(.05)
