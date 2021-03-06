#Run this prior to starting the exercise
from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))


genFiles(memReg,exReg)

# Here starts the magic
removed_members = []
active_members = ""

with open("members.txt", "r") as readFile:
        with open("inactive.txt", "a") as testwritefile:
            Lines = readFile.readlines()
            line = 1
            for line in Lines:
                if line != 1:
                    if line.find("no") != -1:
                        testwritefile.write(line)
                        removed_members.append(line)
                    else:
                        active_members = (active_members + line)

with open("members.txt", "w") as writefile:
    writefile.write(active_members)



# Code to help you see the files
# Leave as is
memReg = 'members.txt'
exReg = 'inactive.txt'
#cleanFiles(memReg,exReg)


headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
                