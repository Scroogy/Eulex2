""" This file contains the main algorithm
None of the functions in this file have been tested yet but there are no syntax errors.

"""

vowels = ['a', 'e', 'i', 'o', 'u']
twoStrings=['sh','wh','th','ch','cr','ss','ck', 'di', 'lk', 'bl'];
threeStrings=['rkn','thn','thw','chn','shn','rdm','lkm'];
neverSplit=['tch'];
vowelSplit=['ing','ate'];
pSymbols = [',', '.', '\''];



def indexOf(s,v,index):
   for i in range(index, len(s)):
      if(s[i] == v):
         return i
   return -1

def isVowel(ch, low, high):
   mid = (low+high)/2
   if(vowels[mid] == ch): return True
   elif(vowels[mid] < ch): return isVowel(ch,mid+1,high)
   else: return isVowel(ch,0,mid-1)


def subStr(s,a,index):
   for i in range(0,len(a),1):
      find = indexOf(s,a[i],index)
   if(find == index): 
      return True
   return False

def getSyllable(s): 
    s=s.lower()
    s=s.split(".")[0]
    print s
    x=s.split("")
    vMask=[]
    firstV=-1		   
    firstC=-1
    # mark vowels with vMask=1, remember the first Vowel index in firstV
    for i in range(0,len(x),1):
       if isVowel(x[i]) == True: 
          vMask[i]=1
	  if (firstV==-1): firstV=i                  
       else: 
          vMask[i]=0
	  if (firstC==-1): firstC=i
				    
    # rules 1 and 2
   # process maximal vowels stretches sandwiched by consonants
    pC=firstC
    for i in range(0,len(vMask),1):
	if (vMask[i]==0) and (i-pC>1):
          if(i-pC-1 == 3):
             vMask[i-2] = 2
             break
          elif(i-pC-1 == subStr(s,vowelSplit,i-1)):
             vMask[i-1] = 2
             break	
        if vMask[i]==0: pC=i


    # rules 4, 5 and 6
    # process maximal consonant stretches sandwiched by vowels
    pV=firstV
    for i in range(0,len(vMask),1):
	if (vMask[i]==1) and (i-pV>1):
          temp = i - pV - 1
          if(temp == 1): 
             vMask[i-1] = 2
             break
          elif(temp == 2):
             if(not subStr(s,twoStrings,i-2)):
                vMask[i-1]=2
             else:
                vMask[i-2]=2
             break
          elif(temp == 3):
             if(subStr(s,threeStrings,i-3)): vMask[i-1]=2
             else:
                if(subStr(s,neverSplit,i-3)): vMask[i-3]=2
                else: vMask[i-2]=2
             break
          else:
             vMask[pV+3] = 2
             break
        if(vMask[i]==1): pV=i
   

    # rule 7
    i=len(vMask)-1
    while(i>=0):
       if(vMask[i] == 2): break
       i=i-1

    if ((i==vMask.length-2) and (not isVowel(x[i])) and (isVowel(x[i-1])) and (x[i+1]=='e')): vMask[i]=1

    print vMask
   
    string = ""
    
    for i in range(0,len(vMask),1):
       if(vMask[i] == 2 and i!=0): string = string + "-" 
       string = string + str(x[i])

    return string


def main():
   print "No errors"

if __name__ == '__main__':
   main()
