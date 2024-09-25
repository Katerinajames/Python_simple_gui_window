
#https://stackoverflow.com/questions/74429721/how-do-you-resize-the-window-size-of-a-tkinter-application-made-using-the-class

from tkinter import*

root=Tk()
label=Label(root,text='Hello there')
label.pack()
root.geometry("300x300")
root.mainloop()
