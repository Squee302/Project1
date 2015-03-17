
#yo

#so far you should see just a window that displays text.
#we need to get santi's api in here and get it producing usable values.
#once we have those we can build the state machine... Hopefully. 
#dont worry about how pretty it looks yet. But if you wanna fuck with it, go ahead. 










#print "This is the master file for our project"
#http://www.java2s.com/Code/Python/GUI-Tk/BaseWindows.htm
from Tkinter import *

 
 #create the root window
root = Tk()

root.title("Halodrobe")
canvas = Canvas(width=500, height=500, bg='white')   
canvas.pack(expand=YES, fill=BOTH)                   

canvas.create_text(250, 50, text='WELCOME TO HALDROBE')  
canvas.create_text(100, 70*1.5, text='Location:')
canvas.create_text(90, 110*1.5, text='Temperature:')
canvas.create_text(81, 150*1.5, text='Chance of Precip:')
#This is where any text or outputs should be printed


# Start the window's event-loop
root.mainloop()




          


