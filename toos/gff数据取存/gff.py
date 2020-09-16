#coding = utf-8
###
###by charles lan###
###邮箱:charles_kiko@163.com###
###
#gff数据读取与储存
import sys
import re

target1='CDS'
target2=['ID','gene']

def gff():
	chro=''
	xhkz=0
	num1=0#染色体状态
	ch=[]#染色体计数
	f=open("xx.cds.gff","w")
	for line in open(sys.argv[1]):
		if (line[0]!="#"):
			data=line.strip("\n").split("\t")
			if (str(data[2])=="region"):
				num1=1#表示文件chr名未改
				chro=str(re.findall(r"chromosome=(.*?);",line))[2:-2]
			elif (str(data[2])==target1):
				tq=''#lt8提取状态
				na={}#lt8的字典
				if (num1==1):
					if(chro not in ch):
						ch.append(chro)
						gene=1#基因计数，对CDS不准确
						lt8=str(data[8]).split(";")
						for i in lt8:
							na[str(i)[0:str(i).rfind('=')]]=str(i)[str(i).rfind('=')+1:]
						for i in target2:
							if (tq!=''):
								tq=tq+"\t"+str(na[i])
							else:
								tq=str(na[i])
					else:
						gene=gene+1
						lt8=str(data[8]).split(";")
						for i in lt8:
							na[str(i)[0:str(i).rfind('=')]]=str(i)[str(i).rfind('=')+1:]
						for i in target2:
							if (tq!=''):
								tq=tq+"\t"+str(na[i])
							else:
								tq=str(na[i])
					print(chro+"\t"+tq+"\t"+str(data[3])+"\t"+str(data[4])+"\t"+str(data[6])+"\t"+str(gene)+"\n")
					f.write(chro+"\t"+tq+"\t"+str(data[3])+"\t"+str(data[4])+"\t"+str(data[6])+"\t"+str(gene)+"\n")
				else:
					if(chro not in ch):
						ch.append(chro)
						gene=1#基因计数，对CDS不准确
						lt8=str(data[8]).split(";")
						for i in lt8:
							na[str(i)[0:str(i).rfind('=')]]=str(i)[str(i).rfind('=')+1:]
						for i in target2:
							if (tq!=''):
								tq=tq+"\t"+str(na[i])
							else:
								tq=str(na[i])
					else:
						gene=gene+1#基因计数，对CDS不准确
						lt8=str(data[8]).split(";")
						for i in lt8:
							na[str(i)[0:str(i).rfind('=')]]=str(i)[str(i).rfind('=')+1:]
						for i in target2:
							if (tq!=''):
								tq=tq+"\t"+str(na[i])
							else:
								tq=str(na[i])
					print(str(data[0])+"\t"+tq+"\t"+str(data[3])+"\t"+str(data[4])+"\t"+str(data[6])+"\t"+str(gene)+"\n")
					f.write(str(data[0])+"\t"+tq+"\t"+str(data[3])+"\t"+str(data[4])+"\t"+str(data[6])+"\t"+str(gene)+"\n")
	f.close()
gff()
print("运行结束!")