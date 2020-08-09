from tkinter import*
import time
root = Tk()
root.title("Digital Clock")
root.geometry("1350x700+0+0")
#by defaul background color is sky blue
root.config(bg="#6698FF")

def clock():
    h = str(time.strftime("%H"))
    m = str(time.strftime("%M"))
    s = str(time.strftime("%S"))

    #if hour is greater than 12 then changing noon and repeating hour from the starting
    if int(h)>12 and int(m)>0:
        noon_lbl.config(text="PM")
        #if it is PM then background color changes to midnight blue
        root.config(bg="#151B54")
        cp_lbl.config(bg="#151B54")
        
    if int(h)>12:
        h = str((int(h)-12))
    
    hr_lbl.config(text=h)
    mnt_lbl.config(text=m)
    sec_lbl.config(text=s)

    #calling clock function after 200 miliseconds
    hr_lbl.after(200, clock)


hr_lbl = Label(root, text="12", font=("Times New Roman", 50, "bold"), bg="#0875B7", fg="white")
hr_lbl.place(x=350, y=200, width=150, height=150)

hr2_lbl = Label(root, text="Hour(s)", font=("Times New Roman", 20, "bold"), bg="#0875B7", fg="white")
hr2_lbl.place(x=350, y=360, width=150, height=50)

mnt_lbl = Label(root, text="12", font=("Times New Roman", 50, "bold"), bg="#008EA4", fg="white")
mnt_lbl.place(x=520, y=200, width=150, height=150)

mnt2_lbl = Label(root, text="Minute(s)", font=("Times New Roman", 20, "bold"), bg="#008EA4", fg="white")
mnt2_lbl.place(x=520, y=360, width=150, height=50)

sec_lbl = Label(root, text="12", font=("Times New Roman", 50, "bold"), bg="#79BAEC", fg="white")
sec_lbl.place(x=690, y=200, width=150, height=150)

sec2_lbl = Label(root, text="Second(s)", font=("Times New Roman", 20, "bold"), bg="#79BAEC", fg="white")
sec2_lbl.place(x=690, y=360, width=150, height=50)

noon_lbl = Label(root, text="AM", font=("Times New Roman", 50, "bold"), bg="#DF002A", fg="white")
noon_lbl.place(x=860, y=200, width=150, height=150)

noon_lbl2 = Label(root, text="Noon", font=("Times New Roman", 20, "bold"), bg="#DF002A", fg="white")
noon_lbl2.place(x=860, y=360, width=150, height=50)

cp_lbl = Label(root, text="(C) 2020 Digital Clock -> Python Project by Brijesh Vishwakarma", font=("Times New Roman", 11, "bold"), bg="#6698FF", fg="white")
cp_lbl.place(x=350, y=650, width=600, height=50)

clock()
root.mainloop()
