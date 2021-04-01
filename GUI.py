import tkinter as tk
import Registration as rg
import Taking_Entry as ta
import Deleting as dt
from admin_passwords import get_admin
from Initialise_firebase import initialise

initialise()
id=0
name=""

from PIL import Image,ImageTk
    
def create_window():
    global id,name
    root=tk.Toplevel(window)
    root.title("Registration")
    root.configure(background="#832cd6")
    root.state("zoomed")
    root.geometry("1366x768")
    background_label = tk.Label(
        root, background="#ededed", width=150, height=34)
    background_label.place(x=150, y=110)
    message = tk.Label(root, text="Registration-Desk", bg="#832cd6", fg="white", width=43,
                   height=1, font=('Sans', 25, 'bold'))
    message.place(x=230, y=40)
    lbl = tk.Label(root, text="Enter ID", width=20, height=2,
                   fg="black", bg="#ededed", font=('Sans', 15, ' bold '))
    lbl.place(x=400, y=160)

    txt = tk.Entry(root, width=20, bg="white", fg="black", font=('times', 17, ' bold '))
    txt.place(x=700, y=170)

    lbl2 = tk.Label(root, text="Enter Name", width=20, fg="black",
                    bg="#ededed", height=2, font=('Sans', 15, ' bold '))
    lbl2.place(x=400, y=220)
    txt2 = tk.Entry(root, width=20, bg="white", fg="black", font=('Times New Roman', 17, ' bold '))
    txt2.place(x=700, y=230)

    lbl4 = tk.Label(root, text="Choose Password", width=20, fg="black",
                    bg="#ededed", height=2, font=('Sans', 15, ' bold '))
    lbl4.place(x=400, y=280)
    lbl5 = tk.Label(root, text="(to login)", width=20, fg="black",
                    bg="#ededed", height=1, font=('Sans', 8, ' bold '))
    lbl5.place(x=450, y=315)
    txt4 = tk.Entry(root, width=20, bg="white", fg="black",
                    font=('Times New Roman', 17, ' bold '))
    txt4.place(x=700, y=290)
    
    lbl3 = tk.Label(root, text="Notification : ", width=20, fg="black", bg="#ededed", height=2,
                font=('Sans', 15, ' bold'))
    lbl3.place(x=410, y=350)
    

    def register():
        message = ""
        id=txt.get()
        name=txt2.get()
        pss=txt4.get()
        msg=rg.registration(id,name,pss)
        message = tk.Label(root, text=msg, bg="#ededed", fg="blue", width=40, height=2, activebackground="blue",
                   font=('times', 15, ' bold '))
        if(("already" in msg) or "Please" in msg):
            message.configure(fg="firebrick2")
        message.place(x=600, y=350)
        
    trainImg = tk.Button(root, text="Register", command=register, fg="black", bg="#c6c6c6", width=40, height=2,
                         activebackground="#00c146", font=('Sans', 15, ' bold '))
    trainImg.place(x=440, y=450)
    back_button=tk.Button(root,text="Back",command=root.destroy,fg="black",bg="#c6c6c6",width=40,height=2,
                     activebackground="firebrick2",font=('Sans',15,'bold'))
    back_button.place(x=440,y=540)                     


def create_window2():
    root1=tk.Toplevel(window)
    root1.title("Entry")
    root1.state("zoomed")
    root1.configure(background="#832cd6")
    root1.geometry("1366x768")
    
    background_label = tk.Label(root1, background="#ededed", width=150, height=34)
    background_label.place(x=150, y=110)
    message = tk.Label(root1, text="Entry-desk",  bg="#832cd6", fg="white", width=43,
                       height=1, font=('Sans', 30, 'bold'))
    message.place(x=150, y=30)
    def call():
        notif=ta.attend()
        message = tk.Label(root1, text=notif, bg="#ededed", fg="blue", width=30, height=2, activebackground="blue",
                   font=('times', 15, ' bold '))
        message.place(x=470,y=150)           
    trackImg = tk.Button(root1, text="Take Entry", command=call, fg="white", bg="#3f4884", width=50, height=2,
                         activebackground="#00c146", font=('Sans', 18, ' bold '))
    trackImg.place(x=300, y=400)
    back_button=tk.Button(root1,text="Back",command=root1.destroy,fg="white",bg="#3f4884",width=50,height=2,
                     activebackground="firebrick2",font=('Sans',18,'bold'))
    back_button.place(x=300,y=500)
                    

