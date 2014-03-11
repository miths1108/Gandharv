def init(request, db):
	username = (request.split('^'))[0]
	cur = db.cursor() 
	cur.execute("SELECT * FROM updates WHERE username ='"+username+"'")
	return cur.fetchall()


def getCount(request, db):
	return str(len(init(request, db)))


def getUpdate(request, db):
	resultset = init(request, db)
	cur = db.cursor() 
	if resultset[0][1] == "fetch":
		content = "fetch"+'^'+resultset[0][0]
	'''elif resultset[0][1] == "add":
		cur.execute("SELECT versions FROM files WHERE projectid = '"+filename1[0]+"' AND filename ='"+filename1[1]+"'")
		res = cur.fetchall()
		version = res[0][0] 
		filename = filename+'^'+str(version)
		sock = connectFilesystem.createCon()
		string = connectFilesystem.getResponse("1"+filename,sock)
		connectFilesystem.closeCon(sock)
	
#		fp = open("../filesystem/"+filename,'r')
#		for line in fp:
#			string = string +line
		cur.execute("SELECT projectname FROM project_info WHERE projectid = '"+filename1[0]+"'")
		res = cur.fetchall()
		content = "add"+'^'+"Sync-n-Share/"+res[0][0]+'/'+filename1[1]+'^'+string
	elif resultset[0][1] == "delete":
		filename = resultset[0][0].split('^')
		cur.execute("SELECT projectname FROM project_info WHERE projectid = '"+filename[0]+"'")
		res = cur.fetchall()
		content = "delete"+'^'+"Sync-n-Share/"+res[0][0]+'/'+filename[1]
	elif resultset[0][1] == "rename":
		filename = resultset[0][0].split('^')
		cur.execute("SELECT projectname FROM project_info WHERE projectid = '"+filename[0]+"'")
		res = cur.fetchall()
		filename2 = resultset[0][4].split('^')
		content = 'rename^'+'Sync-n-Share/'+res[0][0]+'/'+filename2[1]+'^'+'Sync-n-Share/'+res[0][0]+'/'+filename[1]
	elif resultset[0][1] == "modify":
		print "in modify"
		filename=resultset[0][0].replace("/",'^')
		filename1 = resultset[0][0].split('^')
		cur.execute("SELECT versions FROM files WHERE projectid = '"+filename1[0]+"' AND filename ='"+filename1[1]+"'")
		res = cur.fetchall()
		version = int(res[0][0]) 
		print version
		cur.execute("SELECT version FROM updates WHERE operation = 'modify' AND filename ='"+filename1[0]+'^'+filename1[1]+"'")
		res = cur.fetchall()
		version2 = int(res[0][0])
		version2 -=1
		cur.execute("SELECT projectname FROM project_info WHERE projectid = '"+filename1[0]+"'")
		rest = cur.fetchall()
		print version
		print version2
		if version>version2+1:
			virtualfile = createVirtualFile(filename1[0]+'^'+filename1[1]+'^'+str(version2))
			for i in range (version2, version):
				virtualfile = getfinalfile(virtualfile, i, filename1[0]+'^'+filename1[1])
			string = getdiff(virtualfile)
		else:
			sock = connectFilesystem.createCon()
			string = connectFilesystem.getResponse("1"+filename+'^'+str(version-1),sock)
			connectFilesystem.closeCon(sock)
	
	#		fp = open("../filesystem/"+filename+"^"+str((version-1)),'r')
	#		for line in fp:
	#			string = string +line
			print string
		content = "modify"+'^'+"Sync-n-Share/"+rest[0][0]+"/"+filename1[1]+"^"+string
	elif resultset[0][1] == "fetch":
		print "fetch entered"
		filename = resultset[0][0]
		content = "fetch" + '^' + filename'''
	cur.execute("DELETE FROM updates WHERE operation_id='"+str(resultset[0][3])+"'")
	db.commit()
	return content

