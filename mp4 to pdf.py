"""
Welcome to mp4 to pdf auto working engine!
"""
import os
import re
from PIL import Image
import aircv as ac
import cv2
import img2pdf

def extract_path_components(file_path):
    # Split the path into directory and file components
    dir_path, file_name = os.path.split(file_path)
    return dir_path, file_name
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite(str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames
def ifsame(origin, search):
    imsrc = ac.imread(f"{origin}.jpg")
    imsch = ac.imread(f"{search}.jpg")
    match_result = ac.find_all_template(imsrc, imsch, 0.85)
    # print(str(origin) + '+' + str(search))
    if match_result != []:
        return True
    else:
        return False

path = input('path:').replace("\\","")
path = path.rstrip(path[-1])

# Call the function to extract components
dir_path, file_name = extract_path_components(path)
dir_path = dir_path + '/'
file_name = file_name.replace('.mp4', '')
vidcap = cv2.VideoCapture(path)
sec = 0
frameRate = 9 # it will capture image in each 0.5 second
count = 1
success = getFrame(sec)

while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
def main(dir_path, file_name):
    image_good = 1
    image_good_list = []
    for image_number in range(1, count):
        same = ifsame(image_good, image_number)
        if same == False:
            image_good_list.append(image_good)
            image_good = image_number
    print(str(image_good_list))
    thing = ''
    img_list = []
    for things in image_good_list:
        thing = str(things) + '.jpg'
        img_list.append(thing)
    images = [
        Image.open(dir_path + f)
        for f in img_list
    ]

    pdf_path = f"{dir_path}{file_name}.pdf"
    
    images[0].save(
        pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
    )
    
    test = os.listdir(dir_path)
    for item in test:
        if item.endswith(".jpg"):
            os.remove(os.path.join(dir_path, item))

if __name__ == '__main__':
    main(dir_path, file_name)
