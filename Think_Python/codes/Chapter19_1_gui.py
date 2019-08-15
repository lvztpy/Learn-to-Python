from swampy.Gui import *
#from Gui import * #这句话不要，第一句话就可以了

g = Gui()
g.title('Gui')

button = g.bu(text = 'lOVE Mi')
label = g.la(text='it is the label do sth')

def make_label():
    g.la(text='Thank you')

button2 = g.bu(text='no,press me',command=make_label)#create a button

canvas = g.ca(width=500, height=500)
canvas.config(bg='red')
item = canvas.circle([0,0],100,fill='black')
item.config(fill='yellow',outline='orange',width=10)
canvas.rectangle([[0,0],[200,100]],
fill='red',outline='orange',width=10)#draw a rectangle
canvas.oval([[0,0],[200,100]],outline='pink',width='20')#draw an oval
canvas.line([[0,100],[100,200]],width=20)#draw a lines

g.mainloop()
