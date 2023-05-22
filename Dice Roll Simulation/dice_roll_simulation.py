import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.geometry("480x360")
window.title("Dice Roll")

# def roll_dice():
#     a = random.randint(1,6) #random integer
#     label = tk.Label(window, text=a).pack()

# button = tk.Button(window,text = "click", command=roll_dice)
# button.pack()

    

#Here we will add images of dice face
dice = ["Enter","The", "Path", "Of ", "dice face", "images"]
image_one = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image_two = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label_one = tk.Label(window,image=image_one)
label_two = tk.Label(window,image=image_two)

label_one.image = image_one
label_two.image = image_two

label_one.place(x=30, y=100)
label_two.place(x=300, y=100)

def dice_roll():
    image_one = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label_one.configure(image=image_one)
    label_one.image = image_one
    
    image_two = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label_two.configure(image=image_two)
    label_two.image = image_two
button = tk.Button(window,text="ROLL", bg="cyan", fg="black", font="Times 20 bold", command=dice_roll)
button.place(x=200, y=0)


window.mainloop()


