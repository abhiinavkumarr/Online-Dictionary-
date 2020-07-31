import json
from difflib import get_close_matches

data=json.load(open("data.json","r"))

def translate(w):
   w=w.lower()
   if w in data:
      return data[w]
   elif w.title() in data:
      return data[w.title()]
   elif w.upper() in data:
      return data[w.upper()]
   elif len(get_close_matches(w,data.keys()))>0:
      yn=input("did u mean %s instead? enter Y if yes and N if no:" % get_close_matches(w,data.keys())[0] )
      if yn=="Y" or yn=="y":
         return data[get_close_matches(w,data.keys())[0]]
      elif yn=="N" or yn=="n":
         return "the word dont exist."
      else:
         return "we dont get your choice."
   else:
       return "the word dont exist.Please double check it."
t=1
while(t==1):
   word=input("enter word: ")
   output=translate(word)
   if type(output)== list:
        for i in output:
            print(i)
   else:
       print(output)
   t=int(input("press 1 to continue or press any other key to exit"))
if t!=1:
   print("*** program ends ***")
