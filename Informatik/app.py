# Import module
from tkinter import *
from tkinter import messagebox

number = 9;
number1 = 1;
number2 = 23459;

def show_canvas_2():
    canvas2.pack(fill = "both", expand = True)

def hide_canvas_1():
    canvas1.pack_forget()

def show_canvas_1():
    canvas1.pack(fill = "both", expand = True)

def hide_canvas_2():
    canvas2.pack_forget()

def clear1():
    txt.delete('0',END)

def sel():
    number1 = v.get()

# back to page 1
def back_to_1():
     hide_canvas_2()
     show_canvas_1()
    
def check1():
    if (int(txt.get()) > 8850) and (int(txt.get()) > 0):
        messagebox.showinfo("Fehlermeldung", "Bitte eine Meereshöhe zwischen 0 - 8.850m eingeben")
    else:
        hide_canvas_1()
        show_canvas_2()
        number2 = txt.get()

        variabel1 = Label(root, text = txt.get(),bg = '#fbfbb2')
        variabel1_canvas = canvas2.create_window( 17, 47,anchor = "nw",window = variabel1 )
        
        letter=StringVar()

        number1= v.get()
        if number1 == '1':
          letter='S'
        if number1 == '2':
          letter='M'
        if number1 == '3':
          letter='L'
        
        label2=Label(root, text = letter,bg = '#fbfbb2')
        label2_canvas = canvas2.create_window( 730, 47,anchor = "nw",window = label2 )




    
def action(number):
    txt.insert(10, number)
    

# actionPerform canvas 2

def button_1():
    messagebox.showinfo("Information", "Ei bitte in die Messstation legen!")    
def button_2():
    messagebox.showinfo("Information", "Ei bitte in die Messstation legen!")
def button_3():
    messagebox.showinfo("Information", "Ei bitte in die Messstation legen!")
def button_4():
    messagebox.showinfo("Information", "Ei bitte in die Messstation legen!")
   



root = Tk()

#fullscreen / für Fenstermodus auskommentieren
root.wm_attributes('-fullscreen', 'True') 

# Bildschirm 800x480
root.geometry("800x480")

# Add image file
# Bild am Raspberry
# bg = PhotoImage(file=r"/home/pi/Desktop/Bilder/logo800x480.png")

# Bild am PC 
bg = PhotoImage(file = "logo800x480.png")

# Create Canvas  1
canvas1 = Canvas( root, width = 480, height = 240)
canvas1.pack(fill = "both", expand = True)
# Create Canvas  2
canvas2 = Canvas( root, width = 480, height = 240)

# Bild anzeigen
canvas1.create_image( 0, 0, image = bg,	anchor = "nw")



# Buttons erzeugen canvas1
button0 = Button( root, text = "0", height=2, width = 13, command = lambda:action(0))
button1 = Button( root, text = "1", height=2, width = 13, command = lambda:action(1))
button2 = Button( root, text = "2", height=2, width = 13, command = lambda:action(2))
button3 = Button( root, text = "3", height=2, width = 13, command = lambda:action(3))
button4 = Button( root, text = "4", height=2, width = 13, command = lambda:action(4))
button5 = Button( root, text = "5", height=2, width = 13, command = lambda:action(5))
button6 = Button( root, text = "6", height=2, width = 13, command = lambda:action(6))
button7 = Button( root, text = "7", height=2, width = 13, command = lambda:action(7))
button8 = Button( root, text = "8", height=2, width = 13, command = lambda:action(8))
button9 = Button( root, text = "9", height=2, width = 13, command = lambda:action(9))
button_clear = Button( root, text = "Löschen", height = 2, width = 13, command = clear1)
button_next = Button( root, text = "Weiter", height = 2, width = 13, command = check1)

#textbox
txt = Entry(root, width = 19)


#label
meereshoehe = Label(root, text = "Meereshöhe eingeben: ", bg = '#fbfbb2', font = ("Courier", 20))
text_canvas = canvas1.create_window(490, 330, anchor = "nw", window = txt)
eigröße = Label(root, text="Eigröße auswählen: ", bg = '#fbfbb2', font = ("Courier", 20))



# Bilder platzieren canvas1
# Bilder erzeugen canvas2
canvas2.create_image( 0, 0, image = bg,	anchor = "nw")


meereshoehe_canvas = canvas1.create_window( 150, 320, anchor = "nw", window = meereshoehe )
eigröße_canvas2 = canvas1.create_window( 150, 280, anchor = "nw", window = eigröße )

