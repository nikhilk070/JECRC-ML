#GUI - graphical user interface
# library
# 1. tkinter
# 2. pyQT
# 3. turtle

import tkinter as ttk

app = ttk.Tk()

app.title('My App')
app.geometry('600x400')
ttk.lable(app, text = 'A simple text lable').place(x=50,y=50)


app.mainloop()
