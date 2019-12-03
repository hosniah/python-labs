import os 
  
logout = input("Do you wish to log out your computer ? (yes / no): ") 
  
if logout == 'no': 
    os.system("shutdown -t 0 -r -f") 
else: 
    os.system("shutdown -l")