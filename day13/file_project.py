import os
from time import sleep
user=input("Enter the file name that you want to create:")
#file=open(f"{user}","x")
try:
   file=open(f"{user}","x")
   print("file is not exists......")
except FileExistsError:
    print("File already exists")
content=input("Do you want to put content:")
if content=="yes":
    file=open(f"{user}","a")
    contented=input("Enter content that you want to take:")
    file.write(f"{contented}")
else:
    print("I dont want to add any content in file.")
file.close()
delete=input("do you want too delete?:")
if delete=="yes":
    detete_file=input("Enter the file name that you want to delete:")
    sleep(4)
    os.remove(f"{detete_file}")
else:
    print("I am not interested to delete file ")


