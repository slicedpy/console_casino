def docEngine(pyfile,docName="script_documentation.txt"):
    with open(docName,'wb') as write_document:
        with open(pyfile,'rb') as pyscript:
            for each in pyscript:
                if each[0] == '#':
                    write_document.write(each.replace('# ','').replace('#',''))
            print "Documentation complete"
            print "Script Source: " + pyfile
            print "File name: " + docName
            print "Made by: docEngine"

        write_document.write("\nScript Source: " + pyfile + "\nFile name: " + docName + "\nMade by: docEngine")

docEngine('console_horserace_v4.py','script_dcoumentation.txt')


    
