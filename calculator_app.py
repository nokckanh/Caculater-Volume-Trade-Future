import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from decimal import Decimal

# CREATE TICKER SYMBOL DICTIONARY WITH TICK_SIZE AND TICK_VALUE
futures = { }

# MAIN WINDOW
root = tk.Tk()
root.title("Caculater Volume")
root.geometry('220x360-40+500')
# root.resizable(0, 0) 

# for entry boxes
num_contracts_var = tk.DoubleVar()     
entry_price_var = tk.DoubleVar()
exit_price_var = tk.DoubleVar()
Gia_thanh_ly = tk.DoubleVar()

# CREATE FRAMES FOR AREAS OF THE ROOT WINDOW
# Radio button frame
frame = tk.LabelFrame(root)
frame.grid(row=0, column=0, padx=20, pady=25, sticky=tk.W)

# Parameters Frame
parm_frame = tk.LabelFrame(root, text = "Nhập dữ liệu", )
parm_frame.grid(row=1, column=0, columnspan=3, padx=20, ipadx=10)

# Frame for long or short radiobuttons
output_frame = tk.LabelFrame(root, text = "Kết quả")
output_frame.grid(row=2, column=0, columnspan=3, padx=20, ipadx=5)


# DEFINE AND PLACE PARAMETERS LABELS AND ENTRY BOXES ON THE WINDOW
# Labels
num_contracts_lbl = tk.Label(parm_frame, text='Rủi Ro:')
num_contracts_lbl.grid(row=0, column=0, padx=5, sticky=tk.E)

entry_price_lbl = tk.Label(parm_frame, text='Entry Price:')
entry_price_lbl.grid(row=1, column=0, padx=5, sticky=tk.E)

exit_price_lbl = tk.Label(parm_frame, text='Giá cắt lỗ:')
exit_price_lbl.grid(row=2, column=0, padx=5, sticky=tk.E)


total_risk_lbl = tk.Label(parm_frame , text='Đòn bẩy:')
total_risk_lbl.grid(row=3, column=0, padx=5, sticky=tk.E)

Gia_thanh_lylbl = tk.Label(parm_frame , text='Giá thanh lý:')
Gia_thanh_lylbl.grid(row=4, column=0, padx=5, sticky=tk.E)

# Entry boxes
num_contracts_box = tk.Entry(parm_frame, textvariable=num_contracts_var, width=11)
num_contracts_box.grid(row=0, column=1, pady=5, sticky=tk.E)

entry_price_box = tk.Entry(parm_frame, textvariable=entry_price_var, width=11)
entry_price_box.grid(row=1, column=1, pady=5, sticky=tk.E)

exit_price_box = tk.Entry(parm_frame, textvariable=exit_price_var, width=11)
exit_price_box.grid(row=2, column=1, pady=5, sticky=tk.E)

donbay = tk.StringVar()

total_risk_box = ttk.Combobox(parm_frame , width=8,textvariable = donbay)
total_risk_box['values'] = ('5', 
                          '10',
                          '15',
                          '20',
                          '25',
                          '30', 
                          '35', 
                          '50')
total_risk_box.grid(row=3, column=1, pady=5, sticky=tk.E)

giathanhly_box = tk.Entry(parm_frame , textvariable=Gia_thanh_ly, width=11)
giathanhly_box.grid(row=4, column=1, pady=5, sticky=tk.E)

#---------------------- OUTPUT--------------------

keyqua = tk.Label(output_frame, text='Khối lượng:')
keyqua.grid(row=0, column=0, padx=5, sticky=tk.E)

#------------ End output--------------
keyquakhoiluong = tk.Label(output_frame, text='0.001')
keyquakhoiluong.grid(row=0, column=1, padx=5, sticky=tk.E)
# create calculate button
calc_button = tk.Button(root, text='Calculate', )
calc_button.grid(row=3, column=1, sticky=tk.W, pady=5)

# CREATE BUTTON TO CLEAR ALL FIELDS
# function to control the clear button
# create clear button
clear_button = tk.Button(root, text='Reset',)
clear_button.grid(row=3, column=0, sticky=tk.E, pady=5, padx=5)

root.mainloop()