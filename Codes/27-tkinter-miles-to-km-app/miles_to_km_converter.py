import tkinter as tk

def miles_to_km():
    miles = user_input.get()
    km = round(float(miles) * 1.609)
    result_label.config(text= f"{km}")

window = tk.Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

user_input = tk.Entry(width=10)
user_input.grid(column=1, row=0)

miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = tk.Label(text="is iqual to")
is_equal_to_label.grid(column=0, row=1)

result_label = tk.Label(text="0")
result_label.grid(column=1, row=1)

km_label = tk.Label(text="Km")
km_label.grid(column=2, row=1)


calculate_button = tk.Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)






window.mainloop()