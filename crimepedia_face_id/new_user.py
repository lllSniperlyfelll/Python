import cv2
import os
import tkinter as tkinter
from tkinter import messagebox

import time

class NEW_FACE_CAPTURE:

	def getusername(self):
		line=" "
		with open("temp_usr.txt","r") as f:
			for line in f:
				line=line.replace("\n",'')
		file =  open("temp_usr.txt","w")
		file.write("")
		print("userame got -> ",line)
		return line		

	def capture_face(self):
		root =tkinter.Tk()
		root.withdraw()
		messagebox.showinfo("Authentication"," Look at the camera ")
		face_cascades=cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml') # classifier
		cap=cv2.VideoCapture(0)
		i=1
		username=self.getusername()
		path="images/"+username	
		if not os.path.exists("/images/"+username):
			print("dir present -> ",path)
			os.mkdir(path)
		while True:
			ret , frame = cap.read()
			#grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # coz above usd classifer needs grey scale frames
			faces = face_cascades.detectMultiScale(frame,scaleFactor=1.5,minNeighbors=5)
			for (x ,y ,w ,h) in faces:

				cv2.putText(frame," ",(x,y) ,cv2.FONT_HERSHEY_SIMPLEX ,1 ,(255,255,255),3,cv2.LINE_AA)
				#if i>=1:	

				img_item=path+"/"+username+str(i)+".png"
				i+=1
				cv2.imwrite(img_item ,frame[y:y+h,x:x+w])
				rect_color=(255,0,0)
				stroke=4
				width=(x+w)
				height=(y+h)
				cv2.rectangle(frame,(x,y),(width+5,height+5),rect_color,stroke)
			cv2.imshow("test",frame)
			if cv2.waitKey(27) & 0XFF == ord('q') or i>=36:
				break
		cap.release()
		cv2.destroyAllWindows()
		messagebox.showinfo("Done!!","Try loggin in now")
































# NFC=NEW_FACE_CAPTURE()

# NFC.capture_face()