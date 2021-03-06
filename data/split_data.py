'''
File to mimic structure of training and testing data of the voxelnet repo. File takes in text files listing the point clouds and splits the data into testing and training data.
'''

import pandas
from shutil import copyfile
import os

train=pandas.read_table("ImageSets/train.txt",header=None,dtype="str")
validation=pandas.read_table("ImageSets/val.txt",header=None,dtype="str")

train.columns= ["filename"]
validation.columns= ["filename"]

#cropped data directory
original_directory="/ufrc/ewhite/b.weinstein/"
destination_directory="/ufrc/ewhite/b.weinstein/voxelnet_split/"

train.columns= ["filename"]
for index,row in train.iterrows():
    pc="training/velodyne/%s.bin" % row.filename
    im="training/image_2/%s.png" % row.filename
    label="training/label_2/%s.txt" % row.filename
    
    for f in [pc,im,label]:
        if not os.path.exists(destination_directory+f):
            copyfile(original_directory + f,destination_directory+f)
    
for index,row in validation.iterrows():
    pc="training/velodyne/%s.bin" % row.filename
    im="training/image_2/%s.png" % row.filename
    label="training/label_2/%s.txt" % row.filename
    
    for f in [pc,im,label]:
        #validation dir name
        x=f.replace("training","testing")
        if not os.path.exists(destination_directory+x):
            copyfile(original_directory + f,destination_directory+x)