#convert phylip to fasta
#Author: Thulek@gmail.com
 
from os import listdir
from os.path import isfile, join
import os
import sys
import platform
import subprocess
import time
import array as arr
#import runCommand

import argparse

text = "===================\nConvert Fasta to Phylip file\n===================="

parser = argparse.ArgumentParser(description = text)  
#parser.parse_args()  

jobIds = arr.array('i')

parser.add_argument("-f", "--filex", help="The input file")
parser.add_argument('-fasta', action='store_const', dest='fasta',const='1',help='convert 2 fasta option, for convert to fasta, remove for convert to phylip')
parser.add_argument("-o", "--output", help="the output file")

# read arguments from the command line
args = parser.parse_args()

filex = args.filex
output = args.output

fasta = 0
if args.fasta:
	fasta = 1
	
if fasta == 0:
	os.system("python convert2Phylip.py -f "+filex+" -o "+output)
else:
	os.system("python convert2Fasta.py -f "+filex+" -o "+output)
