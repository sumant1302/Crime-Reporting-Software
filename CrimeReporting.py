from tkinter import *
from tkinter import font
import mysql.connector as mysql
import tkinter.messagebox

userLoggedIn=False

#mysql connection
def about():

	aboutScreen=Toplevel(win)
	aboutScreen.title("About | Online Crime Reporting System")
	aboutScreen.geometry("300x200")


	global frameAbout
	frameAbout=Frame(aboutScreen)
	frameAbout["bg"]="white"

	Label(frameAbout, text="Onine Crime Reporting System", font=("Helvetica", 20), bg="white", fg="green", justify=LEFT).pack()
	Label(frameAbout, text="", font=("Helvetica", 20), fg="green", justify=LEFT).pack()

	Label(frameAbout, text="ABOUT", font="Times 20 bold", bg="white").pack()
	
	#aboutImage=PhotoImage(file="image.gif")
	frame1=Frame(frameAbout)
	frame1.pack()
	Label(frame1, text="Image").pack(side=LEFT,padx=50)
	Message(frame1, text="hkjjhsvd gcg hhkb hb hmnb shkb hmbjh bjssbck bjssnc asnm").pack(side=LEFT)

	frameAbout.pack()

def home():
	win["bg"]="white"
	
	global frameHome
	frameHome=Frame(win)
	
	frameHome["bg"]="white"
	labelHome=Label(frameHome, text="HOME", font=("Helvetica", 20), bg="white", fg="green", justify=LEFT).pack()
	Label(frameHome, text="").pack()
	btn1Home=Button(frameHome, width=10, height=2, text="File New\n Case", fg="white", bg="red", font=("Helvetica", 10), command=reportCase).pack(side=LEFT, padx=20)
	btn2Home=Button(frameHome, width=10, height=2, text="Check Status\n of Case", fg="white", bg="red",font=("Helvetica", 10), command=checkCaseStatus).pack(side=LEFT, padx=20)

	btn3Home=Button(frameHome, width=10, height=2, text="Login to\nyour account", fg="white", bg="red",font=("Helvetica", 10), command=userLoginWindow).pack(side=LEFT, padx=20)
	btn4Home=Button(frameHome, width=10, height=2, text="Contact Us", fg="white", bg="red",font=("Helvetica", 10)).pack(side=LEFT, padx=20)
	frameHome.pack(pady=10)


def register_user():
	regUserName=regName.get()
	regUserEmail=regEmail.get()
	regUserPassword=regPassword.get()
	regUserContact=regContact.get()
	regUserEmgContName=emgContName.get()
	regUserEmgCont=emgContMob.get()
	regUserEmgContRel=emgContRel.get()
	regUserAdd1=regAdd1.get()
	regUserAdd2=regAdd2.get()
	regUserCity=regCity.get()
	regUserState=regState.get()
	if regUserName=="" or regUserEmail=="" or regUserPassword=="" or regUserContact=="" or 		regUserEmgContName=="" or emgContName=="" or regUserAdd2=="" or regUserAdd1=="" or regUserCity=="" or 		regUserState=="" :
		tkinter.messagebox.showerror("User Registration Error!","All fields are Required. Please fill all fields to register.")
	else:
		con=mysql.connect(host="localhost", user="root", password="", database="crime_reporting")
		cursor=con.cursor()
		cursor.execute("insert into users values('""','"+regUserName +"','"+regUserEmail +"','"+regUserPassword +"','"+regUserContact +"','"+regUserEmgContName +"','"+regUserEmgCont +"','"+regUserEmgContRel +"','"+regUserAdd1 +"','"+regUserAdd2 +"','"+regUserCity +"','"+regUserState +"')")
		cursor.execute("commit")

		# file=open(regUserName+".txt","w")
		# file.write(regUserName+"\n")
		# file.write(regUserEmail+"\n")
		# file.write(regUserPassword+"\n")
		# file.write(regUserContact+"\n")
		# file.write(regUserEmgContName+"\n")
		# file.write(regUserEmgCont+"\n")
		# file.write(regUserEmgContMob+"\n")
		# file.write(regUserAdd1+"\n")
		# file.write(regUserAdd2+"\n")
		# file.write(regUserCity+"\n")
		# file.write(regUserState)
		# file.close()

		
		tkinter.messagebox.showinfo("Message", "Hey, "+regUserName +"! You have successfully Registered!")
		con.close()
		userRegisterWindow.destroy()


