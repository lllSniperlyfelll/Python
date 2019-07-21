from tkinter import *
import tkinter.messagebox
import tkinter.scrolledtext as tkst
import random
import string
import os
from pathlib import Path
import datetime
from new_user import *
from face_auth import *

def is_criminal(username):
	useracop=''
	for i in username:
		if(i!=" "):
			useracop+=i
		else:
			break
			
	id=[]
	with open("Criminal_rec.txt","r") as f:
		for line in f:
			line=line.replace("\n",'')
			id.append(line)
	print("is_criminal  ->  ",useracop)
	
	#fe=open("Criminal_rec.txt","r")
	#str=fe.read()
	#bgcolor="#69F0AE"
	for i in id:
		ff=open("color.txt","w")
		if(i==useracop):
			bgcolor="#FF1744"
			print("Color set to red ")
			ff.truncate()
			ff.write(bgcolor)
			ff.close()
			break
		elif(i!=useracop):
			print("Color set to green ")
			ff.truncate()
			bgcolor="#69F0AE"
			ff.write(bgcolor)
			ff.close()
	print("criminals   ->  ",id)
	#ff.close()
	f.close()
	

def check_theme():
	file=open("color.txt","r")
	str=file.read()
	file.close()
	return str
	
	
def edit_logs(logss1):
	logss=''
	for i in logss1:
		if(i!=" "):
			logss+=i
		elif(i==" "):
			break
	now=datetime.datetime.now()
	log_file=open("logs.txt","a")
	log_str=now.strftime("Date -> %Y-%m-%d      Time -> %H : %M")
	log_str=logss+"      "+log_str+"\n"
	log_file.write(log_str)
	log_file.close()
	
def Logs():
	root=Tk()
	root.configure(bg=check_theme())
	width=900
	height=600
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	x = (screen_width / 2) - (width / 2)
	y = (screen_height / 2) - (height / 2)
	root.geometry('%dx%d+%d+%d' % (width, height, x, y))
	root.geometry("800x540")
	filelog=open("logs.txt","r")
	str=filelog.read()
	txt = tkst.ScrolledText(root,width=150,height=37, undo=True,state=NORMAL,bg="white",fg="black")
	txt['font'] = ('Times new roman', '12')
	txt.yview(END)
	txt.insert(END,str)
	txt.place(x=0,y=0)
	filelog.close()

	
def encryption(stringg):
	b=0
	string1=''
	for i in stringg:
		b=ord(i)
		b+=7
		i=chr(b)
		string1+=i
	string.ascii_letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01'
	stack=[]
	str=''
	temp=[]
	encrpyted_stringc=''
	for i in string1:
		stack.append(i)
	j=len(stack)-1
	while(j>=0):
		str=str+stack[j]
		j-=1
	print("stack ->  ",str)
	for u in str:
		temp.append(u)
	for j in range(0,len(temp)*2):
		if(j%2==0):
			temp.insert(j,(random.choice(string.ascii_letters)))
			
	for e in range(0,len(temp)):
		encrpyted_stringc+=temp[e]
	return encrpyted_stringc




def de_encryption(encrpyted_string):
	tempr=[]
	retrived=''
	strr=''
	a=0
	for l in encrpyted_string:
		tempr.append(l)

	b=len(tempr)-1
	while(b>=0):
		if(b%2!=0):
			retrived+=tempr[b]
		b-=1
		
	for i in retrived:
		a=ord(i)
		a-=7
		i=chr(a)
		strr+=i
	
	print("De-enrypted string ->  ",strr)
	return strr




