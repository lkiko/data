#coding = utf-8
###
###by charles lan###
###邮箱:charles_kiko@163.com###
###
#下载'ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/plant/'路径下的物种数据
import requests
import requests_ftp
import os
import sys

name=[]#储存目标物种
htname=[]#储存plant下已有物种
for line in open(sys.argv[1],"r"):
	name.append(line.strip("\n"))
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

def dow(url,name,htname):
	for i in name:
		if (i in htname):
			try:
				geturl="wget -r -np -nH -R index.html "+url+str(i)
				print(geturl)
				d=os.popen(geturl)
			except:
				print("网络或者其他错误！！！！！")
				continue
		else:
			print("%s名字错误或者%s未收录%s!!!!"%(i,url,i))

get(text)
dow(url,name,htname)

print("over!")