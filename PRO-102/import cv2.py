import cv2
import dropbox
import time
import random


start_time=time.time()
def take_snapshot():
    number=random.randint(1,100)
    image=cv2.VideoCapture(0)
    result=True

    while(result):
        ret,frame="img"+str(number)+".jpg"
        cv2.imwrite(image_name,frame)
        start_time=time.time
        result=False
    return image_name
    print("image saved")

    image.release()
    cv2.destroyAllWindows()
take_snapshot()

def upload_image(image_name):
    access_token=""
    file=image_name
    file_from=file
    file_to="/"+file
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,"rb")as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file_uploaded")
def main():
    while(True):
        if((time.time()-start_time)>=5):
            image_name=take_snapshot()
            name=take_snapshot()
            upload_image(image_name)

main()