def newaccount():
	root=Tk()
	root.configure(bg="#536DFE")
	width=900
	height=600
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	x = (screen_width / 2) - (width / 2)
	y = (screen_height / 2) - (height / 2)
	root.geometry('%dx%d+%d+%d' % (width, height, x, y))
	root.geometry("800x540")
	root.resizable(0,0)
	def addnewinfo():
		flag=0
		usernamestr=username.get()
		#passwordstr=password.get()
		answer=tkinter.messagebox.askquestion("Sure?","Continue to face id -> ")
		if (answer=="yes"):
			id=[]
			with open("admin.txt","r") as f:
				for line in f:
					line=line.replace("\n",'')
					id.append((line))
			length1=len(id)
			print(id)
			
			for i in range (0,length1) :
				if usernamestr==id[i]:
					flag=1
					break
			if(flag==1):
				tkinter.messagebox.showinfo("ERROR!!!", "USERNAME ALREADY EXISTS!!")
				root.destroy()
			else:
				
				print(usernamestr)
				file=open("admin.txt","a")
				#encrpyted_string=encryption(usernamestr)
				#encrpyted_string+='\n'
				file.write(usernamestr+'\n')
				file.close()
				file=open("temp_usr.txt","w")
				file.write(usernamestr)
				file.close()
	
				NFC=NEW_FACE_CAPTURE()
				NFC.capture_face()
				tkinter.messagebox.showinfo("Done!!", "Account added!!")
				root.destroy()

	buttonok=Button(root,text="Face id",height=1,width=10,command=addnewinfo,bg="#3D5AFE",fg="white",borderwidth=0)
	username=Entry(root,width=30+5,borderwidth=0,font=("Times new Roman",11),fg="#3D5AFE")
	#password=Entry(root,width=30+5,show="*",font=("Times new Roman",11),borderwidth=0,fg="#3D5AFE")
	userlabel=Label(root,text="New Username:-",fg="white",bg="#536DFE",font=("Times new Roman",11),justify="center")
	#passwordlabel=Label(root,text="New Password:-",fg="white",bg="#536DFE",font=("Times new Roman",11),justify="center")
	username.place(x=320,y=180)
	userlabel.place(x=208,y=178)
	#password.place(x=320,y=240)
	#passwordlabel.place(x=208,y=240)
	buttonok.place(x=380,y=290)
	root.mainloop()



def bootwindow():
	root=Tk()
	root.configure(bg="#536DFE")
	width=900
	height=600
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	x = (screen_width / 2) - (width / 2)
	y = (screen_height / 2) - (height / 2)
	root.geometry('%dx%d+%d+%d' % (width, height, x, y))
	root.geometry("800x540")
	root.resizable(0,0)
	root.title("                                                                                                              WELCOME TO CRIMEPEDIA")
	def checker():
		id=[]
		FA=FACE_AUTH()
		with open("admin.txt","r") as f:
			for line in f:
				line=line.replace("\n",'')
				id.append(line)
		usernamestr=username.get()
		print(id)
		print(usernamestr)
		length1=len(id)
		flaggg=1

		try:
			for i in range (0,length1) :
				destr=(id[i])
				if(i==0):
					if usernamestr==(id[i]):
						name_file=open("current_user.txt","w")
						name_file.write(usernamestr)
						name_file.close()
						print("Written usernamestr in current_user.txt ...")
						#####needs to match face now###########
						auth_status=FA.face_authenticate(usernamestr)
						print(auth_status)
						if(auth_status == True):
							flaggg=0
						else:
							flaggg=1
						######################################
						is_criminal(usernamestr)
						edit_logs(destr)
						root.destroy()
						adminwindow()
				elif usernamestr==(id[i]):
					name_file=open("current_user.txt","w")
					name_file.write(usernamestr)
					name_file.close()
					print("Written usernamestr in current_user.txt ...")
					#needs to match face now
					#####needs to match face now###########
					auth_status=FA.face_authenticate(usernamestr)
					print(auth_status)
					if(auth_status == True):
						flaggg=0
					else:
						flaggg=1
					######################################
					is_criminal(usernamestr)
					#flaggg=0
					edit_logs(destr)
					root.destroy()
					userwindow()
			if(flaggg==1):
				errorlabel=Label(root,text="Invalid Username or Face id error",fg="white",bg="crimson",font=("Times new Roman",11),justify="center")
				errorlabel.place(x=330,y=500)
		except:
			print("")
	buttonok=Button(root,text="Done",height=1,width=10,command=checker,bg="#3D5AFE",fg="white",borderwidth=0)
	newacc=Button(root,text="CREATE NEW ACCOUNT",height=1,width=len("		CREATE NEW ACCOUNT		"),command=newaccount,bg="#3D5AFE",fg="white",borderwidth=0,font=("Times new Roman",11))
	username=Entry(root,width=40-5,borderwidth=0,font=("Times new Roman",11),fg="#3D5AFE")
	#password=Entry(root,width=40-5,show="*",font=("Times new Roman",11),borderwidth=0,fg="#3D5AFE")
	userlabel=Label(root,text="Username:-",fg="white",bg="#536DFE",font=("Times new Roman",11),justify="center")
	OR=Label(root,text="OR",fg="white",bg="#536DFE",font=("Times new Roman",13),justify="center")
	#passwordlabel=Label(root,text="Password:-",fg="white",bg="#536DFE",font=("Times new Roman",11),justify="center")
	username.place(x=320,y=180)
	userlabel.place(x=238,y=178)
	#password.place(x=320,y=240)
	#passwordlabel.place(x=238,y=240)
	buttonok.place(x=380,y=290)
	OR.place(x=400,y=350)
	newacc.place(x=333,y=400)
	root.mainloop()




