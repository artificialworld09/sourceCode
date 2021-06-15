import googletrans

l=googletrans.LANGUAGES
for i in l:
  print(f'{i} - {l[i]}')
  
  
  
#string='how are you?'

#gt=googletrans.Translator()
#text=gt.translate(string,dest='hi')
##text=gt.translate(string, dest='hi', src='en')
#data=text.text
#print(data)
