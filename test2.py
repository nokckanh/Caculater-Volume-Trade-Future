import tkinter as tk
import re

def validate(string):
    regex = re.compile(r"(\+|\-)?[0-9,]*$")
    result = regex.match(string)
    return (string == ""
            or (string.count('+') <= 1
                and string.count('-') <= 1
                and string.count(',') <= 1
                and result is not None
                and result.group(0) != ""))
    
def on_validate(P):
    return validate(P)    
    
root = tk.Tk()
entry = tk.Entry(root, validate="key")
vcmd = (entry.register(on_validate), '%P')
entry.config(validatecommand=vcmd)
entry.pack()
root.mainloop()