#""""ADMIN WINDOWS WITH EXTRA PERMISSIONS
def adminwindow():
	root=Tk()
	root.configure(bg=check_theme())
	width = 900
	height = 600
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	x = (screen_width / 2) - (width / 2)
	y = (screen_height / 2) - (height / 2)
	root.geometry('%dx%d+%d+%d' % (width, height, x, y))
	root.geometry("800x540")
	root.resizable(0,0)
	file10=open("home.txt",'r')
	strhome=file10.read();
	infolabel=Label(root,text=strhome,font=("Times New Roman",12),bg=check_theme(),fg="black")
	infolabel.place(x=20,y=150)
	def recurse():
		root.destroy()
		adminwindow()
	name_file=open("current_user.txt","r")
	name=name_file.read()
	name_file.close()
	name_file=open("current_user.txt","w")
	name_file.write("")
	name_file.close()
	welcome=Label(root,text="WELCOME "+name,font=("Elephant",15),bg=check_theme(),fg="black",borderwidth=0)
	toolbar=Frame(root,bg=check_theme())
	home=Button(toolbar,text="Home",fg="black",width=5,bg=check_theme(),borderwidth=0,font=("Times new Roman Bold",15),command=recurse)
	strtest="Crimes and Sections"
	logs=Button(toolbar,text="Logs",fg="black",width=10,bg=check_theme(),borderwidth=0,font=(("Times new Roman Bold",15)),command=Logs)
	a=len(strtest)
	#settings=Button(toolbar,text="Settings",fg="black",width=a,borderwidth=0,bg=check_theme(),font=("Times new Roman Bold",15),command=crimefn)
	crimes=Button(toolbar,text="Crimes and Sections",fg="black",width=a,borderwidth=0,bg=check_theme(),font=("Times new Roman Bold",15),command=crimefn)
	info=Button(toolbar,text="Information",width=10,bg=check_theme(),fg="black",borderwidth=0,font=("Times new Roman Bold",15),command=infofn)
	About=Button(toolbar,text="About",command=(about),width=5,bg=check_theme(),fg="black",borderwidth=0,font=(("Times new Roman Bold",15)))
	strtest = "Edit Section Files"
	a = len(strtest)
	Editt=Button(toolbar,text="Edit Section Files",command=readsections,width=a,bg=check_theme(),fg="black",borderwidth=0,font=("Times new Roman Bold",15))
	toolbar.pack(side=TOP)
	home.pack(side=LEFT,pady=20)
	crimes.pack(side=LEFT,pady=20)
	info.pack(side=LEFT,pady=20)
	Editt.pack(side=LEFT,pady=20)
	About.pack(side=LEFT, pady=20)
	welcome.place(x=300,y=80)
	logs.pack(side=LEFT ,pady=20)
	#settings.pack(x=900,y=600)
	root.mainloop()




