# -*- coding: utf-8 -*-

def revword(word:str)->str:
    wordlen=len(word)
    tempword=""
    for i in range(1,len(word)+1):
        char=word[wordlen-i]
        tempword=tempword+char
    return tempword.lower()

def countword()->int:
    fhand=open("text.txt",'r')
    words = fhand.read()
    words=words.split() 
    searchword = words[0].lower()
    count=1
    for word in words[1:]:
        if revword(word)==searchword:
            count = count+1
    return count
 
# print(countword())