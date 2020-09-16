#coding = utf-8
###
###by charles lan###
###邮箱:charles_kiko@163.com###
###

#blast数据读取与储存
import sys
blast=[]#储存blast信息的列表
query=[]
num=5#决定蓝色点个数
number=1
r=[]#红色点列表
b=[]#蓝色点列表&蓝色点除了基础个数之外我将阈值为0的点也划为蓝色
g=[]#灰色点列表

def blast():
	for line in open(sys.argv[1]):
		blast=line.strip("\n").split("\t")
		if (str(blast[0]) not in query):
			query.append(str(blast[0]))
			r.append(str(blast))
			number=1
		else:
			if (number<=num or eval(blast[10])==0):
				b.append(str(blast))
				number=number+1
			else:
				g.append(str(blast))
blast()

print(str(r)+"\n")
print(str(b)+"\n")
print(str(g)+"\n")