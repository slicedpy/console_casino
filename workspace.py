with open('script_documentation.txt','wb') as write_document:
    with open('console_horserace_v4.py','rb') as pyscript:
        for each in pyscript:
            if each[0] == '#':
                write_document.write(each.replace('# ','').replace('#',''))
        print "Documentation complete"

    
