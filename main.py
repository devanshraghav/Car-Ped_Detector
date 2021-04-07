import cv2
import os



while True : 
	selected = input('1. Use Video Location \n2. Use live camera \nYour Input :  ')
	if selected == '1' : 
		video_location = input('Enter video location : ') 
		#check if file exist or not 
		if not os.path.exists(video_location) :  # Or folder
			print('file not found!')
			exit()


		if video_location.split('.').pop().lower() != 'mp4' : 
			print('Only mp4 file allowed!')
			exit()


		video = cv2.VideoCapture(video_location);
		break


	elif selected == '2' :
		video = cv2.VideoCapture(0)
		break
	else : 
		print(">>>>Wrong Input")





#get current dictionary 
current_dir = os.path.dirname(os.path.realpath(__file__)) + '/';

#xml file to track car and pedestrian
track_car_file_location = current_dir + 'car.xml'
track_pedestrian_file_location = current_dir + 'pedes.xml'

#create car and pedestrian
track_car = cv2.CascadeClassifier(track_car_file_location);
track_pedestrian = cv2.CascadeClassifier(track_pedestrian_file_location);


while True : 
	#read one frame at a time
	(successful,frame) = video.read();

	#for
	if successful : 
		#conver file to grayscale
		grayscaled_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	else : 
		break

	#detect the car 
	cars = track_car.detectMultiScale(grayscaled_frame);

	#detect pedestrians
	pedestrians = track_pedestrian.detectMultiScale(grayscaled_frame);

	#draw a rectangles around the cars 
	for (x,y,w,h) in cars : 
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

	#draw a rectangles around the pedestrians
	for (x,y,w,h) in pedestrians : 
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)

	#displaying the images (current frame)
	cv2.imshow('main',frame)	

	key = cv2.waitKey(1);

	#stop if entered
	if key == 81 or key == 113 : 
		break

#releae the videoCapture object 

video.release();
