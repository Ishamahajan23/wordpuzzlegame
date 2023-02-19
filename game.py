print("     ------WORD-PUZZLE-GAME------     \n",)
print("--RULES--")
print("1. User score +1 for each correct answer")
print("2. User score -1 for each wrong answer")
print("3. ANSWER must be written in uppercase")
print("4. Each round of the game only 5 words are shown to the user")

input("\nPRESS ENTER TO CONTINUE..... ")
while True:

#CORRECT WORDS LIST
 l2=["PICTURE","DOLLARS","LUNCH","BICYCLE","BROTHER","YELLOW","MISTAKE","AIRPLANE","GLASS"]
#RANDOM WORD LIST
 l1=["UERICPT","LALORDS","ULHCN","YBICLCE","ETRBOHR","OWLELY","ITSKAEM","PNELARIA","SASGL"]   
 s=set(l1)
 l=len(s)
 result=[]

#POINT FUNCTION 
 def point():
     result.append(input("Enter correct word(ANSWER):"))
     return result
 
 
#STARTING LOOP FOR DISPLAY RANDOM WORDS  

 for e in s:
   if l<=5:
     print("\nArrange the Letters to form a valid word:",e)
     r=point()
   l-=1

 
#COUNTING SCORE DISPLAY LOOP
 x=0
 print("\n----RESULT----\n")
 for e in r:
     if e in l2:
        print("correct")
        x+=1
    
     else:
        print("wrong")
        x-=1
         
 print("Total score out of 5:",x)
 
 choose=input("\nIF YOU WANT TO PLAY AGAIN PRESS y/n:")
 print("\n")
 if choose=='y':
   continue
 else:
   print("\nTHANK YOU FOR PLAYING")
   break
 