def register():
	global userRegisterWindow
	userRegisterWindow=Toplevel(win)
	userRegisterWindow.title("User Registeration")
	#userRegisterWindow["bg"]="white"
	userRegisterWindow.geometry("500x400")

	Label(userRegisterWindow,text="Online Crime Reporting System", font=("Helvetica",20)).grid(row=1, column=1, columnspan=3, padx=20, sticky=W)
	Label(userRegisterWindow,text="").grid(row=2, column=1, padx=20, sticky=W)

	Label(userRegisterWindow,text="Name:").grid(row=3, column=1, sticky=W)
	
	Label(userRegisterWindow,text="Email:").grid(row=4, column=1, sticky=W)
	Label(userRegisterWindow,text="Password:").grid(row=5, column=1, sticky=W)
	Label(userRegisterWindow,text="Contact Number:").grid(row=6, column=1, sticky=W)

	Label(userRegisterWindow,text="Enter Emergency Contact:").grid(row=7, column=1, sticky=W)
	Label(userRegisterWindow,text="Name:").grid(row=8, column=1, padx=20, sticky=W)
	Label(userRegisterWindow,text="Relation:").grid(row=9, column=1, padx=20, sticky=W)
	Label(userRegisterWindow,text="Contact. No.:").grid(row=10, column=1, padx=20, sticky=W)

	Label(userRegisterWindow,text="").grid(row=11, column=11, padx=20, sticky=W)

	Label(userRegisterWindow,text="Address Line 1:").grid(row=12, column=1, sticky=W)
	Label(userRegisterWindow,text="Address Line 2:").grid(row=13, column=1, sticky=W)
	Label(userRegisterWindow,text="City:").grid(row=14, column=1, sticky=W)
	Label(userRegisterWindow,text="State:").grid(row=15, column=1, sticky=W)

	global regName
	global regEmail
	global regPassword
	global regContact
	global emgContName
	global emgContMob
	global emgContRel
	global regAdd1
	global regAdd2
	global regCity
	global regState
		
	regName= StringVar()
	Entry(userRegisterWindow, textvariable=regName).grid(row=3, column=2)
	regEmail=StringVar()
	Entry(userRegisterWindow, textvariable=regEmail).grid(row=4, column=2)
	regPassword= StringVar()
	Entry(userRegisterWindow, textvariable=regPassword).grid(row=5, column=2)
	regContact=StringVar()
	Entry(userRegisterWindow, textvariable=regContact).grid(row=6, column=2)
	emgContName=StringVar()
	Entry(userRegisterWindow, textvariable=emgContName).grid(row=8, column=2)
	emgContRel=StringVar()
	Entry(userRegisterWindow, textvariable=emgContRel).grid(row=9, column=2)
	emgContMob=StringVar()
	Entry(userRegisterWindow, textvariable=emgContMob).grid(row=10, column=2)
	regAdd1=StringVar()
	Entry(userRegisterWindow, textvariable=regAdd1).grid(row=12, column=2)
	regAdd2=StringVar()
	Entry(userRegisterWindow, textvariable=regAdd2).grid(row=13, column=2)
	regCity=StringVar()
	Entry(userRegisterWindow, textvariable=regCity).grid(row=14, column=2)
	regState=StringVar()
	Entry(userRegisterWindow, textvariable=regState).grid(row=15, column=2)
	
	Label(userRegisterWindow,text="").grid(row=16, column=1, padx=20, sticky=W)

	
	btnRegister=Button(userRegisterWindow, text="Register", width=6,height=2,bg="#00ff00", command=register_user).grid(row=17, column=2, sticky=E)


def userLogin():
	userEmail=userEmailVar.get()
	userPassword=userPasswordVar.get()

	con=mysql.connect(host="localhost", user="root", password="", database="crime_reporting")
	cursor=con.cursor()
	cursor.execute("select email, password from users")
	for email, pas in cursor:
		if userEmail==email and userPassword==pas:
			tkinter.messagebox.showinfo("Message", "You have successfully Logged in!")
			userLoggedIn=True
			userDashboard()
			userLoginWindow.destroy()
			win.update()
			
		else:
			tkinter.messagebox.showerror("Error!", "Invalid Credentials! Please enter valid email and password to continue")
			print(userEmail+" "+email+" "+userPassword+" "+pas)
	
	con.close()

