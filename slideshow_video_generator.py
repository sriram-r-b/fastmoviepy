from image_animator import Image_animator
import cv2
import os

# Create a video animator
temp=Image_animator(height =1080,width=1920)
# get the list of images from the dir - change the path as required
image_dir="unsplash_images"
images=os.listdir(image_dir)
image_paths=[os.path.join(image_dir,image) for image in images]
# zoomout
img=cv2.imread(image_paths[0])
img2=None
temp.zoomin(img,img2)
# zoomin
img2=img
img=cv2.imread(image_paths[1])
temp.zoomout(img2,img)
# translate_left
img2=img
img=cv2.imread(image_paths[2])
temp.translate_right(img2,img)
# translate_right
img2=img
img=cv2.imread(image_paths[3])
temp.translate_left(img2,img)
# zoomout
img2=img
img=cv2.imread(image_paths[4])
temp.zoomout(img2,img)
# zoomin
img2=img
img=cv2.imread(image_paths[5])
temp.zoomin(img,img2)



