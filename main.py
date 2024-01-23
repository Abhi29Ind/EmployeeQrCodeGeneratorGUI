from tkinter import*
import qrcode as q
from PIL import Image,ImageTk
from resizeimage import resizeimage

class Qr_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        #self.root.geometry("900x500+200+50")
        self.root.title("QR Generator | Developed by Abhishek and Aarushi")
        self.root.resizable(False,False)

        title=Label(self.root,text="  Qr Code Generator",font=("times new roman",40),bg='#053246',fg='white',anchor='w').place(x=0,y=0,relwidth=1)

        #+++++++++++ EMPLOYEE Details Window ++++++++++++++
        #+++++++++++Variables+++++++++++++
        self.var_emp_code=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_designation=StringVar()


        emp_Frame = Frame(self.root,bd=2, relief=RIDGE,bg='white')
        emp_Frame.place(x=50,y=100,width=500,height=380)
        emp_title = Label(emp_Frame,text=" Employee Details",font=("goudy old style",20),bg='#043246',fg='white').place(x=0,y=0,relwidth=1)
       
        lbl_emp_code = Label(emp_Frame,text="Employee ID",font=("times new roman",15,'bold'),bg='white').place(x=50,y=60)
        lbl_name = Label(emp_Frame,text="Name",font=("times new roman",15,'bold'),bg='white').place(x=50,y=100)
        lbl_department = Label(emp_Frame,text="Department",font=("times new roman",15,'bold'),bg='white').place(x=50,y=140)
        lbl_designation = Label(emp_Frame,text="Designation",font=("times new roman",15,'bold'),bg='white').place(x=50,y=180)
        
        txt_emp_code = Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_emp_code,bg='beige').place(x=250,y=60)
        txt_name = Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_name,bg='beige').place(x=250,y=100)
        txt_department = Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_department,bg='beige').place(x=250,y=140)
        txt_designation = Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_designation,bg='beige').place(x=250,y=180)
     
        btn_gen = Button(emp_Frame,text="QR Generate",command=self.generate,font=("times new roman",18,'bold'),bg='grey').place(x=50,y=260,width=180,height=30)
        btn_clr = Button(emp_Frame,text="Clear",command=self.clear,font=("times new roman",18,'bold'),bg='grey').place(x=275,y=260,width=180,height=30)

        self.mesg = " "
        self.lbl_mesg = Label(emp_Frame,text=self.mesg,font=("times new roman",20,'bold'),bg='white',fg='green')
        self.lbl_mesg.place(x=0,y=320,relwidth=1)

        #++++++++++++++Employee QR Code Window++++++++++++
        qr_Frame= Frame(self.root,bd=2, relief=RIDGE,bg='white')
        qr_Frame.place(x=600,y=100,width=250,height=380)
        qr_title = Label(qr_Frame,text=" Employee QR Code",font=("goudy old style",20),bg='#043246',fg='white').place(x=0,y=0,relwidth=1)
        
        self.qr_code=Label(qr_Frame,text='Qr Code not available',font=('time new roman',15),bg='#3f51b5',fg='white',bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)


    def clear(self):
        self.var_emp_code.set('')
        self.var_name.set('')
        self.var_department.set('')
        self.var_designation.set('')
        self.mesg = ' '
        self.lbl_mesg.config(text=self.mesg)
        self.qr_code.config(image='')

    def generate(self):
        if self.var_emp_code.get() =='' or self.var_department.get()=='' or self.var_designation.get()=='' or self.var_name.get()=='':
            self.mesg='All fields are required!'
            self.lbl_mesg.config(text=self.mesg,fg='red')
        else:
            qr_data=(f"Employee ID: {self.var_emp_code.get()}\nEmplyee Name: {self.var_name.get()}\nEmployee Designation: {self.var_designation.get()}\nEmployee Department:{self.var_department.get()}")
            qr_code = q.make(qr_data) 
           # print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("Employee_Qr/Emp_"+str(self.var_emp_code.get())+'.png')
            #====== Qr Code Image ========
            self.img=ImageTk.PhotoImage(file="Employee_Qr/Emp_"+str(self.var_emp_code.get())+'.png')
            self.qr_code.config(image=self.img)

            #====== Updating Information======
            self.mesg='QR Generated Sucessfully'
            self.lbl_mesg.config(text=self.mesg,fg='green')

        

root=Tk()
cl =Qr_Generator(root)    #4
root.mainloop()