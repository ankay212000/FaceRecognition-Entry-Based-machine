import tkinter as tk
import Registration as rg
import Taking_Attendance as ta
import Deleting as dt
id=0
name=""

    
def create_window():
    global id,name
    root=tk.Toplevel(window)
    root.title("Registration")
    root.configure(background='white')
    root.state("zoomed")
    message = tk.Label(root, text="Registration-Desk", bg="blue", fg="white", width=43,
                   height=1, font=('times', 30, 'italic bold'))
    message.place(x=170, y=20)
    lbl = tk.Label(root, text="Enter ID", width=20, height=2, fg="black", bg="white", font=('times', 15, ' bold '))
    lbl.place(x=400, y=200)

    txt = tk.Entry(root, width=20, bg="blue", fg="white", font=('times', 15, ' bold '))
    txt.place(x=700, y=215)

    lbl2 = tk.Label(root, text="Enter Name", width=20, fg="black", bg="white", height=2, font=('times', 15, ' bold '))
    lbl2.place(x=400, y=300)
    txt2 = tk.Entry(root, width=20, bg="blue", fg="white", font=('times', 15, ' bold '))
    txt2.place(x=700, y=315)
    lbl3 = tk.Label(root, text="Notification : ", width=20, fg="black", bg="white", height=2,
                font=('times', 15, ' bold'))
    lbl3.place(x=250, y=400)
    

    def register():
        id=txt.get()
        name=txt2.get()
        rg.registration(id,name)
        message = tk.Label(root, text=rg.notif, bg="white", fg="blue", width=30, height=2, activebackground="blue",
                   font=('times', 15, ' bold '))
        message.place(x=600, y=400)
        
    trainImg = tk.Button(root, text="Registration", command=register, fg="white", bg="blue", width=113, height=3,
                     activebackground="Red", font=('times', 15, ' bold '))
    trainImg.place(x=0, y=500)
    back_button=tk.Button(root,text="Back",command=root.destroy,fg="white",bg="blue",width=113,height=3,
                     activebackground="Red",font=('times',15,'bold'))
    back_button.place(x=0,y=600)                     


def create_window2():
    root1=tk.Toplevel(window)
    root1.title("Attendance")
    root1.state("zoomed")
    root1.configure(background='white')
    message = tk.Label(root1, text="Attendance-desk", bg="blue", fg="white", width=43,
                   height=1, font=('times', 30, 'italic bold'))
    message.place(x=170, y=20)
    def call():
        ta.attend()    
    trackImg = tk.Button(root1, text="Take Attendance", command=call, fg="white", bg="blue", width=112, height=3,
                activebackground="Red", font=('times', 15, ' bold '))
    trackImg.place(x=2, y=500)
    back_button=tk.Button(root1,text="Back",command=root1.destroy,fg="white",bg="blue",width=113,height=3,
                     activebackground="Red",font=('times',15,'bold'))
    back_button.place(x=0,y=600)

def password():
    root2=tk.Toplevel(window)
    root2.title("Login")
    root2.configure(background="cyan2")
    root2.state("zoomed")
    def get_in():
        passw=txt2.get()
        if "pass" in passw:
            root2.destroy()
            admin_login()
        else:
            retry_button=tk.Label(root2,text="Retry",fg="black",bg="white", width=70, height=3, font=('times',15,'bold'))
            retry_button.place(x=250,y=500)                       
    lbl2 = tk.Label(root2, text="Enter Password", width=20, fg="black", bg="white", height=2, font=('times', 15, ' bold '))
    lbl2.place(x=400, y=200)
    txt2 = tk.Entry(root2, width=20,show="*",bg="blue", fg="white", font=('times', 15, ' bold '))
    txt2.place(x=700, y=215)
    submit_button=tk.Button(root2,text="Submit",command=get_in,fg="white",bg="blue", width=70, height=3,
                    activebackground="Red", font=('times',15,'bold'))
    submit_button.place(x=250,y=400)
    back_button= tk.Button(root2, text="Back", command=root2.destroy, fg="white", bg="blue", width=70, height=3,
                     activebackground="Red", font=('times', 15, ' bold '))
    back_button.place(x=250, y=600)

