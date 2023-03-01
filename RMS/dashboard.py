from tkinter import*
from course import CourseClass
from student import studentClass
from PIL import Image,ImageTk
from result import resultClass
from report import reportClass
class RMS: 
    def __init__(self,root):
      self.root=root
      self.root.title("Student Result Management System")
      self.root.config(bg="white")
      #=========title==========
      title=Label(self.root,text="Student Result Management System",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
      #===========menu==============
      M_Frame=LabelFrame(self.root,text="Menus",font=("Times new roman",15),bg="white")
      M_Frame.place(x=10,y=70,width=1340,height=80)

      btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
      btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)
      btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)
      btn_view=Button(M_Frame,text="View Student Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=680,y=5,width=200,height=40)
      btn_logout=Button(M_Frame,text="Log Out",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=900,y=5,width=200,height=40)
      btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=1120,y=5,width=200,height=40)
     
      self.lbl_course=Label(self.root,text="Total Courses\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
      self.lbl_course.place(x=400,y=600,width=300)    

      self.lbl_student=Label(self.root,text="Total Courses\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
      self.lbl_student.place(x=710,y=600,width=300)  

      self.lbl_result=Label(self.root,text="Total Results\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
      self.lbl_result.place(x=1020,y=600,width=300) 

    #========Content_window==============
      self.bg_img=Image.open("images/side.png")
      self.bg_img=self.bg_img.resize((920,350),Image.ANTIALIAS)
      self.bg_img=ImageTk.PhotoImage(self.bg_img) 

      self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=200,width=920,height=400)
    #=====footer=====
      footer=Label(self.root,text="SRMS-Student Result Management System\nContact us for any technical issue:997*****01",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)

    def add_course(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=CourseClass(self.new_win)

    def add_student(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=studentClass(self.new_win)

    def add_result(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=resultClass(self.new_win)

    def add_report(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=reportClass(self.new_win)

      
  
if __name__=='__main__':
  root=Tk()
  obj=RMS(root)
  root.mainloop()
        