#USER WINDOW WITH LESS PERMISSIONS
def userwindow():
	root2=Tk()
	root2.configure(bg=check_theme())
	width = 900
	height = 600
	screen_width = root2.winfo_screenwidth()
	screen_height = root2.winfo_screenheight()
	x = (screen_width / 2) - (width / 2)
	y = (screen_height / 2) - (height / 2)
	root2.geometry('%dx%d+%d+%d' % (width, height, x, y))
	root2.geometry("800x540")
	root2.resizable(0,0)
	file10=open("home.txt",'r')
	strhome=file10.read()
	infolabel=Label(root2,text=strhome,font=("Times New Roman",12),bg=check_theme(),fg="black")
	infolabel.place(x=20,y=150)
	def recurse():
		root2.destroy()
		userwindow()
	name_file=open("current_user.txt","r")
	name=name_file.read()
	name_file.close()
	name_file=open("current_user.txt","w")
	name_file.write("")
	name_file.close()
	welcome = Label(root2, text="WELCOME "+name, font=("Elephant", 15), bg=check_theme(), fg="black",borderwidth=0)
	toolbar=Frame(root2,bg=check_theme())
	home=Button(toolbar,text="Home",fg="black",width=10,bg=check_theme(),borderwidth=0,font=("Times new Roman Bold",15),command=recurse)
	strtest="Crimes and Sections"
	a=len(strtest)
	crimes=Button(toolbar,text="Crimes and Sections",fg="black",width=a,borderwidth=0,bg=check_theme(),font=("Times new Roman Bold",15),command=crimefn)
	info=Button(toolbar,text="Information",width=10,bg=check_theme(),fg="black",borderwidth=0,font=("Times new Roman Bold",15),command=infofn)
	About=Button(toolbar,text="About",width=10,command=(about),bg=check_theme(),fg="black",borderwidth=0,font=("Times new Roman Bold",15))
	toolbar.pack(side=TOP)
	home.pack(side=LEFT, padx=20, pady=20)
	crimes.pack(side=LEFT, padx=20, pady=20)
	info.pack(side=LEFT, padx=20, pady=20)
	About.pack(side=LEFT, padx=20, pady=20)
	welcome.place(x=300, y=80)
	root2.mainloop()




#"""""scrollbar ,file edit function fixed
#"""""""""""""""""""''restore button remaining
def readsections():
	def readsectionfiles():
		root=Tk()
		root.configure(bg=check_theme())
		screen_width = root.winfo_screenwidth()
		screen_height = root.winfo_screenheight()
		root.geometry("%dx%d" % (screen_width, screen_height))
		#root.geometry("2000x1000")
		file = open("sections.txt", 'r')
		str=file.read()
		def ask():
			answer=tkinter.messagebox.askquestion("Continue?","Do you want to change file permanantly ?")
			if (answer=="yes"):
				tkinter.messagebox.showinfo("Done!!", "File changed !!")
				saveit()
			else:
				root.destroy()
		def askcancel():
			answer1 = tkinter.messagebox.askquestion("Continue?", "Do you want to Cancel editing and quit without saving?")
			if(answer1=="yes"):
				root.destroy()
		def saveit():
			file1=open("sections.txt",'w')
			string1=txt.get('0.0',END)
			print(string1)
			file1.write(string1)
			file1.close()
			root.destroy()
		tolbar=Frame(root,bg=check_theme())
		save=Button(tolbar,text="Save",fg="black",bg=check_theme(),command=ask,borderwidth=0,width=len("savesavesavesave"),font=("Times new roman",15))
		cancel = Button(tolbar, text="Cancel", fg="black", bg=check_theme(), command=askcancel, borderwidth=0,width=len("savesavesavesave"), font=("Times new roman", 15))
		txt = tkst.ScrolledText(root,width=150,height=37, undo=True,state=NORMAL,bg="#E0E0E0",fg="black")
		txt['font'] = ('Times new roman', '12')
		txt.yview(END)
		txt.insert(END,str)
		txt.place(x=0,y=0)
		tolbar.pack(side=RIGHT)
		save.pack(side=TOP,pady=10)
		cancel.pack(side=TOP,pady=10)
		file.close()
		root.mainloop()

	root=Tk()
	root.configure(bg=check_theme())
	width = 900
	height = 600
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	x = (screen_width / 2) - (width / 2)
	y = (screen_height / 2) - (height / 2)
	root.geometry('%dx%d+%d+%d' % (width, height, x, y))
	root.geometry("800x540")
	root.resizable(0,0)
	root.title("                                                                                                      PLEASE RECONFIRM YOUR DETAILS TO CONTINUE")
	def checker():
		id=[]
		with open("admin.txt","r") as f:
			for line in f:
				line=line.replace("\n",'')
				id.append(line)
		usernamestr=username.get()
		passwordstr=password.get()
		print(id)
		usernamestr=usernamestr+" "+passwordstr
		print(usernamestr)
		if usernamestr==de_encryption(id[0]):
			root.destroy()
			readsectionfiles()
		else:
			tkinter.messagebox.showinfo("Error", "Username or Password Not Valid !!")
			root.destroy()
			print("ERROR")
		'''print(infocpy)
		usernamestr=usernamestr+" "+passwordstr
		print(usernamestr)
		if(usernamestr==infocpy):
			root.destroy()
			readsectionfiles()
		else:
			tkinter.messagebox.showinfo("Error", "Username or Password Not Valid !!")
			root.destroy()
			print("Error")'''
	buttonok=Button(root,text="Done",height=1,width=10,command=checker,bg=check_theme(),fg="black",borderwidth=0)
	username=Entry(root,width=30+5,borderwidth=0,font=("Times new Roman",11))
	textlabel=Label(root,text="CONFIRM YOUR USERNAME AND PASSWORD",font=("Times New Roman Bold",12),fg="black",bg=check_theme())
	password=Entry(root,width=30+5,show="*",font=("Times new Roman",11),borderwidth=0)
	userlabel=Label(root,text="Username:-",fg="black",bg=check_theme(),font=("Times new Roman",11),justify="center")
	passwordlabel=Label(root,text="Password:-",fg="black",bg=check_theme(),font=("Times new Roman",11),justify="center")
	username.place(x=320,y=180)
	userlabel.place(x=238,y=178)
	password.place(x=320,y=240)
	passwordlabel.place(x=238,y=240)
	buttonok.place(x=380,y=290)
	textlabel.place(x=250,y=100)
	root.mainloop()




