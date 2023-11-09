"""import os
from time import sleep
try:
    f=open('arko.txt','x')
    # print(f.readline())
    # f.write("\ni was written from python")
    f.close()
    sleep(4)
    os.remove('arko.txt')
except FileNotFoundError:
    print("File not found")
except FileExistsError:
    print("file already exists")
except Exception as e:
    print("An error occurred",e)"""
    
# todo:homework
# take input from user to create 
# take input form user tyo file content 
# take input from user  to delete file
f=open('hello.txt','r')
print(f.read())
f.close()