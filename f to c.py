import tkinter as tk
from tkinter import ttk

window = tk.Tk()
farenhait_val = tk.StringVar()

lbl_result = tk.Label(
    window,
    text = "Enter your number...",  
)
def convert_F_to_C(*args):
    
    farenhait_input = farenhait_val.get()
    try:
        farenhait_value = float(farenhait_input) 
        lbl_result["text"] = (farenhait_value- 32)*5/9
    except ValueError:
        if farenhait_input != '':
            
            lbl_result["text"] = "You should enter a number..."
        else:
            lbl_result["text"] = "Your input is empty...."

window.bind('<Return>', convert_F_to_C) 
                      
farenhait_name = tk.Label(
    window,
    text = "Farenhait")
farenhait_entry = ttk.Entry(
    window,
    width=50,
    textvariable= farenhait_val,
    )

calc_button = ttk.Button(
    window,
    text = "calc",
    width=10,
    command= convert_F_to_C)

farenhait_name.grid(row = 0, column = 0, padx=10, pady=10)
farenhait_entry.grid(row = 0, column = 1)
calc_button.grid(row = 0, column = 2, padx= 30)

lbl_celsuis = tk.Label(
    window,
    text = "celsuis")

lbl_celsuis.grid(row = 1, column =0 , pady =(10,20))
lbl_result.grid(row = 1, column = 1, pady = (10,20))



window.title("Farenhait to Celsuis")
window.mainloop()