def crimefn():
	root=Tk()
	root.geometry("1100x650")
	root.configure(bg=check_theme())
	root.resizable(0,0)
	root.title("Crimes and Sections")
	toolbar=Frame(root,bg=check_theme())
	toolbar.pack(side=TOP)
	home=Button(toolbar,text="Home",fg="black",width=5,bg=check_theme(),borderwidth=0,font=("Times new Roman Bold",15),command=root.destroy)
	home.pack(side=LEFT, padx=20, pady=20)
	def checkstate(n):
		ch1.after(2000, ch1.deselect)
		ch2.after(2000, ch2.deselect)
		ch3.after(2000, ch3.deselect)
		ch4.after(2000, ch4.deselect)
		ch5.after(2000, ch5.deselect)
		ch6.after(2000, ch6.deselect)
		ch7.after(2000, ch7.deselect)
		ch8.after(2000, ch8.deselect)
		ch9.after(2000, ch9.deselect)
		ch10.after(2000, ch10.deselect)
		ch11.after(2000, ch11.deselect)
		ch12.after(2000, ch12.deselect)
		ch13.after(2000, ch13.deselect)
		ch14.after(2000, ch14.deselect)
		ch15.after(2000, ch15.deselect)
		ch16.after(2000, ch16.deselect)
		ch17.after(2000, ch17.deselect)
		ch18.after(2000, ch18.deselect)
		ch19.after(2000, ch19.deselect)
		ch20.after(2000, ch20.deselect)
		ch21.after(2000, ch21.deselect)
		ch22.after(2000, ch22.deselect)
		ch23.after(2000, ch23.deselect)
		ch24.after(2000, ch24.deselect)
		ch25.after(2000, ch25.deselect)
		ch26.after(2000, ch26.deselect)
		ch27.after(2000, ch27.deselect)
		ch28.after(2000, ch28.deselect)
		ch29.after(2000, ch29.deselect)
		ch30.after(2000, ch30.deselect)
		
		if(n==1):
			path="affray.txt"
			print("1")
		elif(n==2):
			path="bribery.txt"
		elif(n==3):
			path = "cheating.txt"
			print("3")
		elif(n==4):
			path="criminal intimidation.txt"
			print("4")
		elif(n==5):
			path = "dacoity.txt"
			print("5")
		elif(n==6):
			path = "defamation.txt"
			print("6")
		elif(n==7):
			path = "extortion.txt"
			print("7")
		elif(n==8):
			path = "forgery.txt"
			print("8")
		elif(n==9):
			path = "gfevi.txt"
			print("9")
		elif (n == 10):
			path = "kidnapping.txt"
			print("10")
		elif(n==11):
			path = "mischief.txt"
			print("11")
		elif(n==12):
			path = "murder.txt"
			print("12")
		elif(n==13):
			path = "rioting.txt"
			print("13")
		elif(n==14):
			path = "robbery.txt"
			print("14")
		elif(n==15):
			path = "theft.txt"
			print("15")
		elif(n==16):
			path = "uiae.txt"
			print("16")
		elif(n==17):
			path = "Unassem.txt"
			print("17")
		elif(n==18):
			path = "gh.txt"
			print("18")
		elif(n==19):
			path = "hurt.txt"
			print("19")
		elif(n==20):
			path = "wc.txt"
			print("20")
		elif(n==21):
			path = "wr.txt"
			print("21")
		elif(n==22):
			path = "extortion.txt"
			print("22")
		elif(n==23):
			print("23")
		elif(n==24):
			print("24")
		elif(n==25):
			print("25")
		elif(n==26):
			print("26")
		elif(n==27):
			print("27")
		elif(n==28):
			print("28")
		elif(n==29):
			print("29")
		elif(n==230):
			print("30")
		filec = open(path,'r')
		
		crimestring = filec.read()
		root1=Tk()
		root1.title("Crimes and Sections")
		root1.config(bg=check_theme())
		width = 900
		height = 600
		screen_width = root.winfo_screenwidth()
		screen_height = root.winfo_screenheight()
		x = (screen_width / 2) - (width / 2)
		y = (screen_height / 2) - (height / 2)
		root1.geometry('%dx%d+%d+%d' % (width, height, x, y))
		root1.geometry("1080x540")
		root1.resizable(0,0)
		crimelabel = Label(root1, text=crimestring,fg="black",bg=check_theme(),font=("Times New Roman justify",12))
		crimelabel.pack(fill='both')
		root1.mainloop()
	var1=IntVar()
	var2=IntVar()
	var3 = IntVar()
	var4 = IntVar()
	var5 = IntVar()
	var6 = IntVar()
	var7 = IntVar()
	var8 = IntVar()
	var9 = IntVar()
	var10 = IntVar()
	var11 = IntVar()
	var12 = IntVar()
	var13= IntVar()
	var14 = IntVar()
	var15 = IntVar()
	var16 = IntVar()
	var17 = IntVar()
	var18 = IntVar()
	var19 = IntVar()
	var20 = IntVar()
	var21 = IntVar()
	var22 = IntVar()
	var23 = IntVar()
	var24 = IntVar()
	var25 = IntVar()
	var26 = IntVar()
	var27 = IntVar()
	var28 = IntVar()
	var29 = IntVar()
	var30 = IntVar()
	ch1 = Checkbutton(root, bg=check_theme(),text="Affray",fg="black", command=lambda:checkstate(1), variable=var1)
	ch2 = Checkbutton(root, bg=check_theme(),text="Bribery",fg="black", command=lambda :checkstate(2), variable=var2)
	ch3 = Checkbutton(root, bg=check_theme(),text="Cheating",fg="black", command=lambda :checkstate(3), variable=var3)
	ch4 = Checkbutton(root, bg=check_theme(),text="Criminal Intimidation",fg="black", command=lambda :checkstate(4), variable=var4)
	ch5 = Checkbutton(root, bg=check_theme(),text="Dacoity",fg="black", command=lambda :checkstate(5), variable=var5)
	ch6 = Checkbutton(root, bg=check_theme(),text="Defamation",fg="black", command=lambda :checkstate(6), variable=var6)
	ch7 = Checkbutton(root, bg=check_theme(),text="Extortion",fg="black", command=lambda :checkstate(7), variable=var7)
	ch8 = Checkbutton(root, bg=check_theme(),text="Forgery",fg="black", command=lambda :checkstate(8), variable=var8)
	ch9 = Checkbutton(root, bg=check_theme(),text="Giving False Evdience",fg="black", command=lambda :checkstate(9), variable=var9)
	ch10 = Checkbutton(root, bg=check_theme(),text="Kidnapping",fg="black", command=lambda :checkstate(10), variable=var10)
	ch11= Checkbutton(root, bg=check_theme(),text="Mischief", fg="black",command=lambda :checkstate(11), variable=var11)
	ch12 = Checkbutton(root, bg=check_theme(),text="Murder", fg="black",command=lambda :checkstate(12), variable=var12)
	ch13 = Checkbutton(root, bg=check_theme(),text="Rioting", fg="black",command=lambda :checkstate(13), variable=var13)
	ch14 = Checkbutton(root, bg=check_theme(),text="Robbery", fg="black",command=lambda :checkstate(14), variable=var14)
	ch15 = Checkbutton(root, bg=check_theme(),text="Theft", fg="black",command=lambda :checkstate(15), variable=var15)
	ch16 = Checkbutton(root, bg=check_theme(),text="Undue Influence At Elections", fg="black",command=lambda :checkstate(16), variable=var16)
	ch17 = Checkbutton(root, bg=check_theme(),text="Unlawfull Assembly Member", fg="black",command=lambda :checkstate(17), variable=var17)
	ch18 = Checkbutton(root, bg=check_theme(),text="Causing Grievous Hurt", fg="black",command=lambda :checkstate(18), variable=var18)
	ch19 = Checkbutton(root, bg=check_theme(),text="Causing Hurt", fg="black",command=lambda :checkstate(19), variable=var19)
	ch20 = Checkbutton(root, bg=check_theme(),text="Wrong Confinement", fg="black",command=lambda :checkstate(20), variable=var20)
	ch21 = Checkbutton(root, bg=check_theme(),text="Wrong Restrain", fg="black",command=lambda: checkstate(21), variable=var21)
	ch22 = Checkbutton(root, bg=check_theme(),text="crime22", fg="black",command=lambda: checkstate(22), variable=var22)
	ch23 = Checkbutton(root, bg=check_theme(),text="crime23", fg="black",command=lambda: checkstate(23), variable=var23)
	ch24 = Checkbutton(root, bg=check_theme(),text="crime24", fg="black",command=lambda: checkstate(24), variable=var24)
	ch25 = Checkbutton(root, bg=check_theme(),text="crime25", fg="black",command=lambda: checkstate(25), variable=var25)
	ch26 = Checkbutton(root, bg=check_theme(),text="crime26", fg="black",command=lambda: checkstate(26), variable=var26)
	ch27 = Checkbutton(root, bg=check_theme(),text="crime27", fg="black",command=lambda: checkstate(27), variable=var27)
	ch28 = Checkbutton(root, bg=check_theme(),text="crime28", fg="black",command=lambda: checkstate(28), variable=var28)
	ch29 = Checkbutton(root, bg=check_theme(),text="crime29", fg="black",command=lambda: checkstate(29), variable=var29)
	ch30 = Checkbutton(root, bg=check_theme(),text="crime30", fg="black",command=lambda: checkstate(30), variable=var30)
	tuto=Label(root,fg="black",bg=check_theme(),text="Select the Crime Checkbox to get the Section of related to Indian Penal Code and the Punishment related to Crime",font=("Times New Roman",15))
	tuto.pack(side=TOP,pady=20,fill=X)
	ch1.place(x=100,y=200)
	ch2.place(x=200,y=200)
	ch3.place(x=300, y=200)
	ch4.place(x=400, y=200)
	ch5.place(x=550, y=200)
	ch6.place(x=630, y=200)
	ch7.place(x=730, y=200)
	ch8.place(x=820, y=200)
	ch9.place(x=900, y=200)
	ch10.place(x=100, y=300)
	ch11.place(x=200, y=300)
	ch12.place(x=300, y=300)
	ch13.place(x=400, y=300)
	ch14.place(x=500, y=300)
	ch15.place(x=600, y=300)
	ch16.place(x=680, y=300)
	ch17.place(x=867, y=300)
	ch18.place(x=100, y=400)
	ch19.place(x=250, y=400)
	ch20.place(x=360, y=400)
	ch21.place(x=500, y=400)
	root.mainloop()




