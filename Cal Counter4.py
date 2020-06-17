import turtle,random,time,math
import winsound # Import sound library
wn=turtle.Screen()
wn.setup(800,700)
wn.bgpic('eatbackground.gif')
images=['Cherry.gif','Apple.gif','Muffin.gif','Pizza.gif','Hotdog.gif',\
        'Ice.gif','Banana.gif','Plum.gif','Cucumber.gif','Frize.gif',\
        'Sprite.gif','Donut.gif','empty.gif']

images1=['Cherry_cal.gif','Apple_cal.gif','Muffin_cal.gif','Pizza_cal.gif',\
         'Hotdog_cal.gif','Ice_cal.gif','Banana_cal.gif','Plum_cal.gif',\
         'Cucumber_cal.gif','Frize_cal.gif','Sprite_cal.gif','Donut_cal.gif',
         'Donut_cal.gif']
turtle.tracer(3)
t=[]
tclone=[]
t1=[]


a=[]
M=12

for i in range (M+1):
        wn.addshape(images[i])
        wn.addshape(images1[i])
        t.append(turtle.Turtle())
        t[i].up()
        t[i].shape(images[i])
        tclone.append(t[i])
        t1.append(turtle.Turtle())
        t1[i].up()
        t1[i].shape(images1[i])
        t1[i].goto(50,-200)
        t1[i].hideturtle()
        a.append(0)
for n in range(M+1):
        tclone[n]=t[n].clone()
        tclone[n].up()
        tclone[n].goto(-300,-200)
        tclone[n].hideturtle()
        
for m in range(4):
    t[m].goto(-300+200*m,250)
    
    
for m in range(4):
    t[m+4].goto(-300+200*m,100)
    

for m in range(4):
    t[m+8].goto(-300+200*m,-50)

wn.addshape('Counter.gif')
Counter=turtle.Turtle()
Counter.up()
Counter.shape('Counter.gif')
Counter.goto(50,-200)

wn.addshape('pixx10.gif')
player=turtle.Turtle()
player.shape('pixx10.gif')
player.up()
player.hideturtle()
player.goto(-300,-200)
player.showturtle()

playersposition=player.position()

t0pos=t[0].position()
#print('tt0pos=',t0pos)        
delta=abs(playersposition-t0pos)
#print('delta=',delta)
#------------------------------------
turtle.tracer(1)

def h1(x,y):
    #wn.update()
    player.goto(x,y)
    playerposition=player.position()
    #print('!!!=',playerposition)
    if (abs(playerposition)-360)<40:
        #print('!!!=',playerposition)
        Counter.showturtle()        
    
    #print('t0pos=',t0pos)
    for q in range(12):
        a[q]=abs(playerposition-t[q].position())
        
    
        if a[q]<40:
            Counter.hideturtle()
            tclone[q].showturtle()
            t1[q].showturtle()
            #print('a[q]=',a[q])
            for m in range(q):
                tclone[m].hideturtle()
                tclone[m].clear()
                t1[m].hideturtle()
            for m in range((q+1),12):
                tclone[m].hideturtle()
                tclone[m].clear()
                t1[m].hideturtle()

wn.onclick(h1)



