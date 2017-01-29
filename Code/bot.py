#!/usr/bin/python 2.4
#my sms sending bot..
import urllib2
import sys
import time
import cookielib
from getpass import getpass
def main():
	user='8547546280'
	pas=''
	pas=getpass()
	auth(user,pas)

def auth(user,pas):
	moblist=["8080765267","9920723683"]
	fp=open('data.txt','rs=fp.readlines()
	for dat in lines:	
		for mob in moblist:
			url='http://site4.way2sms.com/Login1.action'
			data='username='+user+'&password='+pas+'&button=Login'
			cj=cookielib.CookieJar()
			opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
			opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Ubuntu/9.10 (karmic) Firefox/3.5.3 GTB7.0')]
			try:
				print ' '
				usock=opener.open(url,data)
			except IOError:
				print "Check connection.."
				sys.exit()

			urr='http://site4.way2sms.com/quicksms.action'
			data2='HiddenAction=instantsms&catnamedis=Birthday&Action=sa65sdf656fdfd&chkall=on&MobNo='+mob+'&textArea='+dat
			send=opener.open(urr,data2)
			print mob
			print dat

if __name__=="__main__":
	main()