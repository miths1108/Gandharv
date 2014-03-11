import configure
import connectify
import userlog
import dirlog
import time


def getUser(sock):
	try:
		userinfo = userlog.getInfo()
	except:	
		userinfo = configure.init(sock)
	userinfo = userinfo.split('^')[0]
#	print userinfo
	return userinfo

if __name__=="__main__":	
	sock = connectify.createCon()
	userinfo = getUser(sock)
	while 1:
		dirs, flag = dirlog.getDirs()
		if flag:
			sock.send('2'+userinfo+'^'+dirs)
			print  sock.recv(1024)
		sock.send('3'+userinfo)
		update_count = sock.recv(1024)
		update = []
		for x in range(0,int(update_count)):
			sock.send('4'+userinfo)
			update.append(sock.recv(1024))
		print update
		time.sleep(2)
	connectify.closeCon(sock)
