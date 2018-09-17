#!/home/ml/anaconda3/bin/python3

#This script automates the data gathering for training
# You need to have googleimagesdownload and chromedriver installed before being able to run the script
import requests
import subprocess

target = ['"impressionism painting"', '"expressionism painting"', '"fauvism painting"', '"modern abstract painting"'] #Classes (In this case, the type of paintings you want to download and train)
limit_num = str(500) #500 images per class
img_format = "jpg"
chromedriver = "/usr/local/bin/chromedriver" #Chromedriver is necessary if you want use 'googleimagesdownload' for over 100 images
output_path= '"/home/ml/image_classification/challenges/painting_classify/painting_classify/tf_files/data/train/"'
for i in target:
    cmd = "googleimagesdownload --keywords " + i +  " --limit "  + limit_num  + " --format " + img_format + " --no_numbering " + " --chromedriver " + chromedriver + " --output_directory " + output_path
    print (cmd)
    pipe = subprocess.Popen(cmd, shell=True)
    pipe.wait()
    print ("Dataset complete")
