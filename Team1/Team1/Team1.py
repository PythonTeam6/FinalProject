from tkinter import *

root = Tk()
form = '1200x600'
root.geometry(form)

str = 'kkk'
mlist = []

for r in range(6):
    root.rowconfigure(r, weight=1)    
for c in range(10):
    root.columnconfigure(c, weight=1)
    

frame = Frame(root, bg="red")
frame.grid(row = 0, column = 0, rowspan = 1, columnspan = 10, sticky = W+E+N+S) 
#frame.pack_propagate(0)
frame2 = Frame(root, bg="blue")
frame2.grid(row = 1, column = 0, rowspan = 5, columnspan = 5, sticky = W+E+N+S)
frame2.pack_propagate(0)
frame2.grid_propagate(0)
frame3 = Frame(root, bg="green")
frame3.grid(row = 1, column = 5, rowspan = 5, columnspan = 5, sticky = W+E+N+S)
#frame3.pack_propagate(0)

#frame = Frame(root, bg="red")
#frame.grid(row = 0, column = 0, columnspan = 2, rowspan = 1, sticky = W+E+N+S) 

#frame2 = Frame(root, bg="blue")
#frame2.grid(row = 1, column = 0, columnspan = 1, rowspan = 1, sticky = W+E+N+S)


#frame3 = Frame(root, bg="green")
#frame3.grid(row = 1, column = 1, columnspan = 1, rowspan = 1, sticky = W+E+N+S)

#root.rowconfigure(1, weight = 1)
#root.columnconfigure(0, weight = 1)
#root.columnconfigure(1, weight = 1)


def onExit():
    root.quit()

def addFile():
    from tkinter import filedialog
    filenames = filedialog.askopenfilenames(filetypes = (("mp3 files", "*.mp3"),("wma files", "*.wma"),("All files", "*.*")))
    str = root.splitlist(filenames)
    mlist = list(str)
    print(mlist)
    #mlist.append(str.split(','))
    #print(mlist)
    
    for k in range(len(mlist)):
        Label(frame2, text= "unchanged", relief=RIDGE).grid(row=k,column=0)
        Label(frame2, text = mlist[k]).grid(row=k,column=1, sticky = W)
        #mlabel = Label(frame2, text = mlist[k], fg = 'black')
        #mlabel.pack(padx = 10)
        #mlabel2 = Label(frame3, text = mlist[k], fg = 'black')
        #mlabel2.pack(anchor = W)

menubar = Menu(root)
root.config(menu = menubar)

fileMenu = Menu(menubar)
fileMenu.add_command(label="Add file", command = addFile)
fileMenu.add('separator')
fileMenu.add_command(label="Exit", command = onExit)
menubar.add_cascade(label="File", menu = fileMenu)

setMenu = Menu(menubar)
setMenu.add_command(label="String Format")
setMenu.add_checkbutton(label="Override")
menubar.add_cascade(label = "Setting", menu = setMenu)








root.title("Python Team6")
root.mainloop()





