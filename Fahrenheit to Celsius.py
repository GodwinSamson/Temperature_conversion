import tkinter as tk

def convert_fah_to_cel():
    fahrenheit = float(ent_fah.get())
    celsius = ((5/9) * fahrenheit) - 32
    lbl_result['text'] = round(celsius, 2), "\N{DEGREE CELSIUS}"


window = tk.Tk()

window.title("Fahrenheit to Celsius")
window.geometry("550x250")
frame = tk.Frame(master=window)

lbl_text = tk.Label(master=frame, text="Enter a fahrenheit temperature")

ent_fah = tk.Entry(master=frame, width=30)

lbl_fah = tk.Label(master=frame, text="\N{DEGREE FAHRENHEIT}", bg="green")

btn_convert = tk.Button(master=frame, command=convert_fah_to_cel, text="convert", bg="orange", width=20, )

lbl_result = tk.Label(master=frame, text="\N{DEGREE CELSIUS}", bg="green")

frame.grid(row=0, column=0)

lbl_fah.grid(row=2, column=2, padx=10)

ent_fah.grid(row=2, column=3, padx=5 )

btn_convert.grid(row=2, column=5, padx=5)

lbl_result.grid(row=2, column=4, padx=10)
lbl_text.grid(row=0, column=1, padx=10, pady=5 )

window.mainloop()