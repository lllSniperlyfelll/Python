import numpy as np
import cv2
import os
from PIL import Image
import pickle


def face_train():
	y_labels=[]
	train=[]
	cur_id=0
	label_id={}
	face_cascades=cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml') # classifier
	reco=cv2.face.LBPHFaceRecognizer_create()
	img_dir='images'
	for root , dirr ,files in os.walk(img_dir):
		for file in files:
			if file.endswith("png") or file.endswith("jpg"):
				#path=os.path.join(root,file)
				#print(path)

				path=img_dir+"/"+file
				label = img_dir+"/"+file.replace(" ","-").lower()

				#path=label
				print("label -> ",label)
				if not label in label_id:
					label_id[label] = cur_id
					cur_id+=1
				id_=label_id[label]
				#print(id_)

				pil_img=Image.open(path).convert('L').resize((600,600),Image.ANTIALIAS)#converts to grey
				
				# size=(600,600)
				# final_img=pil_img

				img_matrix = np.array(pil_img,'uint8')

				#print("img_matrix -> ",img_matrix)

				faces=face_cascades.detectMultiScale(img_matrix,scaleFactor=1.5,minNeighbors=5)
				print("face cascade open ->")
				for x,y,w,h in faces:
					roi = img_matrix[y:y+h , x:x+w]
					train.append(roi)
					#print("roi -> ",roi," id_ -> ",id_)
					y_labels.append(id_)
	#print(train)
	#print(y_labels)
	print("open labels.pkl")
	with open("user_names.pkl","wb") as f:
		pickle.dump(label_id,f)
	print("closed labels.pkl")

	reco.train(train,np.array(y_labels))
	reco.save("user_trained.yml")










def face_id():

	labels={}
	face_cascades=cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml') # classifier
	reco=cv2.face.LBPHFaceRecognizer_create()
	reco.read("user_trained.yml")
	with open("user_names.pkl","rb") as f:
		og_labels=pickle.load(f)
		labels={v:k for k,v in og_labels.items()}
		print(labels)


	cap=cv2.VideoCapture(0)
	i=1
	while True:
		ret , frame = cap.read()
		grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # coz above usd classifer needs grey scale frames
		faces = face_cascades.detectMultiScale(grey,scaleFactor=1.5,minNeighbors=5)
		for (x ,y ,w ,h) in faces:
			#print(x,y,w,h)
			roi_gray = grey[y:y+h,x:x+w]
			id__ , conf =reco.predict(roi_gray)
			name=(labels[id__]).replace("images/","")

			print("name -> ",name,"confidence -> ",conf) if(conf>=60) else print()
			
			cv2.putText(frame,name ,(x,y) ,cv2.FONT_HERSHEY_SIMPLEX ,1 ,(255,255,255),3,cv2.LINE_AA)
			# img_item="images/pravleen"+str(i)+".png"
			# i+=1
			# cv2.imwrite(img_item ,frame[y:y+h,x:x+w])
			rect_color=(255,0,0)
			stroke=4
			width=(x+w)
			height=(y+h)
			cv2.rectangle(frame,(x,y),(width+5,height+5),rect_color,stroke)
		cv2.imshow("test",frame)
		if cv2.waitKey(27) & 0XFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()
	root.destroy()

#face_train()
face_id()

