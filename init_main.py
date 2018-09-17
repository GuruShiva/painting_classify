#!/home/ml/anaconda3/bin/python3

import requests
import subprocess

folder_path = '"/home/ml/image_classification/challenges/painting_classify/painting_classify/"'

def git_data_science_file_structure():
    print ("Building Data Sciene File Structure")
    #This git repo provides the folder structure and necessary python files for training and labelling
    url = "https://github.com/johannesharmse/learn_image_classification.git"
    print (url)
    gitcmd = "git clone " + url + " " + folder_path
    print (gitcmd)
    pipe = subprocess.Popen(gitcmd, shell=True)
    pipe.wait()
    print ("Cloning complete")




def main():
    git_data_science_file_structure()


if __name__ == "__main__":
    main()