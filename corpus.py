# coding=utf-8   #
import os
import re
import codecs

#更改工作目录
os.chdir('D:/Rcode/LDA/clean')

i = 0

for file in os.listdir('.'):
    raw_file = codecs.open(file,'r','utf-8')
    wellfilename = 'D:/Rcode/LDA/corpus/'+ str(i) + '.txt'
    wellfile = codecs.open(wellfilename, 'w', 'utf-8')
    text = raw_file.read()
    word = re.sub(r'[\d"x]','',text)
    wellfile.write(word)
    raw_file.close()
    wellfile.close()
    i = i + 1
