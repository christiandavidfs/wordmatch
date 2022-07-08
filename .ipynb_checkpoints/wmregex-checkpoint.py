 
import re

matches=[]
str = input()
my_list = []


def load_file():
    #Load the words from the file

    with open("File1.txt") as file:
        for l in file:
            my_list.append(l.strip())


def matching():

    joined_string = "|".join(my_list)
    matches=re.findall(''.join(joined_string), str, re.IGNORECASE)
    #print[matches]
    a=matches
    b=my_list
    
    #everything to Lowercase
    a= [x.lower() for x in my_list]

    #a=my_list
    b= [x.lower() for x in matches]
    
    print (set(a) == set(b) and len(a) == len(b))
    
load_file()
matching()