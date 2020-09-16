#coding = utf-8
###
###by charles lan###
###邮箱:charles_kiko@163.com###
###
#fna数据的存取建立关系
import sys
import re

sqr={}
sq=''
def fna(argv):
	for line in open(sys.argv[1]):
		print(line)
		notes=line.strip("\n")
		if (notes[0]==">"):
			note=notes.split(" ")
			print(str(note[0]))
			#if (sq!=""):
			#	sqr[]
			#	sq=''
			print(str(note[0]))
		else:
			if (sq==''):
				sq=notes
			else:
				sq=sq+notes
fna(sys.argv)