import numpy as np
import cv2
import os
from PIL import Image
import dlib
import click 
import face_recognition
import tkinter as tkinter
from tkinter import messagebox


################ No Face In View Is An Issue


class FACE_AUTH:

	def face_authenticate(self,username):
		print("face_authenticate got username as %s"%(username))
		results=False
		face_cascades=cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml') # classifier
		cap=cv2.VideoCapture(0)
		i=1
		user_image=face_recognition.load_image_file("images/"+username+"/"+username+"10.png")
		
		user_image1=face_recognition.load_image_file("images/"+username+"/"+username+"11.png")
		user_image2=face_recognition.load_image_file("images/"+username+"/"+username+"12.png")
		print("Known Images loaded")
		
		user_image_enc = face_recognition.face_encodings(user_image)[0]
		user_image_enc1 = face_recognition.face_encodings(user_image1)[0]
		user_image_enc2 = face_recognition.face_encodings(user_image2)[0]
		print("Known Images Encoded")
		while True:
			i+=1
			ret , frame = cap.read()
			grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # coz above usd classifer needs grey scale frames
			faces = face_cascades.detectMultiScale(grey,scaleFactor=1.5,minNeighbors=5)
			for (x ,y ,w ,h) in faces:
				roi=frame[y:y+h,x:x+w]
				img_item="images/temp.png"
				cv2.imwrite(img_item ,roi)
				unknown_image = face_recognition.load_image_file("images/temp.png")
				unknown_image_face_location = face_recognition.face_locations(unknown_image)
				print("image loaded ...")
				print("number of faces are -> ",len(unknown_image_face_location))
				if(len(unknown_image_face_location)>=2):
					root =tkinter.Tk()
					root.withdraw()
					messagebox.showinfo("Alert !",''' I See More Than One Face 
						 Please Show True You :-)''')
				else:	
					unknown_image_enc = face_recognition.face_encodings(unknown_image,unknown_image_face_location)#,unknown_image)
					print("image encoded ...")
					results = face_recognition.compare_faces(user_image_enc,unknown_image_enc)
					results = face_recognition.compare_faces(user_image_enc1,unknown_image_enc)
					results = face_recognition.compare_faces(user_image_enc2,unknown_image_enc)
					if(results == False):
						os.remove("images/temp.png")
						cap.release()
						cv2.destroyAllWindows()
					#print(" I am {} in image ".format(results))

				rect_color=(255,255,255)
				stroke=1
				width=(x+w)
				height=(y+h)
				cv2.circle(frame,(x+(w//2),y+(h//2)),width//4,rect_color,stroke)
			cv2.imshow("test",frame)
			if cv2.waitKey(27) & 0XFF == ord('q') or i<=10:#or (i<=7 and len(unknown_image_face_location)==0):
				break

		os.remove("images/temp.png")
		cap.release()
		cv2.destroyAllWindows()
		return results