def password():
    root2=tk.Toplevel(window)
    root2.title("Login")
    root2.configure(background="#832cd6")
    root2.geometry("1366x768")
    root2.state("zoomed")
    
    background_label = tk.Label(
        root2, background="#ededed", width=165, height=33)
    background_label.place(x=100, y=110)
    
    def get_in():
        passw=txt3.get()
        username=txt2.get()
        user=get_admin()
        if username not in user.keys():
            retry_button=tk.Label(root2,text="Incorrect username. Please retry.",fg="red",bg="white", width=60, height=2, font=('Sans',15,'bold'))
            retry_button.place(x=300,y=290)
        elif user[username]!=passw:
            retry_button=tk.Label(root2,text="Incorrect password. Please retry.",fg="red",bg="white", width=60, height=2, font=('Sans',15,'bold'))
            retry_button.place(x=300,y=290)    
        else:
            root2.destroy()
            admin_login()
            #create_window()                       
    lbl2 = tk.Label(root2, text="Enter Username  :", width=20, fg="black",
                    bg="#ededed", height=2, font=('Sans', 15, ' bold '))
    lbl2.place(x=400, y=150)
    txt2 = tk.Entry(root2, width=20,bg="white", fg="black", font=('times', 20, ' bold '))
    txt2.place(x=700, y=158)
    lbl3 = tk.Label(root2, text="Enter Password  :", width=20, fg="black",
                    bg="#ededed", height=2, font=('Sans', 15, ' bold '))
    lbl3.place(x=400, y=218)
    txt3 = tk.Entry(root2, width=20,show="*",bg="white", fg="black", font=('times', 20, ' bold '))
    txt3.place(x=700, y=218)

    submit_button = tk.Button(root2, text="Login", command=get_in, fg="black", bg="#bfbfbf", width=70, height=3,
                              activebackground="#00c146", font=('Sans', 15, 'bold'))
    submit_button.place(x=250,y=370)
    back_button = tk.Button(root2, text="Back", command=root2.destroy, fg="black", bg="#bfbfbf", width=70, height=3,
                     activebackground="firebrick1", font=('Sans', 15, ' bold '))
    back_button.place(x=250, y=490)