#For user Login
def userLoginWindow():
	global userLoginWindow
	userLoginWindow=Toplevel(win)
	userLoginWindow.title("User Login")
	userLoginWindow.geometry("300x100")

	Label(userLoginWindow,text="Enter Email:").grid(row=1, column=1, sticky=W)
	Label(userLoginWindow,text="Enter Password:").grid(row=2, column=1, sticky=W)

	global userEmailVar
	userEmailVar=StringVar()
	Entry(userLoginWindow, textvariable=userEmailVar).grid(row=1, column=2)
	global userPasswordVar
	userPasswordVar= StringVar()
	Entry(userLoginWindow, textvariable=userPasswordVar).grid(row=2, column=2)
	
	btnLogin=Button(userLoginWindow, text="Login", command=userLogin).grid(row=3, column=2, sticky=E)

	

def adminLogin():
	adminID=adminIdVar.get()
	adminPassword=adminPasswordVar.get()
	adminLoggedIn=False

	if adminID=="sumant1302" and adminPassword=="123456":
		tkinter.messagebox.showinfo("Message Admin", "You have successfully Logged in as admin")
		adminLoggedIn=True
		adminLoginWindow.destroy()
		adminDashboard()
	else:
		tkinter.messagebox.showerror("Error!", "Please enter valid credentials to continue")


#For admin login
def adminLoginWindow():
	global adminLoginWindow
	adminLoginWindow=Toplevel(win)
	adminLoginWindow.title("Admin Login")
	adminLoginWindow.geometry("300x100")

	Label(adminLoginWindow,text="Enter Admin ID:").grid(row=1, column=1, sticky=W)
	Label(adminLoginWindow,text="Enter Password:").grid(row=2, column=1, sticky=W)

	global adminIdVar
	adminIdVar=StringVar()
	Entry(adminLoginWindow, textvariable=adminIdVar).grid(row=1, column=2)
	global adminPasswordVar
	adminPasswordVar = StringVar()
	Entry(adminLoginWindow, textvariable=adminPasswordVar).grid(row=2, column=2)
	
	btnLogin=Button(adminLoginWindow, text="Login", command=adminLogin).grid(row=3, column=2, sticky=E)

	

def reportCase():
	if userLoggedIn==False:
	# 	tkinter.messagebox.showerror("User Error","Please Register or Login to file a new Case")	
	# else:
		rCWin=Toplevel(win)
		rCWin.title("Report new Case")
		rCWin.geometry("400x200")
		
		#Report case Form
		Label(rCWin,text="Case Title:").grid(row=1, column=1, sticky=W)
		Label(rCWin,text="Description:").grid(row=2, column=1, sticky=W)
		Label(rCWin,text="Case Date:").grid(row=3, column=1, sticky=W)

		global cTitle
		cTitle=StringVar()
		Entry(rCWin, textvariable=cTitle).grid(row=1, column=2)
		global cDes
		cDes = StringVar()
		Entry(rCWin, textvariable=cDes).grid(row=2, column=2)
		global cDate
		cDate= StringVar()
		Entry(rCWin, textvariable=cDate).grid(row=3, column=2)
	
		btnLogin=Button(rCWin, text="File Case", command=fileCase).grid(row=4, column=2, sticky=E)

def fileCase():
	caseTitle=cTitle.get()
	caseDate=cDate.get()
	caseDes=cDes.get()
	userId=""
	userName=""

	if caseTitle=="" or caseDate=="" or caseDes=="":
		tkinter.messagebox.showerror("Message File Case", "All fields are required.")
	else:
		con=mysql.connect(host="localhost", user="root", password="", database="crime_reporting")
		cursor=con.cursor()
		cursor.execute("insert into case_reports values('""','"+userId+"','"+userName+"','"+ caseTitle +"','"+ caseDes +"','""','"+ caseDate +"')")
		cursor.execute("commit")
		# caseID=cursor.lastrowid()
		tkinter.messagebox.showinfo("Case Filed Success", "You have successfully filed new case with case id: Please note it down for future references.")
		con.close()

def userDashboard():
	userScreen=Toplevel(win)
	userScreen.title("User Dashboard")
	userScreen.geometry("600x300")

	Label(userScreen, text="Online Crime reporting System", font=("Helvetica", 20), bg="white", fg="green", justify=LEFT).pack()

	Label(userScreen, text="User Dashboard", font=("Helvetica", 10), bg="white", fg="black", justify=LEFT).pack()

	frameUserDashboard=Frame(userScreen)
	Button(frameUserDashboard, width=8, height=4, text="File New\n Case", fg="white", bg="red", command=reportCase).pack(side=LEFT, padx=20)
	Button(frameUserDashboard, width=8, height=4, text="Check Status\n of previous\n Case", fg="white", bg="red", command=checkCaseStatus).pack(side=LEFT, padx=20)
	Button(frameUserDashboard, width=8, height=4, text="My Account", fg="white", bg="red", command=userAccountDetails).pack(side=LEFT, padx=20)
	Button(frameUserDashboard, width=8, height=4, text="Contact Us", fg="white", bg="red", command=contactUs).pack(side=LEFT, padx=20)
	Button(frameUserDashboard, width=8, height=4, text="Logout", fg="white", bg="red", command=userLogout).pack(side=LEFT, padx=20)
	frameUserDashboard.pack(pady=20)
	

