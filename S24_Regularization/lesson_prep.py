f = open('links.txt', 'r')

for line in f:
    lesson = line.strip()
    lesson = lesson.replace('https://github.com/learn-co-students/','')
    lesson = lesson.replace('.git', '')
    print("lesson<br>")
    link='[lesson](./'+lesson+'/index.ipynb)<br>'
    #[Introduction](./dsc-distributions-section-intro-v2-1-onl01-dtsc-ft-030220/index.ipynb)
    print(link)
    print("\n")

f.close()