def about():
	root1=Tk()
	root1.configure(bg=check_theme())
	width = 900
	height = 600
	screen_width = root1.winfo_screenwidth()
	screen_height = root1.winfo_screenheight()
	x = (screen_width / 2) - (width / 2)
	y = (screen_height / 2) - (height / 2)
	root1.geometry('%dx%d+%d+%d' % (width, height, x, y))
	root1.geometry("800x540")
	root1.resizable(0,0)
	file=open("about.txt",'r')
	string=file.read()
	toolbar=Frame(root1,bg=check_theme())
	toolbar.pack(side=TOP)
	home=Button(toolbar,text="Home",fg="black",width=5,bg=check_theme(),borderwidth=0,font=("Times new Roman Bold",15),command=root1.destroy)
	home.pack(side=LEFT, padx=20, pady=20)
	labelinfo=Label(root1,text=string,bg=check_theme(),fg="black",font=("Times New Roman",20))
	labelinfo.place(x=200,y=100)
	root1.mainloop()




def infofn():
	root=Tk()
	root.configure(bg=check_theme())
	width = 900
	height = 600
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	x = (screen_width / 2) - (width / 2)
	y = (screen_height / 2) - (height / 2)
	root.geometry('%dx%d+%d+%d' % (width, height, x, y))
	root.geometry("800x540")
	root.resizable(0,0)
	#root.geometry("2000x1000")
	file1=open("Penal Code.txt",'r')
	str=file1.read()
	file1.close()
	toolbar=Frame(root,bg=check_theme())
	toolbar.pack(side=TOP)
	home=Button(toolbar,text="Home",fg="black",width=5,bg=check_theme(),borderwidth=0,font=("Times new Roman Bold",15),command=root.destroy)
	home.pack(side=LEFT, padx=20, pady=20)
	court = Label(root,text="INDIAN PENAL CODE",font=("Papyrus Bold",20),bg=check_theme(),fg="black")
	infolabel=Label(root,font=("Times Roman Bold Underline",10),bg=check_theme(),fg="black")
	infolabel.config(text=str)
	court.pack(side=TOP, fill=X, pady=50)
	infolabel.pack(side=TOP,fill=X,pady=10)
	root.mainloop()





