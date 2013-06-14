os.chdir('d:\clothe') # 把工作目录更改到需要修改文件名的目录上
i = 1
for file in os.listdir():
	newname = str(i)+'.txt'
	os.rename(file,newname)
	i = i+1