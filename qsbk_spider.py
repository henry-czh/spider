#/bin/python

import re
import urllib
import urllib2

def getcontent(url,page):
	headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/38.0.2125.122 Saferi/537.36 SE 2.X MetaSr 1.0")
	opener=urllib2.build_opener()
	opener.addheaders= [headers]
	urllib2.install_opener(opener)

	#data=urllib2.urlopen(url).read().decode("utf-8")
	data=urllib2.urlopen(url).read()
	#print data
	usrpat='alt=".+?"'
	usrh_pat='alt="'
	usrd_pat='"'
	contentpat='<span>\n\n\n.*?\n'
	userlist=re.compile(usrpat).findall(data)
	contentlist=re.compile(contentpat,re.M).findall(data)
	usrlist=[]
	cttlist=[]
	#print (contentlist)
	for line in userlist:
		if re.search(usrpat,line) == None:
			print line
			print "n"
		else:
			#print "*"
			#print re.search(usrpat,line)
			usr_line=re.search(usrpat,line)
			usr_name1=re.sub(usrh_pat,"",line)
			usr_name=re.sub(usrd_pat,"",usr_name1)
			usrlist.append(usr_name)
	print (usrlist[0])
	print (usrlist[1])
	print (usrlist[2])
	print (usrlist[3])

	for content in contentlist:
		if re.search(contentpat,content) == None:
			print "none"
		else:
			#print (content)
			content=content.replace("\n","")
			content=content.replace("<span>","")
			cttlist.append(content)

	print len(cttlist)
	print len(usrlist)
	#print contentlist
	#exec("print("+contentlist+")")

	#output file set
	output=open("/home/czh/python/spider/qs.txt","w")

	if len(usrlist) <= len(cttlist):
		x=0
		for txt in usrlist:
			output.write("user:%s\n" % (txt))
			output.write("content:%s\n" % (ctlist[x]))
			output.write("\n")
			x+=1
	else:
		x=0
		for txt in cttlist:
			output.write('user:%s\n' % (usrlist[x]))
			output.write("content:%s\n" % (txt))
			output.write("\n")
			x+=1
			
	output.close()	


	#x=1
	#for content in contentlist:
	#	content=content.replace("\n","")
	#	name="content"+str(x)
	#	exec(name+'=content')
	#	x+=1
	#
	#y=1
	#for user in userlist:
	#	name="content"+str(y)
	#	#print("user"+str(page)+str(y)+":"+user)
	#	print("content:")
	#	#exec("print("+name+")")
	#	print("\n")
	#	y+=1

for i in range(1,2):
	url="https://www.qiushibaike.com/text/page/"+str(i)
	getcontent(url,i)