button0_canvas = canvas1.create_window( 0, 380, anchor = "nw", window = button1 )
button1_canvas = canvas1.create_window( 133, 380, anchor = "nw", window = button2 )
button2_canvas = canvas1.create_window( 266, 380, anchor = "nw", window = button3 )
button3_canvas = canvas1.create_window( 399, 380, anchor = "nw", window = button4)
button4_canvas = canvas1.create_window( 532, 380, anchor = "nw", window = button5)
button_clear_canvas = canvas1.create_window( 665, 380, anchor = "nw", window = button_clear)

button5_canvas = canvas1.create_window( 0, 430, anchor = "nw", window = button6)
button6_canvas = canvas1.create_window( 133, 430, anchor = "nw", window = button7)
button7_canvas = canvas1.create_window( 266, 430, anchor = "nw", window = button8)
button8_canvas = canvas1.create_window( 399, 430, anchor = "nw", window = button9)
button9_canvas = canvas1.create_window( 532, 430, anchor = "nw", window = button0)
button_clear_canvas = canvas1.create_window( 665, 430, anchor = "nw", window = button_next)



v = StringVar(root, "1")

var = IntVar()
R1 = Radiobutton(root, text = "S", variable = v, value = 1,command = sel, bg = '#fbfbb2', font = ("Courier", 15))
Radiobutton_canvas = canvas1.create_window( 490, 280, anchor = "nw", window = R1)
R2 = Radiobutton(root, text = "M", variable = v, value = 2, command = sel, bg = '#fbfbb2', font = ("Courier", 15))
Radiobutton_canvas = canvas1.create_window( 540, 280, anchor = "nw", window = R2)
R3 = Radiobutton(root, text = "L", variable = v, value = 3, command = sel, bg = '#fbfbb2', font = ("Courier", 15))
Radiobutton_canvas = canvas1.create_window( 590, 280, anchor = "nw", window = R3)




# canvas 2 ----------------------------------------------------------------------------------

label1 = Label(root, text = "Meereshöhe:", bg = '#fbfbb2', font = ("Courier", 12))
label1 = canvas2.create_window( 17, 17, anchor = "nw", window = label1 )

label1 = Label(root, text = "Gewünschte Kochstufe auswählen :" , bg = '#fbfbb2', font = ("Courier", 20))
label1 = canvas2.create_window( 45, 255, anchor = "nw", window = label1 )

label2 = Label(root, text = "Eigröße:", bg = '#fbfbb2', font = ("Courier", 12))
label2_canvas = canvas2.create_window( 700, 17, anchor = "nw", window = label2 )
 

# Bilder für Raspberry
#photo_logo = PhotoImage(file = r"/home/pi/Desktop/Bilder/logo800x480.png")

#photo1 = PhotoImage(file = r"/home/pi/Desktop/Bilder/stufe_1.png") 
#photo2 = PhotoImage(file = r"/home/pi/Desktop/Bilder/stufe_2.png") 
#photo3 = PhotoImage(file = r"/home/pi/Desktop/Bilder/stufe_3.png") 
#photo4 = PhotoImage(file = r"/home/pi/Desktop/Bilder/stufe_4.png")

# Bilder für PC
photo_logo = PhotoImage(file = "logo800x480.png")

photo1 = PhotoImage(file = "stufe_1.png") 
photo2 = PhotoImage(file = "stufe_1.png") 
photo3 = PhotoImage(file = "stufe_1.png") 
photo4 = PhotoImage(file = "stufe_1.png")

button2_logo = Button( root, text = "1", width = 180, height = 60, bg = 'white', image = photo_logo)

button2_1 = Button( root, text = "1", width = 150, height = 130, bg = 'white', image = photo1, command=button_1)
button2_2 = Button( root, text = "2", width = 150, height = 130, bg = 'white', image = photo2, command=button_2)
button2_3 = Button( root, text = "3", width = 150, height = 130, bg = 'white', image = photo3, command=button_3)
button2_4 = Button( root, text = "4", width = 150, height = 130, bg = 'white', image = photo4, command=button_4)

button1_canvas2 = canvas2.create_window( 40, 300, anchor = "nw", window = button2_1)
button2_canvas2 = canvas2.create_window( 230, 300, anchor = "nw", window = button2_2)
button3_canvas2 = canvas2.create_window( 420, 300, anchor = "nw", window = button2_3)
button4_canvas2 = canvas2.create_window( 610, 300, anchor = "nw", window = button2_4)



button_back = Button( root, text = "Zurück", width = 11, height = 1, bg = 'white', command=back_to_1)
button_canvas_button_new = canvas2.create_window( 650, 440, anchor = "nw", window = button_back)

root.mainloop()