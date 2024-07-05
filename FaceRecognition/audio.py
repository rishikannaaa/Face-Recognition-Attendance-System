import pyttsx3
#import pywintypes

text = pyttsx3.init()
voices=text.getProperty('voices')
text.setProperty('voice',voices[1].id)
text.setProperty('rate',200)
db = "nfd"                                   # db =data base , fd= found or nfd = not found
sts = "out"                                  # sts = status , in or out for attendance
name = "  miss soaniga   ,"                       # name of the person in db

def audio(pl):
    
    text.say(pl)
    text.runAndWait()


    
if (db == "fd") & (sts == "in"):                                 # in attendancde
  
   
   a= "welcome to mor cube ,   "+ name
   b ="   you'  attendance  was  registered ,   successfully,"
   f = a+b
  
   audio(f)
   
elif (db == "fd" ) & (sts == "out") :                              # out attendancde
   
     c="hello , "+ name 
     d="   you'r attendance  was  closed successfully , keep  rock  with, mor cube"
     f= c+d
     audio(f)
     
else :                                                               # an unautharised person
 
  f="thank  you for  visiting , mor cube , yor data is not found .  pleace contect with admin"
  audio(f)   
