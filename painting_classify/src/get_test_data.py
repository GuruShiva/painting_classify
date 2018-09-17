#!/home/ml/anaconda3/bin/python3

#This script automates the data gathering for testing
# You need to have googleimagesdownload and chromedriver installed before being able to run the script

import requests
import subprocess


target = ['"van gogh painting"'] #Class (Type of painting you want to download for testing the image classification)
limit_num = str(10) #Num of images wanted
offset_num = str(1) #To skip x number of links before downloading the images (Optional) 
img_format = "jpg"
output_path= '"/home/ml/image_classification/challenges/painting_classify/painting_classify/tf_files/data/test/"'
for i in target:
    cmd = "googleimagesdownload --keywords " + i +  " --limit "  + limit_num  + " --format " + img_format + " --no_numbering " + " --offset " + offset_num + " --output_directory " + output_path
    print (cmd)
    pipe = subprocess.Popen(cmd, shell=True)
    pipe.wait()
    print ("Dataset complete")
