f = open('links.txt', 'r')

for line in f:
     #https://github.com/learn-co-students/dsc-linalg-introduction-onl01-dtsc-ft-030220
     lesson = line.strip()
     lesson = lesson.replace('https://github.com/learn-co-students/','')
     lesson = lesson.replace('.git', '')

     name = lesson
     name = name.replace('dsc-', '')
     name = name.replace('-onl01-dtsc-ft-030220', '')
     
     #print(name, "<br>")
     link='['+name+'](./'+lesson+'/index.ipynb)<br>'
     print(link)
     print("\n")
	 
f.close()