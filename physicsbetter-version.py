from tkinter import *
from tkinter import font
# ===================================== Creating Screen ===========================================================================
root = Tk()
root.geometry('1500x900')
root.title('Physic Solver')
root.iconbitmap('D:\Omar\Codezilla\PhysicsApp\Images\mrahmed.ico')
root.resizable(False,False)
# ============================================================ Colors and Fonts =========================================================
mainColor = 'grey'
mainFont = 'sans-serif'
backgroundColor = '#4B4E6D'
mainBackground ='#3C6997'
secondaryColor = '#011936'
thirdColor = '#3E4C5E'
fourthColor = '#3C6997'
saphireBlue ='#0C6291'
secondaryFont = 'tajawal'
thirdFont ='Russo One', 'sans-serif'
root.config(bg='#3C6997')
# ======================================== Results Variables ==================================================================================
#resultedIntesnity = StringVar()
#resultedPotentialDifference = StringVar()
#resultedRestience = StringVar()
firstlabeltext = StringVar()
secondlabeltext = StringVar()
results = StringVar()
results.set('                    Choose Operation                    ')
#========================================= Labels =============================================================================================

solveequation= Label(root,text='Solve The Physics problem',font=(thirdFont,30,'bold'),fg='white',bg=mainBackground)
solveequation.place(x=400,y=400)

firstlabel= Label(root,text=('Choose an operation'),font=(mainFont,20),fg='white',bg=mainBackground)
firstlabel.place(x=400,y=450)

firstlabelentry=Entry(root,justify=CENTER,width=30,fg='white',bg=thirdColor,state=DISABLED)

secondlabel = Label(root,text='from above',font=(mainFont,20),fg='white',bg=mainBackground)
secondlabel.place(x=670,y=450)

secondlabelentry =Entry(root,justify=CENTER,width=30,fg='white',bg=thirdColor,state=DISABLED)

resulttextlabel= Label(root,text='Results =',font=(mainFont,20),fg='white',bg=mainBackground)


resultlabel = Label(root,textvariable=results,font=(mainFont,20),fg='white',bg=saphireBlue)


# ======================================== Functions ============================================================================================
#=========================================== Credit ===========================================================================================
def credit():
    global namess
    global ahmedSamir
    # creditwindow = Toplevel()
    # creditwindow.title('Credits')
    # creditwindow.resizable(False,False)
    # creditwindow.geometry('455x150')
    # creditwindow.config(bg='#3C6997')
    # creditlabel= Label(creditwindow,text='This app was made for Mr.Ahmed samir',font=('tajawal',19),bg=saphireBlue,fg='white')
    # bylabelM= Label(creditwindow,text='By: Mohamed Mahmoud',font=('tajawal',19),bg=saphireBlue,fg='white')
    # bylabelO= Label(creditwindow,text='By: Omar El-Sawy',font=('tajawal',19),bg=saphireBlue,fg='white')
    # creditlabel.place(x=0,y=0)
    # bylabelM.place(x=0,y=100)
    # bylabelO.place(x=0,y=50)
    firstlabel.place(x=0,y=6000)
    firstlabelentry.place(x=0,y=6000)
    secondlabel.place(x=0,y=6000)
    secondlabelentry.place(x=0,y=6000)
    calculatebutton.place(x=0,y=6000)
    resultlabel.place(x=0,y=6000)
    resulttextlabel.place(x=0,y=6000)
    try:
        solveequation.destroy()
    except NameError:
        pass
    namess = Label(root,text='By Omar Elsawy And Mohamed Mahmoud',width=50,height=5,font=(mainFont,20,'bold'),fg='white',bg=mainBackground)
    namess.place(x=300,y=400)
    ahmedSamir = Label(root,text='To Mr Ahmed Samir',width=30,height=2,font=(mainFont,20,'bold'),fg='white',bg=mainBackground)
    ahmedSamir.place(x=450,y=500)
# ======================================== Intesnity Function ==================================================================================

