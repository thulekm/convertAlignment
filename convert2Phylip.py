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

parser.add_argument("-f", "--filex", help="The Fasta file")
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

def line_prepender(filename, line):
	with open(filename, 'r+') as f:
		content = f.read()
		f.seek(0, 0)
		f.write(line.rstrip('\r\n') + '\n' + content)


def convertFasta2Phylip(filex,tofile):
	taxa = 0
	sites = 0
	infile = open(filex,"r")
	outfile = open(tofile,"w")
	i = 1
	for line in infile:
		if len(line.strip()) >= 1:
			if ">" in line:
				tx = line.strip(">").split("|")[0]
				tx = tx.split("/")[0]
				outfile.write(tx.strip()+"\t")
				taxa = taxa + 1
			else:
				outfile.write(line.strip()+"\n")
				if sites < len(line.strip()):
					sites = len(line.strip())
		i = i + 1
	outfile.close()
	infile.close()
	if(countLines(tofile)>0):
		line_prepender(tofile, str(taxa)+" "+str(sites))
		print "Finish to create the phylip file."
	else:
		print "Create phylip file error."

if os.path.isfile(filex):
	convertFasta2Phylip(filex,output)
	if os.path.isfile(output):
		print("Create file ok.")		
else:
	print "Input file's not exists."
	