def bootwin():
	root=Tk()
	width = 900
	height = 600
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	x = (screen_width / 2) - (width / 2)
	y = (screen_height / 2) - (height / 2)
	root.geometry('%dx%d+%d+%d' % (width, height, x, y))
	root.geometry("800x540")
	root.configure(bg="black")
	root.resizable(0, 0)
	root.title("                                                                                                              WELCOME TO CRIMEPEDIA")
	def start():
		root.destroy()
		check_data_file()
	infol=Label(root,text="WELCOME TO ",font=("Freestyle Script",35),bg="black",fg="white")
	c = Label(root, text="C", font=("SHOWCARD GOTHIC", 70), bg="black", fg="#9C27B0")
	r = Label(root, text="R", font=("SHOWCARD GOTHIC", 50), bg="black", fg="#00B8D4")
	i = Label(root, text="I", font=("SHOWCARD GOTHIC", 100), bg="black", fg="blue")
	m = Label(root, text="M", font=("SHOWCARD GOTHIC", 50), bg="black", fg="red")
	e = Label(root, text="e", font=("SHOWCARD GOTHIC", 50), bg="black", fg="yellow")
	p = Label(root, text="P", font=("SHOWCARD GOTHIC", 110), bg="black", fg="#FF3D00")
	ee = Label(root, text="E", font=("SHOWCARD GOTHIC", 50), bg="black", fg="#2196F3")
	d = Label(root, text="D", font=("SHOWCARD GOTHIC", 50), bg="black", fg="#E91E63")
	ii = Label(root, text="i", font=("SHOWCARD GOTHIC", 50), bg="black", fg="#9C27B0")
	aa = Label(root, text="A", font=("SHOWCARD GOTHIC", 50), bg="black", fg="#F44336")
	infol.pack(side=TOP,pady=60)
	c.place(y=178+20,x=160-30)
	r.place(y=200+20, x=217-30)
	i.place(y=140+20, x=270-30)
	m.place(y=200+20, x=330-30)
	e.place(y=200+20, x=399-30)
	p.place(y=120+20, x=440-30)
	ee.place(y=200+20, x=540-30)
	d.place(y=200+20, x=590-30)
	ii.place(y=200+20, x=640-30)
	aa.place(y=200+20, x=680-30)
	root.after(4000,lambda :start())
	root.mainloop()






def check_data_file():
	dir_path=os.getcwd()
	file_path=dir_path+"/admin.txt"
	file=Path(file_path)
	status=False
	if file.is_file():
		status=True
	else:
		status=False

	if(status==True):
		bootwindow()
	else:
		tkinter.messagebox.showinfo("Error!!", "Some Files Are Missing!!")




























#check_data_file()
#bootwindow()
bootwin()
#infofn()
#readsections()
#about()
#adminwindow()
#userwindow()
#checker()
#crimefn()