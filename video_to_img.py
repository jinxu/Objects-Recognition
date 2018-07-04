import os
import cv2
dataset = 'dataset/'
videoes_dir = dataset + 'videoes/'
photoes_dir = dataset + '/products/'

for video_file in os.listdir(videoes_dir):
    if (video_file=='.DS_Store'): continue
    dest_dir = photoes_dir+video_file[:-4]
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    vidcap = cv2.VideoCapture(videoes_dir+video_file)
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
        cv2.imwrite(dest_dir+"/frame%d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        count += 1

    