def userAccountDetails():
	userAccScreen=Toplevel(win)
	userAccScreen.title("User Account")
	userAccScreen.geometry("400x300")

def contactUs():
	print("Contact")


def adminDashboard():
	adminScreen=Toplevel(win)
	adminScreen.title("Admin Dashboard")
	adminScreen.geometry("600x300")
	adminScreen["bg"]="white"

	Label(adminScreen, text="Online Crime reporting System", font=("Helvetica", 20), bg="white", fg="green", justify=LEFT).pack()

	Label(adminScreen, text="Admin Dashboard", font=("Helvetica", 10), bg="white", fg="black", justify=LEFT).pack()

	Button(adminScreen, width=10, height=4, text="File New\n Case", fg="white", bg="red", command=reportCase).pack(side=LEFT, padx=20)
	Button(adminScreen, width=10, height=4, text="Check Status\n of Case", fg="white", bg="red", command=checkCaseStatus).pack(side=LEFT, padx=20)
	Button(adminScreen, width=10, height=4, text="Update Status\n of Case", fg="white", bg="red", command=updateCaseStatus).pack(side=LEFT, padx=20)
	
	Button(adminScreen, width=10, height=4, text="Messages", fg="white", bg="red", command=adminMessages).pack(side=LEFT, padx=20)
	Button(adminScreen, width=10, height=4, text="Logout", fg="white", bg="red", command=userLogout).pack(side=LEFT, padx=20)

def adminMessages():
	print("admin Messages")

def updateCaseStatus():
	print("Update Case status")


def userLogout():
	win.destroy()
	#Make a main function to run
	main_screen()
	userLoggedIn==False

def checkStatus():
        print("checkStatus")
		
def checkCaseStatus():
	cStatusWin=Toplevel(win)
	cStatusWin.title("Check Case Status")
	cStatusWin.geometry("400x250")
	Label(cStatusWin, text="Online Crime reporting System", font=("Helvetica", 20), bg="white", fg="green").grid(row=1, column=1, columnspan=3,)

	Label(cStatusWin, text="Check Case Status", font=("Helvetica", 10), bg="white", fg="black", justify=LEFT).grid(row=2, column=2)
	Label(cStatusWin,text="EnterCase ID to check case status").grid(row=4,column=2)

	Label(cStatusWin,text="Case ID:").grid(row=6,column=1, pady=20)
	cTitle=StringVar()
	Entry(cStatusWin, textvariable=cTitle).grid(row=6,column=2, pady=20)
	
	btnCheckStatus=Button(cStatusWin, text="Check Status",bg="green", command=checkStatus).grid(row=8, column=2, pady=10, sticky=E)

def main_screen():
	global win
	win=Tk()
	win.title("Online Crime Reporting System")
	win.geometry("600x400")
	

	
	# Creating a menubar
	menubar=Menu(win)
	win.config(menu=menubar)

	#Adding commands to button
	global homeMenu
	homeMenu=menubar.add_command(label="Home")
	aboutMenu=menubar.add_command(label="About", command=about)

	if userLoggedIn==False:
		loginMenu=Menu(menubar, tearoff=0)
		menubar.add_cascade(label="Login", menu=loginMenu)
		loginMenu.add_command(label="Admin Login", command=adminLoginWindow)
		loginMenu.add_command(label="User Login", command=userLoginWindow)

		menubar.add_command(label="Register", command=register)

	#creating an exit menu
	exitMenu=Menu(menubar, tearoff=0)
	menubar.add_cascade(label="Exit", menu=exitMenu)
	exitMenu.add_command(label="Quit", command=win.quit)

	#Add a canvas 
	canvas1=Canvas(win, width=600, height=100, bg="red")
	Label(canvas1, text="Online Crime Reporting System", font=("Calibri", 30),fg="white", bg="red").pack()
	canvas1.pack(pady=30)

	global canvasHome
	canvasHome=Canvas(win, width=600, height=200, bg="white")

	home()

	win.mainloop()

main_screen()