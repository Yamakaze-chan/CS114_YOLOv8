
# RUN THIS
from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
#RUN THIS
# %cd "/content/drive/MyDrive/CS114"

!nvidia-smi #Check GPU run or not

!pwd #Check path

#RUN THIS
!pip install ultralytics

!yolo checks

#get dataset detect license plate
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="9kyd4JYgozcndtViaLzD")
project = rf.workspace("yolov8-license-plate").project("vnlp-dataset-yolov8")
dataset = project.version(4).download("yolov8")

#get dataset character of license plate
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="T66Iu0BbGC7n9lSwcHRY")
project = rf.workspace("yolov8-7gy3r").project("vnlp-character-dataset-yolov8-version-2")
dataset = project.version(1).download("yolov8")

#train model detect LP
!yolo task=detect mode=train model="/content/drive/MyDrive/CS114/yolov8s.pt" data="/content/drive/MyDrive/CS114/VNLP-Dataset-YOLOv8-4/data.yaml" epochs=50 imgsz=640

#train model detect LP
!yolo task=detect mode=train model="/content/drive/MyDrive/CS114/yolov8s.pt" data="/content/drive/MyDrive/CS114/VNLP-Character-Dataset-YOLOv8-VERSION-2-1/data.yaml" epochs=50 imgsz=640

!yolo task=detect mode=predict model="/content/best.pt" conf=0.1 source="/content/Capture (77).PNG" save=True

#RUN THIS
#import library
from ultralytics import YOLO
import numpy as np
from PIL import Image
import cv2
from google.colab.patches import cv2_imshow
import torch
import matplotlib.pyplot as plt

dict_char = {
    0:0,
    1:1,
    2:2,
    3:3,
    4:4,
    5:5,
    6:6,
    7:7,
    8:8,
    9:9,
    10: 'A',
    11: 'C',
    12: 'D',
    13: 'E',
    14: 'G',
    15: 'H',
    16: 'K',
    17: 'R',
    18: 'S',
}

#RUN THIS
#set Model to detect License plate
model = YOLO("/content/drive/MyDrive/CS114/runs/detect/train5/weights/best.pt")
# set model parameters
model.overrides['conf'] = 0.25  # NMS confidence threshold
model.overrides['iou'] = 0.45  # NMS IoU threshold

#set Model to detect character
model_char = YOLO("/content/drive/MyDrive/CS114/runs/detect/train6/weights/best.pt")
# set model parameters
model_char.overrides['conf'] = 0.85  # NMS confidence threshold
model_char.overrides['iou'] = 0.45  # NMS IoU threshold



#RUN THIS
#Set path to image
#path_img = "/content/drive/MyDrive/CS114/VNLP-Dataset-YOLOv8-4/test/images/Capture-44-_PNG.rf.9a981311868a275b4bfda3688e55ce17.jpg"
path_img = "/content/drive/MyDrive/CS114/picture/Capture (56).PNG"

#RUN THIS
result=model.predict(path_img,save=False, save_txt=False, save_crop=False)

#RUN THIS
arr_of_coor = []
for i in result:
  print(i)
#for i in result:
  #print(i.boxes[1].xyxy.tolist())
#print(result.boxes)
for i in result:
  for j in i.boxes:
    arr_of_coor.append(sum(j.xyxy.tolist(),[])) #flatten

def resize_img (image):
  h, w,_ = image.shape
  new_h = 256//h
  new_w = 256//w
  scale_num = max(new_h, new_w)
  return scale_num

def check_row(box1, box2):
    yi1 = max(box1[1],box2[1])
    yi2 = min(box1[3],box2[3])
    inter_area = (yi2-yi1)
  
    box1_area = (box1[3]-box1[1])
    box2_area = (box2[3]-box2[1])
    union_area = box1_area+box2_area-inter_area
    
    iou = inter_area/union_area
    
    return iou

