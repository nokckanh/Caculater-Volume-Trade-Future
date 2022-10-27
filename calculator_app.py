import string
import tkinter as tk
from tkinter import StringVar, messagebox
from tkinter import ttk
from decimal import Decimal


# MAIN WINDOW
root = tk.Tk()
root.title("Caculater Volume")
root.geometry('220x360-40+400')
# root.resizable(0, 0) 

# for entry boxes
RuiRo = tk.DoubleVar()     
entry_price = tk.DoubleVar()
stoploss_price = tk.DoubleVar()
thanhly_price = tk.DoubleVar()
donbay = tk.StringVar()
str = tk.StringVar()
volume = tk.DoubleVar()
giathanhly = 15000

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

entry_price_lbl = tk.Label(parm_frame, text='Giá vào lệnh:')
entry_price_lbl.grid(row=1, column=0, padx=5, sticky=tk.E)

exit_price_lbl = tk.Label(parm_frame, text='Giá cắt lỗ:')
exit_price_lbl.grid(row=2, column=0, padx=5, sticky=tk.E)


total_risk_lbl = tk.Label(parm_frame , text='Đòn bẩy:')
total_risk_lbl.grid(row=3, column=0, padx=5, sticky=tk.E)


# Entry boxes
num_contracts_box = tk.Entry(parm_frame, textvariable=RuiRo, width=11)
num_contracts_box.grid(row=0, column=1, pady=5, sticky=tk.E)

entry_price_box = tk.Entry(parm_frame, textvariable=entry_price, width=11)
entry_price_box.grid(row=1, column=1, pady=5, sticky=tk.E)

exit_price_box = tk.Entry(parm_frame, textvariable=stoploss_price, width=11)
exit_price_box.grid(row=2, column=1, pady=5, sticky=tk.E)


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

#------ Kiem tra LONG SHORT ------------
def CheckLongShort(entry,stoploss):
    strin = 'Bạn đang SHORT'
    if entry > stoploss:
        strin = 'bạn đang LONG'
        return strin
    else:
        return strin

#------ END Kiem tra LONG SHORT ------------

#---------- Update process ---------------

update_in_process = False

def callback():
    global update_in_process
    if update_in_process: return
    try:
        entry = entry_price.get()
        stoploss = stoploss_price.get()
    except ValueError:
        return
    new_status = CheckLongShort(entry,stoploss)
    update_in_process = True
    str.set(new_status)
    update_in_process = False
    print(str.get())
    ketqualongshort = tk.Label(output_frame, text= str.get())
    ketqualongshort.grid(row=2, column=0, padx=5, sticky=tk.E)
    root.after(1000, callback)
    
def calVolume():
    global update_in_process
    if update_in_process: return
    try:
        entry = entry_price.get()
        stoploss = stoploss_price.get()
    except ValueError:
        return
    new_volume = entry + stoploss 
    update_in_process = True
    volume.set(new_volume)
    update_in_process = False
    print(volume.get())
    keyquakhoiluong = tk.Label(output_frame, text=volume.get())
    keyquakhoiluong.grid(row=0, column=1, padx=5, sticky=tk.E)
    root.after(1000, calVolume)
    
callback()

calVolume()

# ------------ End Update process --------------

#---------------------- OUTPUT--------------------




keyqua = tk.Label(output_frame, text='Khối lượng:')
keyqua.grid(row=0, column=0, padx=5, sticky=tk.E)


Gia_thanh_lylbl = tk.Label(output_frame , text='Giá thanh lý:')
Gia_thanh_lylbl.grid(row=1, column=0, padx=5, sticky=tk.E)

ketquathanhly = tk.Label(output_frame, text='{giathanhly} BUSD'.format(giathanhly =  giathanhly))
ketquathanhly.grid(row=1, column=1, padx=5, sticky=tk.E)






root.mainloop()