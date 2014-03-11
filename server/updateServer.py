def setDirs(data,db):
	user_content = data.split('^')
	user = user_content[0]
	elements = ("".join(user_content[1:])).split(',')
	print elements
	dirs = {}
	for element in elements:
		element = element.split(':')
		dirs[element[0]] = element[1].replace('$','^')
	#print dirs
	cur = db.cursor()
	cur.execute("SELECT username from linked_folder WHERE username='"+user+"'")
	resultset = cur.fetchall()
	if len(resultset)!=0:
		cur.execute("DELETE FROM linked_folder WHERE username = '"+user+"'")
	for key, val in dirs.items():
		cur.execute("INSERT INTO linked_folder VALUES('"+user+"', '"+key+"', '"+val+"')")
	cur.close()
	db.commit()
	return "ACK"