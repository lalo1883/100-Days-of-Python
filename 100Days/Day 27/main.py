import tkinter

window = tkinter.Tk()
window.title('Miles to Km converter')
window.minsize(width=200, height=100)
window.config(padx=10, pady=10)

def result_in_km():
    mph = input.get()
    mph = float(mph)
    km = mph * 1.6
    result['text'] = km

# Labels
is_equal = tkinter.Label(text='Is equal to: ')
is_equal.grid(column=0, row=1)

miles = tkinter.Label(text='Miles')
miles.grid(column=2, row=0)

kilometers = tkinter.Label(text='Km')
kilometers.grid(column=2, row=1)

result = tkinter.Label(text='0')
result.grid(column=1, row=1)

# Button
calculate = tkinter.Button(text='Calculate', command=result_in_km)
calculate.grid(column=1, row=2)

# Label
input = tkinter.Entry()
input.config(width=10)
input.grid(column=1, row=0)


window.mainloop()