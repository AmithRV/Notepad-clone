import os
import webbrowser
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import scrolledtext
from datetime import datetime
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile

win=tk.Tk()

fname='paste'

fname_font='fname_font'

win.title("Notepad Clone")
win.geometry('800x505')

win.resizable(0, 0) # 4 Disable resizing the GUI

label=Label(win,font=('Helvetica', 12))
label['text']='hello'
label.place(relx=0.8,rely=1,anchor='sw')

label2=Label(win,font=('Helvetica', 12))

label2.place(relx=0.3,rely=1,anchor='s')

def secure():
    print("Secure")


def update():
    time=str(datetime.now().strftime('%d-%m-%y  %H:%M:%S'))
    label['text']=time
    win.after(1000,update)

update()
def font_fun():
   
    root=tk.Tk()
    root.title("Python GUI")
    root.geometry('300x250')

    def fun():
        if fontChosen.get()=='Arial':
            font_style='Arial'
        elif fontChosen.get()=='Consolas':
            font_style='Consolas'
        elif fontChosen.get()=='Cambria':
            font_style='Cambria'
        elif   fontChosen.get()=='Candra':
            font_style='Candra'

        ttk.Label(root, text="\t",font=(font_style,int(28)) ).grid(column=1, row=10,pady=15)   

        ttk.Label(root, text="AaBbYyZz",font=(font_style,int(sizeChosen.get())) ).grid(column=1, row=10,pady=15)  


    # Adding a 1-combo box
    ttk.Label(root, text="Font : ").grid(column=0, row=1, padx=20, pady=20 )

    font= tk.StringVar()                         
    fontChosen = ttk.Combobox(root, width=12, textvariable=font)
    fontChosen['values'] = ('Consolas', 'Arial', 'Cambria','Candra')   #default value appear is 1  
    fontChosen.grid(column=1, row=1, padx=20, pady=20)              
    fontChosen.current(1)

    # Adding a 2-combo box
    ttk.Label(root, text="Size : ").grid(column=0, row=2, padx=0, pady=0 )

    size= tk.StringVar()                         
    sizeChosen = ttk.Combobox(root, width=12, textvariable=size)
    sizeChosen['values'] = (12,14,16,18,20,22,24,28)   #default value appear is 1  
    sizeChosen.grid(column=1, row=2, padx=0, pady=0)              
    sizeChosen.current(1)
    # Adding a Button                                            
    action = ttk.Button(root, text="OK", command=fun)  
    action.grid(column=1, row=14, padx=20, pady=20)

    root.mainloop()

def copy_fun():
    temp = str(scr.get(1.0,END)) #scr is the name of the scrollable text box
    fobj=open(fname,'w')
    fobj.write(temp)
    fobj.close()

def cut_fun():
    temp = str(scr.get(1.0,END)) #scr is the name of the scrollable text box
    fobj=open(fname,'w')
    fobj.write(temp)
    fobj.close()
    scr.delete('1.0',END) # to clear the textbox

def paste_fun():
    fobj=open(fname,'r')
    temp=fobj.read()
    scr.insert(tk.INSERT,temp)

def create_new_list():
    print("inside function")
    

def open_file():
    file = askopenfile(mode ='r', filetypes =[('All files', '*.*'),('Python Files', '*.py'),('text files', '*.txt')])
    if file is not None:
        scr.delete('1.0',END) # to clear the textbox
        content = file.read()
        scr.insert(tk.INSERT,content)
        #scr.configure(state='disabled') # opening in read only format

    print(file.name)
    label2['text']=file.name

def save():
    files = [('All Files', '*.*'),('Python Files', '*.py'),('Text Document', '*.txt')]
    file = asksaveasfile(filetypes = files, defaultextension = files)

    text = str(scr.get(1.0,END)) #scr is the name of the scrollable text box
    if file is not None:
        file.write(text)
        file.close()   

def delete():
    scr.delete('1.0',END) # to clear the textbox



# Setting icon of master window 
p1 = PhotoImage(file = 'Notepad_Logo.png') 
win.iconphoto(False, p1) 

menuBar = Menu(win)       #  we are calling the tkinter constructor of the menu

