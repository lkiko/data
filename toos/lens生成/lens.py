#coding = utf-8
###
###by charles lan###
###邮箱:charles_kiko@163.com###
###
#生成lens文件

def lens():
	f = open ("sq.lens",mode = 'w',encoding = 'utf-8')#输出文件名###############################
	number=0
	chr=''
	lon=''
	for line in open ("sq.gff",mode = 'r'):###############################
		x = line
		x=x.strip("\n")
		lt=x.split("\t")
		if (str(lt[0])!=chr):
			#print(chr)
			#print(lon)
			#print(number)
			if (chr!=''):
				f.write(chr+"\t"+lon+"\t"+str(number)+"\n")
			chr=str(lt[0])
			number=0
		lon=str(lt[3])
		number=number+1

lens()