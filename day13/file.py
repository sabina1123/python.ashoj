#f=open("hello.txt","r")
#f.write("hello beautiful\n how are you?")
#print(f.read())
# todo:homework
# take input from user to create 
# take input form user tyo file content 
# take input from user  to delete file
import os
from time import sleep
user=input("Enter the file name that you want to create:")
file=open(f"{user}","w")
# file=open(f"j.txt","w")
content=input("Enter content that you want to take:")
file.write(f"{content}")
file.close()
delete=input("Enter the file name that you want to delete:")
sleep(4)
os.remove(f"{delete}")
