from tkinter import *
import requests
from datetime import datetime
from PIL import ImageTk, Image



# function that is used to track the price of the bitcoin 
def bitcoinTracker():
    response = requests.get(url="https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR").json()
    bitcoinPrice = response["USD"]
    priceINR = (int)(bitcoinPrice * 74.74)
    currentTime = datetime.now().strftime("%H:%M:%S")

    bitcoinPriceLabel.config(text=str(bitcoinPrice) + ' $\n\n' + str(priceINR) + ' INR (approx)')
    currentTimeLabel.config(text="Updated at: " + currentTime)


object_root = Tk()
object_root.geometry('1200x650')
object_root.title('Bitcoin Price Tracker') # this is the title of the application Bitcoin Price Tracker


myLabel = Label(object_root, text="Welcome To The Bitcoin Price Tracker", fg='purple', font="poppins 23 ")
myLabel.pack()

rot = Frame(object_root)
rot.pack(side="top", expand=True, fill="both")
my_canvas = Canvas(rot, width=400,height=206)

my_canvas.pack(fill="both", expand=True)
#bg = my_canvas.create_image(0,0,image=iconPhoto,anchor="nw")
#my_canvas.move(iconPhoto, 20, 20)
#my_canvas.grid(row=100, column=5)
#my_canvas.itemconfig(bg, image=iconPhoto)#this is the icon of the application Bitcoin Price Tracker


image1 = Image.open('C:\\Users\\Priyanshu\\Desktop\\img.png')
test = ImageTk.PhotoImage(image1)

label1 = Label(image=test)
label1.image = test

# Position image
label1.place(x=450, y=100)


bitcoinHeading = Label(object_root, text='Current Bitcoin Price', fg='orange', font="poppins 20 bold")
bitcoinHeading.pack(pady=25)
bitcoinPriceLabel = Label(object_root, font="poppins 18 bold")
bitcoinPriceLabel.pack(pady=25)

currentTimeLabel = Label(object_root, font="poppins 15")
currentTimeLabel.pack(pady=25)
bitcoinTracker()

Button(object_root, text='Refresh', font="poppins 10 bold", bg='black', fg='white', command=bitcoinTracker).pack()

object_root.mainloop()
