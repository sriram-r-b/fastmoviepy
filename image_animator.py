import cv2
import numpy as np
class Image_animator:
    def __init__(self,height =1920,width=1080,output_path="result.mp4",codec_string="mp4v",fps=45,show_img=True):
        self.width=width
        self.height=height    
        self.fourcc=cv2.VideoWriter_fourcc(*codec_string) 
        self.fps=fps
        self.videowriter=cv2.VideoWriter(output_path, self.fourcc, self.fps, (self.width,self.height))
        self.show_img=show_img
    
    def __del__(self):
        self.videowriter.release()
        
    def translate_right(self,img,img2,time=5,show_translation=False):
        img_shape=(self.width,self.height)
        img=cv2.resize(img, img_shape, interpolation = cv2.INTER_AREA)
        img2=cv2.resize(img2, img_shape, interpolation = cv2.INTER_AREA)
        num_frames = self.fps * time  # Total number of frames in the video
        max_translation_x = self.width  # Maximum horizontal translation
        for i in range(num_frames-2):
            translation_factor_x= np.sin(0.5* np.pi * i / num_frames) 
            translation_x = max_translation_x *translation_factor_x # Smooth horizontal translation
            translation_y=0
            translation_matrix = np.float32([
                [1, 0, translation_x],
                [0, 1, translation_y]
            ])

            translated_img = cv2.warpAffine(img, translation_matrix, (self.width, self.height))
            translated_img[:,:int(translation_x),  :] = img2[:,:int(translation_x), :]
            if self.show_img:
                cv2.imshow("video_frame",translated_img)
            
            self.videowriter.write(translated_img)
            cv2.waitKey(1)
                    
    def translate_left(self,img,img2,time=5,show_translation=False):
        img_shape=(self.width,self.height)
        img=cv2.resize(img, img_shape, interpolation = cv2.INTER_AREA)
        img2=cv2.resize(img2, img_shape, interpolation = cv2.INTER_AREA)
        num_frames = self.fps * time  # Total number of frames in the video
        # Translation parameters
        max_translation_x = self.width  # Maximum horizontal translation
        for i in range(num_frames-2):
            translation_factor_x=-np.sin(0.5* np.pi * i / num_frames) 
            translation_x = max_translation_x *translation_factor_x # Smooth horizontal translation
            translation_y=0
            # Create a translation matrix
            translation_matrix = np.float32([
                [1, 0, translation_x],
                [0, 1, translation_y]
            ])

            # Apply the translation
            translated_img = cv2.warpAffine(img, translation_matrix, (self.width, self.height))
            translated_img[:,int(translation_x):,  :] = img2[:,int(translation_x):, :]
            if self.show_img:
                cv2.imshow("video_frame",translated_img)
            

            self.videowriter.write(translated_img)
            cv2.waitKey(1)

    def zoomin(self,img,bg=None,time=5):
        img_shape=(self.width,self.height)
        img=cv2.resize(img, img_shape, interpolation = cv2.INTER_AREA)
        if bg is not None:
            bg=cv2.resize(bg, img_shape, interpolation = cv2.INTER_AREA)
        num_frames = self.fps * time  # Total number of frames in the video

        # Animation loop
        for i in range(1,num_frames):
            scale_factor = np.sin(0.5*np.pi * i / num_frames)  # Create a smooth zoom effect
            w=int(self.width*scale_factor)
            h=int(self.height*scale_factor)
            # Center the resized image within the video frame
            cx=int((self.width) / 2.0)
            cy=int((self.height) / 2.0)
            x = int((self.width/2.0) - (w / 2.0))
            y = int((self.height/2.0) - (h / 2.0))
            if bg is None:
                bg = np.zeros(( self.height,self.width, 3), np.uint8)
            video_frame=bg
            
            img_shape=video_frame[ y:y+h,x:x+w, :].shape[:2][::-1]
            resized_img = cv2.resize(img,img_shape,  interpolation=cv2.INTER_AREA)
            video_frame[ y:y+h,x:x+w, :] = resized_img
            if self.show_img:
                cv2.imshow("video_frame",video_frame)
            self.videowriter.write(video_frame)
            cv2.waitKey(1)
            
    def zoomout(self,img,bg=None,time=5):
        img_shape=(self.width,self.height)
        img=cv2.resize(img, img_shape, interpolation = cv2.INTER_AREA)
        if bg is not None:
            bg=cv2.resize(bg, img_shape, interpolation = cv2.INTER_AREA)
        num_frames = self.fps * time  # Total number of frames in the video

        # Animation loop
        for i in range(1,num_frames):
            scale_factor =1- np.sin(0.5*np.pi * i / num_frames)  # Create a smooth zoom effect
            
            w=int(self.width*scale_factor)
            h=int(self.height*scale_factor)
            if w==0 or h==0:
                continue
            cx=int((self.width) / 2.0)
            cy=int((self.height) / 2.0)
            x = int((self.width/2.0) - (w / 2.0))
            y = int((self.height/2.0) - (h / 2.0))
            if bg is None:
                bg = np.zeros(( self.height,self.width, 3), np.uint8)
            video_frame=bg.copy()
            img_shape=video_frame[ y:y+h,x:x+w, :].shape[:2][::-1]
            resized_img = cv2.resize(img,img_shape,  interpolation=cv2.INTER_AREA)
            video_frame[ y:y+h,x:x+w,] = resized_img
            if self.show_img:
                cv2.imshow("video_frame",video_frame)
            self.videowriter.write(video_frame)
            cv2.waitKey(1)
