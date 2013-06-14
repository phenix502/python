for file in os.listdir():
	f = codecs.open(file,'r','utf-8')
	text = f.read()
	re.sub(r'\d','',text)
	re.sub(r'"','',text)
	