#RUN THIS
#image = cv2.imread("/content/download (59).png")
def read_LP(image):
  
  model_char = YOLO("/content/drive/MyDrive/CS114/runs/detect/train6/weights/best.pt")
  # set model parameters
  model_char.overrides['conf'] = 0.85  # NMS confidence threshold
  model_char.overrides['iou'] = 0.45  # NMS IoU threshold
  #
  #path_img_char = "/content/download (69).png"

  result_char=model_char.predict(image,save=False, save_txt=False, save_crop=False)

  arr_of_coor_char = []
  cls_list = []

  for i in result_char:
    for j in i.boxes:
      arr_of_coor_char.append(sum(j.xyxy.tolist(),[])) #flatten
      cls_list.append(int(j.cls.item()))

  #RUN THIS
  index = 0
  LP_char_ls = []
  highest_box = (0,0,0,0)
  lowest_box = (10000,10000,10000,10000)
  for i in arr_of_coor_char:
    #convert to int
    i = list(map(int, i))
    #print(i)

    #get x y w h
    x = i[0]
    y = i[1]
    w = i[2]
    h = i[3]

    #resize then crop picture
    #print(x,y,w,h)
    ROI = image[y:h, x:w]
    scale_number = resize_img(ROI)
    width = int(ROI.shape[1] * scale_number)
    height = int(ROI.shape[0] * scale_number)
    dim = (width, height)
    ROI = cv2.resize(ROI, dim,interpolation = cv2.INTER_AREA)
    #cv2_imshow(ROI)

    if y < lowest_box[1]:
      lowest_box = (i[0],i[1],i[2],i[3])
    if h > highest_box[3]:
      highest_box = (i[0],i[1],i[2],i[3])
    LP_char_ls.append(((i[0],i[1],i[2],i[3]),cls_list[index]))
    index=index+1
    cv2.rectangle(image, (i[0],i[1]), (i[2],i[3]), (255, 0, 0),1)


  row = check_row(lowest_box,highest_box )
  #print(row)
  if row>0:
    #neu chi co 1 dong thi doc tu trai sang phai
    LP_char_ls=sorted(LP_char_ls,key=lambda l:l[0][0], reverse=False)
    #print([i[1] for i in LP_char_ls])
    for i in LP_char_ls:
      temp = i[1]+0
      print(dict_char[temp],end='')
  else:
    #neu co 2 dong thi doc tu tren xuong
    LP_char_ls=sorted(LP_char_ls,key=lambda l:l[0][3], reverse=False)
    #print(LP_char_ls)
    print([i[1] for i in LP_char_ls])
    for i in LP_char_ls:
      temp = i[1]+0
      print(dict_char[temp],end='')
  cv2_imshow(image)

#RUN THIS
image = cv2.imread(path_img)
list_roi = []
for i in arr_of_coor:
  i = list(map(int, i))
  #print(i)
  x = i[0]
  y = i[1]
  w = i[2]
  h = i[3]
  #print(x,y,w,h)
  ROI = image[y:h, x:w]
  #cv2_imshow(ROI)
  ROI = np.ascontiguousarray(ROI)
  
  #ROI = preprocessing(ROI)
  scale_number = resize_img(ROI)
  width = int(ROI.shape[1] * scale_number)
  height = int(ROI.shape[0] * scale_number)
  dim = (width, height)
  ROI = cv2.resize(ROI, dim,interpolation = cv2.INTER_AREA)
  #list_roi.append(ROI)
  #img_gray_lp = cv2.cvtColor(ROI, cv2.COLOR_BGR2GRAY)
  #_, img_binary_lp = cv2.threshold(img_gray_lp, 200, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
  #img_binary_lp = 255 - img_binary_lp
  #cv2_imshow(ROI)
  read_LP(ROI)
  

  #cv2.rectangle(image, (i[0],i[1]), (i[2],i[3]), (255, 0, 0),1)
  #cv2_imshow(image)

