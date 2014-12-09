from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='violet')
drawpad.grid(row=0, column=0)
player = drawpad.create_oval(390,580,410,600, fill="cyan") 
enemy = drawpad.create_rectangle(50,50,100,60, fill="red")
enemy1 = drawpad.create_rectangle(50,70,100,80, fill="cyan")
enemy2 = drawpad.create_rectangle(50,90,100,100, fill="purple")

enemy3 = drawpad.create_rectangle(20,130,120,140, fill="blue")
enemy4 = drawpad.create_rectangle(20,150,120,160, fill="green")
enemy5 = drawpad.create_rectangle(20,170,120,180, fill="black")

enemy6 = drawpad.create_rectangle(270,210,370,220, fill="pink")
enemy7 = drawpad.create_rectangle(270,230,370,240, fill="grey")
enemy8 = drawpad.create_rectangle(270,250,370,260, fill="orange")

enemyList = [enemy,enemy1,enemy2,enemy3,enemy4,enemy5,enemy6,enemy7,enemy8]

direction = 9
direction1 = 33
direction2 = 6
direction3 = 3
direction4 = 12
direction5 = 15
direction6 = 18
direction7 = 21
direction8 = 24


class myApp(object):
    def __init__(self, parent):
        
        global drawpad
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()



    #start off our project
        drawpad.pack()
        root.bind_all('<Key>', self.key)
        self.animate()


    def animate(self):
        global drawpad
        global enemy
        global direction, direction1, direction2, direction3, direction4, direction5, direction6, direction7, direction8
        global player
        x1,y1,x2,y2 = drawpad.coords(enemy)
        e1x1,e1y1,e1x2,e1y2 = drawpad.coords(enemy1)
        e2x1,e2y1,e2x2,e2y2 = drawpad.coords(enemy2)
        e3x1,e3y1,e3x2,e3y2 = drawpad.coords(enemy3)
        e4x1,e4y1,e4x2,e4y2 = drawpad.coords(enemy4)
        e5x1,e5y1,e5x2,e5y2 = drawpad.coords(enemy5)
        e6x1,e6y1,e6x2,e6y2 = drawpad.coords(enemy6)
        e7x1,e7y1,e7x2,e7y2 = drawpad.coords(enemy7)
        e8x1,e8y1,e8x2,e8y2 = drawpad.coords(enemy8)
        px1,py1,px2,py2 = drawpad.coords(player)

        

        
            
        drawpad.move(enemy, direction, 0)
        if x2 > 800:
            direction = - 6
        elif x1 < 0:
            direction = 6        
        drawpad.move(enemy1, direction1, 0)
        if e1x2 > 800:
            direction1 = - 6
        elif e1x1 < 0:
            direction1 = 6
        drawpad.move(enemy2, direction2, 0)
        if e2x2 > 800:
            direction2 = - 8
        elif e2x1 < 0:
            direction2 = 8
        drawpad.move(enemy3, direction3, 0)
        if e3x2 > 800:
            direction3 = - 9
        elif e3x1 < 0:
            direction3 = 9
        drawpad.move(enemy4, direction4, 0)
        if e4x2 > 800:
            direction4 = - 10
        elif e4x1 < 0:
            direction4 = 10
        drawpad.move(enemy5, direction5, 0)
        if e5x2 > 800:
            direction5 = - 11
        elif e5x1 < 0:
            direction5 = 11
        drawpad.move(enemy6, direction6, 0)
        if e6x2 > 800:
            direction6 = - 8
        elif e6x1 < 0:
            direction6 = 8
        drawpad.move(enemy7, direction7, 0)
        if e7x2 > 800:
            direction7 = - 7
        elif e7x1 < 0:
            direction7 = 7
        drawpad.move(enemy8, direction8, 0)
        if e8x2 > 800:
            direction8 = - 12
        elif e8x1 < 0:
            direction8 = 12
        
        
        x1,y1,x2,y2 = drawpad.coords(player)
        
        for e in enemyList:
               ex1,ey1,ex2,ey2 = drawpad.coords(e)
               if ex1 < x1 and ex2 > x1 and ey1 < y1 and ey2 > y1:
                    drawpad.move(player,390 - x1, 580 - y1)
            
        
        drawpad.after(10,self.animate)
        
        
        

    def key(self,event):
        global player
        x1,y1,x2,y2 = drawpad.coords(player)
        if event.char == "w":
            if y1 < 800:
                drawpad.move(player,0,-8)
                
        if event.char == "s":
            if y2 < 600:
                drawpad.move(player,0,8)
                
        if event.char == "a":
            if x1 > 0:
                drawpad.move(player,-8,0)
                
        
        if event.char == "d":
            if x2 < 800:
                drawpad.move(player,8,0)
                


app = myApp(root)
root.mainloop()