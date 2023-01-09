import tkinter
from PIL import Image, ImageTk
import random

root = tkinter.Tk()
root.geometry('400x400')
root.title('Roll The Dice')
root.configure(bg='#B9C6C9')
root.resizable(False,False)

l0 = tkinter.Label(root, text="")
l0.pack()

l1 = tkinter.Label(root, text="Hello I'm Jagriti!!!",
                    fg = "black", bg='#B9C6C9',
                    font = "Helvetica 16 bold italic")
l1.pack()

dice = ["dice_images/dice1.jpg","dice_images/dice2.jpg","dice_images/dice3.jpg","dice_images/dice4.jpg","dice_images/dice5.jpg","dice_images/dice6.jpg"]

image2 = ImageTk.PhotoImage(file='dice_images/dice.jpg')

label1 = tkinter.Label(root, image=image2)
label1.image = image2

label1.pack( expand=True)

def rolling_dice():
     image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

     label1.configure(image=image1,bg='#B9C6C9')

     label1.image = image1

button = tkinter.Button(root, text='Roll The Dice',font=('Arial,12,bold'),
                    width=20,height=2,bg='#FE3939',fg='white',command=rolling_dice)

button.pack( expand=True)

root.mainloop()