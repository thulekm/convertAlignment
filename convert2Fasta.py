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

text = "===================\nConvert Phylip to Fasta file\n===================="

parser = argparse.ArgumentParser(description = text)  
#parser.parse_args()  

jobIds = arr.array('i')

parser.add_argument("-f", "--filex", help="The phylip file")
parser.add_argument("-o", "--output", help="the output file")

# read arguments from the command line
args = parser.parse_args()

filex = args.filex
output = args.output

def countLines(files):
	if(os.path.isfile(files)):
		with open(files) as f:
			return len(f.readlines())
	else:
		return 0

def convertPhylip2Fasta(filex,tofile):
	infile = open(filex,"r")
	outfile = open(tofile,"w")
	i = 1
	for line in infile:
		if i > 1:
			if len(line.strip()) >= 1:
				if "\t" in line:
					tx = line.split("\t",1)
					outfile.write(">"+tx[0].strip()+"\n")
					outfile.write(tx[1].strip()+"\n")
				elif " " in line:
					tx = line.split(" ",1)
					outfile.write(">"+tx[0].strip()+"\n")
					outfile.write(tx[1].strip()+"\n")
		i = i + 1
	outfile.close()
	infile.close()
	if(countLines(tofile)>0):
		print "Finish to create the fasta file."
	else:
		print "Create fasta file error."

if os.path.isfile(filex):
	convertPhylip2Fasta(filex,output)
	if os.path.isfile(output):
		print("Create file ok.")		
else:
	print "Input file's not exists."
	