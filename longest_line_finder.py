from tkinter import *
import tkinter.messagebox as tmsg
result_line=''
def long(event):
    global result_line
    try:
        with open(f'{text.get()}.txt','r',encoding='utf-8') as file:
            longest=''
            for line in file:
                if len(line)>len(longest):
                    longest=line
                result_line=longest
                length=len(longest)
        myResult.config(text=f'{result_line}\nThe characters in the line is {length}')
    except:
        myResult.config(text="Files doesn't Exist")
    
    
root=Tk()
text=StringVar()
def about():
    tmsg.showinfo('About','Made with Smart Work By Aviral')

myMenu=Menu(root)
About=Menu(myMenu,tearoff=0)
About.add_command(label='About',command=about)
myMenu.add_cascade(label='About',menu=About)
root.configure(menu=myMenu)

root.title('Longest Line Finder')
root.geometry('400x300')
Label(text='Longest Line Finder',font='lucida 13 bold',pady=20).pack()
Label(text='Enter The Full Path Of The File').pack()
file_entry=Entry(textvariable=text)
file_entry.pack()
b=Button(text='Submit')
b.bind('<Button-1>',long)
b.pack()
f=Frame(root,bg='grey')
f.pack()
myResult=Label(f,text=result_line,font='lucida 9 bold')
myResult.pack()

root.mainloop()