win.config(menu=menuBar)  #  and assigning the  menu to our main GUI window
  
FileMenu = Menu(menuBar, tearoff=0)      # creating a menubar1
FileMenu.config(font=("Courier",12))     # changing the style & size of the content of filemenu

EditMenu = Menu(menuBar, tearoff=0)      # creating a menubar2
EditMenu.config(font=("Courier",12))     # changing the style & size of the content of filemenu

FormatMenu = Menu(menuBar, tearoff=0)    # creating a menubar3
FormatMenu.config(font=("Courier",12))   # changing the style & size of the content of filemenu

ViewMenu = Menu(menuBar, tearoff=0)      # creating a menubar4
ViewMenu.config(font=("Courier",12))     # changing the style & size of the content of filemenu

HelpMenu = Menu(menuBar, tearoff=0)      # creating a menubar5
HelpMenu.config(font=("Courier",12))     # changing the style & size of the content of filemenu

SecureMenu = Menu(menuBar, tearoff=0)      # creating a menubar6
SecureMenu.config(font=("Courier",12))     # changing the style & size of the content of filemenu

# names of the menu_bar
menuBar.add_cascade(label="  File   ",      menu =  FileMenu)
menuBar.add_cascade(label="  Edit   ",     menu =  EditMenu)
menuBar.add_cascade(label="  Format ", menu =  FormatMenu)
menuBar.add_cascade(label="  View   ",    menu = ViewMenu)
menuBar.add_cascade(label="  Secure ",   menu = SecureMenu)
menuBar.add_cascade(label="  Help   ",     menu = HelpMenu)

#contents of FileMenu
FileMenu.add_command(label="New",command=lambda: os.system('python notepad.py'))
FileMenu.add_separator()
FileMenu.add_command(label="New Window",command=lambda: os.system('python notepad.py'))
FileMenu.add_separator()
FileMenu.add_command(label="Open",command=lambda: open_file())
FileMenu.add_separator()
FileMenu.add_command(label="Save",command=lambda:save())
FileMenu.add_separator()
FileMenu.add_command(label="Save As",command=lambda:save())
FileMenu.add_separator()
FileMenu.add_command(label="Page Setup",command=lambda:create_new_list())
FileMenu.add_separator()
FileMenu.add_command(label="Print",command=lambda:create_new_list())
FileMenu.add_separator()
FileMenu.add_command(label="Exit",command=quit)

#contents of EditMenu
EditMenu.add_command(label="Undo",command=lambda:create_new_list())
EditMenu.add_separator()
EditMenu.add_command(label="Cut",command=lambda:cut_fun())
EditMenu.add_separator()
EditMenu.add_command(label="Copy",command=lambda:copy_fun())
EditMenu.add_separator()
EditMenu.add_command(label="Paste",command=lambda:paste_fun())
EditMenu.add_separator()
EditMenu.add_command(label="Delete",command=lambda:delete())
EditMenu.add_separator()
EditMenu.add_command(label="Exit",command=quit)

#contents of FormatMenu
FormatMenu.add_command(label="Font",command=lambda:font_fun())


#contents of ViewMenu
ViewMenu.add_command(label="Zoom",command=lambda:create_new_list())
ViewMenu.add_separator()
ViewMenu.add_command(label="Status Bar",command=lambda:create_new_list())

#contents of HelpMenu
HelpMenu.add_command(label="View Help",command= lambda:webbrowser.open('https://go.microsoft.com/fwlink/?LinkId=834783'))
HelpMenu.add_separator()
HelpMenu.add_command(label="Send Feedback",command= lambda:webbrowser.open('http://example.com'))
HelpMenu.add_separator()
HelpMenu.add_command(label="About Notepad",command=lambda: os.system('python license.py'))

#contents of SecureMenu
SecureMenu.add_command(label=" Password ",command=lambda:secure())

#Using a scrolled Text control

scrolW = 71
scrolH = 21

font='Arial'
font_size=14

scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH,wrap=tk.WORD,font=(font,font_size))
scr.grid(column=0, columnspan=3) 
scr.focus()

win.mainloop()