def Intensity():
    try:
        solveequation.destroy()
        namess.destroy()
        ahmedSamir.destroy()
    except NameError:
        pass
    firstlabeltext.set('Enter Quantity')
    firstlabel.config(textvariable=firstlabeltext)
    secondlabeltext.set('Enter Seconds')
    secondlabel.config(textvariable=secondlabeltext)
    firstlabelentry.config(state=NORMAL)
    secondlabelentry.config(state=NORMAL)
    firstlabelentry.delete(0,END)
    secondlabelentry.delete(0,END)
    calculatebutton.config(text='Calculate',command=IntensityValue,state=NORMAL)
    secondlabelentry.place(x=700,y=360)
    firstlabelentry.place(x=700,y=260)
    calculatebutton.place(x=620,y=420)
    resultlabel.place(x=575,y=550)
    resulttextlabel.place(x=400,y=550)
    firstlabel.place(x=400,y=250)
    secondlabel.place(x=400,y=350)
    results.set('                    Enter Values                    ')
def IntensityValue():
    try:
        quantity = float(firstlabelentry.get())
        time = float(secondlabelentry.get())
        results.set('                    '+str(quantity/time)+' Ampere                    ')
        resultlabel.config(textvariable=results)
    except ValueError:
        results.set('                    ERROR                    ')
        resultlabel.config(textvariable=results)

# ========================================================= Potential Difference Function ==============================================================

def potentialdifference():
    try:
        solveequation.destroy()
        namess.destroy()
        ahmedSamir.destroy()
    except NameError:
        pass
    firstlabeltext.set('Enter the Work')
    secondlabeltext.set('Enter the Quantity')
    firstlabel.config(textvariable=firstlabeltext)
    secondlabel.config(textvariable=secondlabeltext)
    firstlabelentry.delete(0,END)
    secondlabelentry.delete(0,END)
    firstlabelentry.config(state=NORMAL)
    secondlabelentry.config(state=NORMAL)
    results.set('                    Enter Values                    ')
    secondlabelentry.place(x=700,y=360)
    firstlabelentry.place(x=700,y=260)
    calculatebutton.place(x=620,y=420)
    resultlabel.place(x=575,y=550)
    resulttextlabel.place(x=400,y=550)
    secondlabel.place(x=400,y=350)
    firstlabel.place(x=400,y=250)
    calculatebutton.config(text='Calculate',command=PotentialValue,state=NORMAL)
def PotentialValue():
    try:
        work = float(firstlabelentry.get())
        quan = float(secondlabelentry.get())
        results.set('                    '+str(work/quan)+ ' Volt                    ')
        resultlabel.config(textvariable=results)
    except ValueError:
        results.set('                    ERROR                    ')
        resultlabel.config(textvariable=results)

# ================================================ Resitence Fuction ================================================================================
def Resistance():
    try:
        solveequation.destroy()
        namess.destroy()
        ahmedSamir.destroy()
    except NameError:
        pass
    firstlabeltext.set('Enter P.Difference:')
    secondlabeltext.set('Enter Intesnity:')
    firstlabel.config(textvariable=firstlabeltext)
    secondlabel.config(textvariable=secondlabeltext)
    firstlabelentry.delete(0,END)
    secondlabelentry.delete(0,END)
    firstlabelentry.config(state=NORMAL)
    secondlabelentry.config(state=NORMAL)
    results.set('                    Enter Values                    ')
    secondlabelentry.place(x=700,y=360)
    firstlabelentry.place(x=700,y=260)
    calculatebutton.place(x=620,y=420)
    resultlabel.place(x=575,y=550)
    resulttextlabel.place(x=400,y=550)
    secondlabel.place(x=400,y=350)
    firstlabel.place(x=400,y=250)
    calculatebutton.config(text='Calculate',command=ResistanceValue,state=NORMAL)

def ResistanceValue():
    try:
        volt= float(firstlabelentry.get())
        ampere= float(secondlabelentry.get())
        results.set('                    '+str(volt/ampere)+' Ohm                    ')
        resultlabel.config(textvariable=results)
    except ValueError:
        results.set('                    ERROR                    ')

