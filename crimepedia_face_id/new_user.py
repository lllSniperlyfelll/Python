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
				if(i>=10 and i<=12):
					img_item=path+"/"+username+str(i)+".png"
					
					cv2.imwrite(img_item ,frame[y:y+h,x:x+w])
				i+=1
				rect_color=(255,0,0)
				stroke=1
				width=(x+w)
				height=(y+h)
				cv2.circle(frame,(x+(w//2),y+(h//2)),width//4,rect_color,stroke)
			cv2.imshow("test",frame)
			if cv2.waitKey(27) & 0XFF == ord('q') or i>=36:
				break





		cap.release()
		root.destroy()
		cv2.destroyAllWindows()
		messagebox.showinfo("Done!!","Try loggin in now")
































# NFC=NEW_FACE_CAPTURE()

# NFC.capture_face()


# def face_recognizer_dlib():

# 	labels={}
# 	face_cascades=cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml') # classifier
# 	# reco=cv2.face.LBPHFaceRecognizer_create()
# 	# reco.read("trained.yml")
# 	# with open("labels.pkl","rb") as f:
# 	# 	og_labels=pickle.load(f)
# 	# 	labels={v:k for k,v in og_labels.items()}



# 	cap=cv2.VideoCapture(0)
# 	i=1
# 	user_image=face_recognition.load_image_file("images/snip1.png")
# 	user_image_enc = face_recognition.face_encodings(user_image)[0]



# 	while True:
# 		ret , frame = cap.read()
# 		grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # coz above usd classifer needs grey scale frames
# 		faces = face_cascades.detectMultiScale(grey,scaleFactor=1.5,minNeighbors=5)
# 		for (x ,y ,w ,h) in faces:

# 			roi=frame[y:y+h,x:x+w]
# 			img_item="images/temp.png"
# 			i+=1
# 			cv2.imwrite(img_item ,roi)


# 			unknown_image = face_recognition.load_image_file("images/temp.png")
# 			unknown_image_face_location = face_recognition.face_locations(unknown_image)
# 			print("image loaded ...")
# 			unknown_image_enc = face_recognition.face_encodings(unknown_image,unknown_image_face_location)#,unknown_image)
# 			print("image encoded ...")
# 			print("number of faces are -> ",len(unknown_image_face_location))
# 			results = face_recognition.compare_faces(user_image_enc,unknown_image_enc)


# 			print(" I am {} in image ".format(results));
	
# 			rect_color=(255,255,255)
# 			stroke=1
# 			width=(x+w)
# 			height=(y+h)
# 			cv2.circle(frame,(x+(w//2),y+(h//2)),width//4,rect_color,stroke)
# 		cv2.imshow("test",frame)
# 		if cv2.waitKey(27) & 0XFF == ord('q'):
# 			break

# 	os.remove("images/temp.png")
# 	cap.release()
# 	cv2.destroyAllWindows()