def delete_ID():
    
    root4=tk.Toplevel(window)
    root4.title("Delete")
    root4.configure(background="cyan2")
    root4.state("zoomed")
    def delet():
        id=txt.get()
        
        dt.delete(id)
        def yes():
            dt.ch="y"
            dt.delete(id)
            
            message = tk.Label(root4, text=dt.notif, bg="white", fg="blue", width=30, height=2, activebackground="blue",
                               font=('times', 15, ' bold '))
            message.place(x=630, y=250)
            lbl.destroy()
            y.destroy()
            n.destroy()
        def no():
            dt.ch="n"
            dt.delete(id)
            
            message = tk.Label(root4, text=dt.notif, bg="white", fg="blue", width=30, height=2, activebackground="blue",
                               font=('times', 15, ' bold '))
            message.place(x=630, y=250)
            lbl.destroy()
            y.destroy()
            n.destroy()

        if(dt.check==1):
            lbl = tk.Label(root4, text="Are you sure you want to delete this ID?", width=40, fg="black",bg="white", height=2, font=('times', 15, ' bold '))
            lbl.place(x=255, y=360)
            y = tk.Button(root4, text="YES", command=yes, fg="white", bg="blue", width=8, height=1,
                                      activebackground="Red", font=('times', 15, 'bold'))
            y.place(x=780, y=365)
            n = tk.Button(root4, text="NO", command=no, fg="white", bg="blue", width=8, height=1,
                            activebackground="Red", font=('times', 15, ' bold '))
            n.place(x=930, y=365)

        message = tk.Label(root4, text=dt.notif, bg="white", fg="blue", width=30, height=2, activebackground="blue",
                           font=('times', 15, ' bold '))
        message.place(x=600, y=250)

        

    lbl = tk.Label(root4, text="Enter ID", width=20, height=2, fg="black", bg="white", font=('times', 15, ' bold '))
    lbl.place(x=400, y=150)
    txt = tk.Entry(root4, width=20, bg="blue", fg="white", font=('times', 15, ' bold '))
    txt.place(x=700, y=165)
    lbl3 = tk.Label(root4, text="Notification : ", width=20, fg="black", bg="white", height=2,
                font=('times', 15, ' bold'))
    lbl3.place(x=280, y=250)
    submit_button = tk.Button(root4, text="Delete", command=delet, fg="white", bg="blue", width=70, height=2,
                              activebackground="Red", font=('times', 15, 'bold'))
    submit_button.place(x=250, y=500)
    back_button = tk.Button(root4, text="Back", command=root4.destroy, fg="white", bg="blue", width=70, height=2,
                            activebackground="Red", font=('times', 15, ' bold '))
    back_button.place(x=250, y=580)
    '''submit_button=tk.Button(root4,text='Delete',command=delet,width=35,fg='white',bg='blue',height=2,
                            activebackground='red',font=('times',15,'bold'))
    submit_button.place(x=500,y=600)'''                       



    
def admin_login():
    
    root5=tk.Toplevel(window)
    root5.title("Admin")
    root5.configure(background="cyan2")
    root5.state("zoomed")
    register_button=tk.Button(root5,text="Register",command=create_window,fg="black",bg="white",width=35,height=3,
                    activebackground="red",font=('times',15,'bold'))
    register_button.place(x=170,y=200)
    delete=tk.Button(root5,text="Delete By ID",command=delete_ID,fg="black",bg="white",width=35,height=3,
                    activebackground="red",font=('times',15,'bold'))
    delete.place(x=770,y=200)
    back_button=tk.Button(root5,text="Back",command=root5.destroy,fg="black",bg="white",width=35,height=3,
                    activebackground="red",font=('times',15,'bold'))
    back_button.place(x=500,y=400)                        

window=tk.Tk()
window.title("Home")
#window.configure(background='white')
window.state("zoomed")


message = tk.Label(window, text="Face-Recognition-Based-Attendance-Management-System", bg="blue", fg="white", width=43,
                   height=1, font=('times', 30, 'italic bold'))
message.place(x=170, y=20)
trainImg = tk.Button(window, text="Admin Login", command=password, fg="white", bg="blue", width=70, height=3,
                     activebackground="Red", font=('times', 15, ' bold '))
trainImg.place(x=250, y=200)                   
trackImg = tk.Button(window, text="Attendance", command=create_window2, fg="white", bg="blue", width=70, height=3,
                     activebackground="Red", font=('times', 15, ' bold '))
trackImg.place(x=250, y=400)
Quit_button=tk.Button(window,text="Quit",command=window.destroy,fg="white",bg="blue", width=70, height=3,
                    activebackground="Red", font=('times',15,'bold'))
Quit_button.place(x=250,y=600)

window.mainloop()
