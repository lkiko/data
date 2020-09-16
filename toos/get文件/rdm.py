#coding = utf-8
###
###by charles lan###
###邮箱:charles_kiko@163.com###
###
#测试用的随机物种生成
import requests
import requests_ftp
import os
import random


name=[]
htname=[]
f=open("cs.txt","w")

#print(name)
requests_ftp.monkeypatch_session()
url = 'ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/plant/'
s = requests.Session()
res = s.list(url)
res.encoding = 'utf-8'
text=str(res.text).strip("\n")
def get(text):
	lt=text.split("\n")
	for i in lt:
		lt1=str(i).strip("\r").split(" ")
		if (str(lt1[0])[-1]=="x"):
			htname.append(str(lt1[-1]))
	#print(htname)
get(text)
for i in range(5):
	x=random.choice(htname)
	name.append(x)
	htname.remove(x)

for i in name:
	f.write(str(i)+"\n")
f.close()