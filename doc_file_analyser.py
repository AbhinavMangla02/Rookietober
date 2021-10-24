ch=input('1. Count the frequency of a word\n2. Search for a line stating with a word/character\n3. Input data in the text file\n4. exit\n\nchoice: ')

if ch=='1':
    with open('data.txt','r') as file:
        contents=file.read()
    wordlist=contents.split()
    wordfreq=[]
    high=0
    word=''
    existing=[]
    for w in wordlist:
        wcount=wordlist.count(w)
        if w not in existing:
            wordfreq.append([w,wcount])
            existing.append(w)
        if wcount>high:
            high=wcount
            word=w
    print('The word'+word+'occurs maximum number of time',high,'times.')
    print('\nother words have the frequencies:')
    print(wordfreq)
    file.close()

elif ch=='2':
    char=input('Character/word to search for: ')
    def display():
        file=open('data.txt','r')
        line=file.readline()
        while line:
            if line[0]==char:
                print(line)
            line=file.readline()
        file.close()
        
elif ch=='3':
    with open('data.txt','w') as file:
        n=int(input('No. of lines in the file: '))
        for i in range(n):
            data=input('>>> ')
            file.write(data)
        file.close()

elif ch=='4':
    file= open("data.txt", "r")
    t=file.read()
    v=0
    for ch in t:
        if ch in ['a','e','i','o','u','A','E','I','O','U']:
            v+=1
        else:
            pass
    file.close()
    print('Count of vowels: ',v)

elif ch=='5':
    file= open("data.txt", "r")
    t=file.read()
    c=0
    for ch in t:
        if ch not in ['a','e','i','o','u','A','E','I','O','U']:
            c+=1
        else:
            pass
    file.close()
    print('Count of consonants: ',c)
        
elif ch=='8':
    exit()
    
else:
    print('Invalid input!')
    pass
