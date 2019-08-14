'''Video extraction into frames'''

def extractframes(extraction_path, path):
    import cv2
    import os
    vidobj = cv2.VideoCapture(path)
    count = 0
    success = 1
    while success:
        vidobj.set(cv2.CAP_PROP_POS_MSEC, count*500,)
        
        success, frame = vidobj.read()
        cv2.imwrite(os.path.join(extraction_path ,"frame%d.jpg"%(count)),frame)
        
        count+=1

        if count==500:
            raise ValueError("Frame Count Exceeding 500")

        
    os.remove(os.path.join(extraction_path,"frame%d.jpg"%(count-1)))
