# 1) Import required libraries:
#    a) Import Tkinter widgets (`from tkinter import *`) and `messagebox`.
#    b) Import PIL tools (`Image`, `ImageTk`) to load and show an image.

# 2) Create the main window:
#    a) Create `root` using `Tk()`.
#    b) Set title, background color, and window size using `.title()`, `.configure()`, `.geometry()`.

# 3) Add an image to the main window:
#    a) Open an image file using `Image.open()`.
#    b) Resize it using `.resize()`.
#    c) Convert it to Tkinter format using `ImageTk.PhotoImage()`.
#    d) Place the image on the window using a `Label` and `.place()`.

# 4) Add a welcome text label:
#    a) Create a label with a welcome message.
#    b) Position it near the bottom using `.place()`.

# 5) Create a function to show a message box:
#    a) Display an info box using `messagebox.showinfo()`.
#    b) If user clicks OK, open the top window by calling `topwin()`.

# 6) Add a button on the main window:
#    a) Create a button with text like "Let's get started!".
#    b) Connect it to the message box function using `command=...`.
#    c) Place the button using `.place()`.

# 7) Create a function to open the top window:
#    a) Create a new window using `Toplevel(root)`.
#    b) Set title, background, and size.
#    c) Place/position widgets inside the top window (labels, entries, buttons, output fields).
#    d) Run the top window loop.

# 8) Start the main application:
#    a) Use `root.mainloop()` to keep the main window running.

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

upload = Image.open("app_img.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(root,
    text="Hey User! Welcome to Denomination Counter Application.",
    bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo(
        "Alert", "Do you want to calculate the denomination count?")
    if MsgBox == 'ok':
        topwin()

button1 = Button(root,
                 text="Let's get started!",
                 command=msg,
                 bg='brown',
                 fg='black')
button1.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg='light grey')
    top.geometry('600x350+50+50')

    label = Label(top, text="Enter total amount", bg='light grey')
    entry = Entry(top)
    lbl = Label(top, text="Here are number of notes for each denomination", bg='light grey')

    l1 = Label(top, text="2000", bg='light grey')
    l2 = Label(top, text="500", bg='light grey')
    l3 = Label(top, text="100", bg='light grey')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    btn = Button(top, text='Calculate', command=calculator, bg='brown', fg='black')

    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    top.mainloop()

root.mainloop()