#====================================================== V BATTERY==============================================================================
def vbattery():
    try:
        solveequation.destroy()
        namess.destroy()
        ahmedSamir.destroy()
    except NameError:
        pass
    firstlabeltext.set('Enter I Main')
    secondlabeltext.set('Enter R eq + R int')
    firstlabel.config(textvariable=firstlabeltext)
    secondlabel.config(textvariable=secondlabeltext)
    firstlabelentry.delete(0,END)
    secondlabelentry.delete(0,END)
    firstlabelentry.config(state=NORMAL)
    secondlabelentry.config(state=NORMAL)
    results.set('                    Enter Values                    ')
    secondlabelentry.place(x=700,y=360)
    firstlabelentry.place(x=700,y=260)
    calculatebutton.place(x=620,y=420)
    resultlabel.place(x=575,y=550)
    resulttextlabel.place(x=400,y=550)
    secondlabel.place(x=400,y=350)
    firstlabel.place(x=400,y=250)
    calculatebutton.config(text='Calculate',command=vbatteryvalue,state=NORMAL)
def vbatteryvalue():
    try:
        imain= float(firstlabelentry.get())
        requiv= float(secondlabelentry.get())
        results.set('                    '+str(imain*requiv)+' Volt                    ')
        resultlabel.config(textvariable=results)
    except ValueError:
        results.set('                    ERROR                    ')

#============================================================ I Main ============================================================================
def imain():
    try:
        solveequation.destroy()
        namess.destroy()
        ahmedSamir.destroy()
    except NameError:
        pass
    firstlabeltext.set('Enter VB')
    secondlabeltext.set('Enter R eq + R int')
    firstlabel.config(textvariable=firstlabeltext)
    secondlabel.config(textvariable=secondlabeltext)
    firstlabelentry.delete(0,END)
    secondlabelentry.delete(0,END)
    firstlabelentry.config(state=NORMAL)
    secondlabelentry.config(state=NORMAL)
    results.set('                    Enter Values                    ')
    secondlabelentry.place(x=700,y=360)
    firstlabelentry.place(x=700,y=260)
    calculatebutton.place(x=620,y=420)
    resultlabel.place(x=575,y=550)
    resulttextlabel.place(x=400,y=550)
    secondlabel.place(x=400,y=350)
    firstlabel.place(x=400,y=250)
    calculatebutton.config(text='Calculate',command=imainvalue,state=NORMAL)
def imainvalue():
    try:
        vbat= float(firstlabelentry.get())
        RequiredMAIN= float(secondlabelentry.get())
        results.set('                    '+str(vbat/RequiredMAIN)+' Ampere                    ')
        resultlabel.config(textvariable=results)
    except ValueError:
        results.set('                    ERROR                    ')

# ======================================= Screen ===============================================================================================
title = Label(root, text='Solve The Physics Problems', fg='white', bg='#3C6997',font=(thirdFont,20,'bold'),height=50)
#title.pack(fill=X)

intesnityButton = Button(root,text='Intensity',fg='white',bg=saphireBlue,width=30,height=5,relief='groove',bd=1,font=(secondaryFont),command=Intensity)
intesnityButton.place(x=30,y=50)

potenialButton = Button(root,text='Potential Difference',fg='white',bg=saphireBlue,width=30,height=5,relief='groove',bd=1,font=(secondaryFont),command=potentialdifference)
potenialButton.place(x=320,y=50)

restienceButton = Button(root,text='Resistance',fg='white',bg=saphireBlue,width=30,height=5,relief='groove',bd=1,font=(secondaryFont),command=Resistance)
restienceButton.place(x=620,y=50)

mainIntensityButton = Button(root,text='Main Intensity In Current',fg='white',bg=saphireBlue,width=30,height=5,relief='groove',bd=1,font=(secondaryFont),command=imain)
mainIntensityButton.place(x=920,y=50)

vbatteryButton = Button(root,text='Battery Voltage',fg='white',bg=saphireBlue,width=30,height=5,relief='groove',bd=1,font=(secondaryFont),command=vbattery)
vbatteryButton.place(x=1220,y=50)

calculatebutton = Button(root,text='Choose operation',fg='white',bg=saphireBlue,width=30,height=2,relief='groove',bd=1,font=(secondaryFont),state=DISABLED)

#========================================= Credits button =================================================================================
creditsbutton= Button(root,text='Credits',fg='white',bg=saphireBlue,width=30,height=3,relief='groove',bd=1,font=(secondaryFont),command=credit)
creditsbutton.place(x=620,y=800)

root.mainloop()