def delete_ID():
    
    root4=tk.Toplevel(window)
    root4.title("Delete")
    root4.configure(background="#832cd6")
    root4.geometry("1366x768")
    
    root4.state("zoomed")
    background_label = tk.Label(
        root4, background="#ededed", width=150, height=34)
    background_label.place(x=150, y=110)
    message = tk.Label(root4, text="Deletion", bg="#832cd6", fg="white", width=43,
                       height=1, font=('Sans', 25, 'bold'))
    message.place(x=230, y=40)
    def delet():
        id=txt.get()
        dt.delete(id)
        
        def yes():
            dt.ch="y"
            dt.delete(id)
            message.configure(text=dt.notif)
            lbl.destroy()
            y.destroy()
            n.destroy()
        def no():
            dt.ch="n"
            dt.delete(id)
            message.configure(text=dt.notif)
            lbl.destroy()
            y.destroy()
            n.destroy()

        if(dt.check==1):
            lbl = tk.Label(root4, text="Are you sure you want to delete this ID?",
                           width=40, fg="black", bg="#ededed", height=2, font=('Sans', 15, ' bold '))
            lbl.place(x=255, y=360)
            y = tk.Button(root4, text="YES", command=yes, fg="white", bg="blue", width=8, height=1,
                                      activebackground="Red", font=('times', 15, 'bold'))
            y.place(x=780, y=365)
            n = tk.Button(root4, text="NO", command=no, fg="white", bg="blue", width=8, height=1,
                            activebackground="Red", font=('times', 15, ' bold '))
            n.place(x=930, y=365)
 
        message = tk.Label(root4, text=dt.notif, width=30, fg="blue2", bg="#ededed", height=2,
                           font=('Sans', 15, ' bold'))
        message.place(x=600, y=250)

        
    '''lbl = tk.Label(root4, text="Enter ID",  width=20, height=2,
                   fg="black", bg="#ededed", font=('Sans', 15, ' bold '))
    lbl.place(x=400, y=150)
    txt = tk.Entry(root4, width=20,  bg="white",
                   fg="black", font=('times', 17, ' bold '))
    txt.place(x=700, y=165)
    lbl3 = tk.Label(root4, text="Notification : ",  width=20, height=2,
                    fg="black", bg="#ededed", font=('Sans', 15, ' bold '))
    lbl3.place(x=280, y=250)
    submit_button = tk.Button(root4, text="Delete", command=delet, fg="black", bg="#c6c6c6", width=40, height=2,
                              activebackground="firebrick2", font=('Sans', 15, 'bold'))
    submit_button.place(x=440, y=450)'''
    back_button = tk.Button(root4, text="Back", command=root4.destroy, fg="black", bg="#c6c6c6", width=40, height=2,
                            activebackground="firebrick2", font=('Sans', 15, 'bold'))
    back_button.place(x=440, y=540)                     
   
def admin_login():
    root5=tk.Toplevel(window)
    root5.title("Admin")
    root5.configure(background="#832cd6")
    root5.geometry("1366x768")
    root5.state("zoomed")

    background_label = tk.Label(root5, background="#474747", width=165, height=39)
    background_label.place(x=100, y=60)
    register_button = tk.Button(root5, text="Register", command=create_window, fg="white", bg="#565656", width=50, height=2,
                                 activebackground="#00c146", font=('Sans', 17, ' bold '))
    register_button.place(x=320, y=250)
    '''delete = tk.Button(root5, text="Delete By ID", command=delete_ID, fg="white", bg="#565656", width=50, height=2,
                        activebackground="#00c146", font=('Sans', 17, ' bold '))
    delete.place(x=320, y=260)'''
    back_button = tk.Button(root5, text="Back", command=root5.destroy, fg="white", bg="#565656", width=50, height=2,
                             activebackground="firebrick2", font=('Sans', 17, ' bold '))
    back_button.place(x=320, y=350)

window=tk.Tk()
window.title("Home")
window.geometry("1366x768")

window.configure(background="#832cd6")
window.state("zoomed")
background_label = tk.Label(window, background="#474747", width=165, height=34)
background_label.place(x=100, y=120)



message = tk.Label(window, text="Face-Recognition-Based-Entry-Management-System", bg="#832cd6", fg="white", width=50,
                   height=1, font=("Comic Sans", 25, 'bold'))
message.place(x=170, y=40)
trainImg = tk.Button(window, text="Register", command=password, fg="white", bg="#505050", width=50, height=3,
                     activebackground="#00c146", font=('Sans', 17, ' bold '))
trainImg.place(x=320, y=180)                   
trackImg = tk.Button(window, text="Entry", command=create_window2, fg="white", bg="#505050", width=50, height=3,
                     activebackground="#00c146", font=('Sans', 17, ' bold '))
trackImg.place(x=320, y=320)
Quit_button=tk.Button(window,text="Quit",command=window.destroy,fg="white",bg="#505050", width=50, height=3,
                      activebackground="firebrick2", font=('Sans', 17, 'bold'))
Quit_button.place(x=320,y=480)

window.mainloop()