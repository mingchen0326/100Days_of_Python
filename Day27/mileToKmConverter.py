import tkinter

window = tkinter.Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

empty_label = tkinter.Label(text="    ")
empty_label.grid(row=0, column=0)

inputMiles = tkinter.Entry(width=7)
inputMiles.grid(row=0, columns=1)


labelMiles = tkinter.Label(text="Miles")
labelEqual = tkinter.Label(text="is equal to")
labelKm = tkinter.Label(text="km")

labelMiles.grid(row=0, column=2)
labelEqual.grid(row=1, column=0)
labelKm.grid(row=1, column=2)


def display_km():
    miles = float(inputMiles.get())
    km = int(miles) * 1.60934
    label_result = tkinter.Label(text=0)
    label_result.grid(row=1, column=1)
    label_result.config(text=str(km))


button = tkinter.Button(text="Calculate", command=display_km)
button.grid(row=2, column=1)

window.mainloop()
