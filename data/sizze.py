from PIL import Image
import numpy as np

with open("/home/syed/EVA/YoloV3/data/customshape.txt", "w") as file1: 
    # Writing data to a file 
    for i in range(1,10):
        im = np.array(Image.open('/home/syed/EVA/YoloV3/data/customdata/images/train/image-00' + str(i)+ '.jpg'))
        h,w,_ = im.shape
        file1.writelines(str(w) + " " + str(h) + '\n')
    for i in range(10,100):
        im = np.array(Image.open('/home/syed/EVA/YoloV3/data/customdata/images/train/image-0' + str(i)+ '.jpg'))
        h,w,_ = im.shape
        file1.writelines(str(w) + " " + str(h)+ '\n')
    for i in range(100,476):
        if i in (199, 277, 307,333):
            continue
        im = np.array(Image.open('/home/syed/EVA/YoloV3/data/customdata/images/train/image-' + str(i)+ '.jpg'))
        h,w,_ = im.shape
        file1.writelines(str(w) + " " + str(h)+ '\n')