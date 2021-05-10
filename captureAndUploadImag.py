import time
import random
import cv2
import dropbox

start_time = time.time()
def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(1)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=  time.time
        return img_name
        result = False

   
    print("Image Taken") 

    videoCaptureObject.release()

    cv2.destroyAllWindows()


def upload_files(img_name):
    access_token = "ws43wjGjxogAAAAAAAAAAQJjSprcYnV8-U_65SUiI6Ec8rSSHqrzUXwRNgui9qW3"
    file = img_name
    file_from = file
    file_2 = '/'+(img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_2,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name = take_snapshot()
            upload_files(name)

main()