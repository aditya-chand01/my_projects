print("WELCOME TO BINARY MANAGEMENT PROGRAM")
while True:
    print("press.....")
    print("1.create")
    print("2.append")
    print("3.update")
    print("4.display")

    x=int(input(""))
    def createfile():
        import pickle
        with open('abc123.txt','wb') as f1:
            d1={}
            while True:
                rn=int(input("enter the roll no."))
                name=input("enter the name")
                marks=int(input("enter marks"))
                d1['rn']=rn
                d1['name']=name
                d1['marks']=marks
                pickle.dump(d1,f1)
                chr=input("enter y or Y to continue")
                if chr not in['y','Y']:
                    break
    def appendf():
        import pickle
        with open('abc123.txt','ab') as f1:
            d1={}
            while True:
                rn=int(input("enter roll no."))
                name=input("enter the name")
                marks=int(input("enter marks"))
                d1['rn']=rn
                d1['name']=name
                d1['marks']=marks
                pickle.dump(d1,f1)
                chr=input("enter y or Y to continue")
                if chr not in['y','Y']:
                    break
    def updatef():
        import pickle
        try:
            with open('abc123.txt','rb+') as f1:
                d1={}
                rn=int(input('enter the roll no. to update'))
                while True:
                    cpos=f1.tell()
                    d1=pickle.load(f1)
                    if(rn==d1['rn']):
                        d1['marks']+=10
                        f1.seek(cpos)
                        pickle.dump(d1,f1)
        except EOFError:
            print("EOF reached")

    def displayf():
        import pickle
        try:
            with open('abc123.txt','rb') as f1:
                d1={}
                while True:
                    d1=pickle.load(f1)
                    print(d1)
        except EOFError:
            print("EOF reached")
    if x==1:
        createfile()
    if x==2:
        appendf()
    if x==3:
        updatef()
    if x==4:
        displayf()
    bv=input("if you want to carry on press 00")
    if bv=='00':
        continue
    else:
        break
    
