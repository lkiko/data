#coding = utf-8
##blast.py调用cmd执行blast
#基础文件为faa和物种列表
###
###by charles lan###
###邮箱:charles_kiko@163.com###
###

import os
from multiprocessing import cpu_count#读取CPU核心数用于匹配线程数

name=[]
for line in open("test.txt",mode='r'):#################
	x=line
	if (x!='' and x!="\n"):
		x=x.strip("\n")
		lt=x.split("\t")
		name.append(str(lt[0]))
		name.append(str(lt[1]))

print(name)
cpu=str(cpu_count())
for i in range(int(len(name)/2)):
	library=str(name[(i*2)-1])
	db=library[:-4]+".library"
	print("makeblastdb -in %s -dbtype prot -out %s" % (library,db))
	d=os.popen("makeblastdb -in %s -dbtype prot -out %s" % (library,db)).read().strip()
	blast=str(name[i*2])
	result=library[:-4]+"_"+blast[:-4]+".1e-5.blast"
	print("blastp -query %s -db %s -out %s -outfmt 6 -evalue 1e-5 -num_threads %s" % (blast,db,result,cpu))
	d=os.popen("blastp -query %s -db %s -out %s -outfmt 6 -evalue 1e-5 -num_threads %s" % (blast,db,result,cpu)).read().strip()
	print(library[:-4]+"_"+blast[:-4]+"blast结束！")

print('程序运行结束!!!')

