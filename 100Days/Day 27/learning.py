import tkinter

window = tkinter.Tk()
window.title('My first GUI program')
window.minsize(width=500, height=300)
window.config(padx=40, pady=40)
def button_clicked():
    text = input.get()
    my_label['text'] = text

# Label
my_label = tkinter.Label(text='Im a label', font=('Arial', 20, 'bold'))
my_label.grid(column=0,row=0)

# Buttons
my_button = tkinter.Button(command=button_clicked)
second_button = tkinter.Button(width=15)
my_button['text'] = 'Click Me'
second_button.grid(column=2, row=0)
my_button.grid(column=1, row=1)


# Entry
input = tkinter.Entry(width=15)
input.grid(column=3, row=3)

window.mainloop()


# Pack
# Place
# Grid