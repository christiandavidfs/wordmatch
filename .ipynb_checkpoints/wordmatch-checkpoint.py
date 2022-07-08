
#Type the sentence to be evaluated

str = input()
my_list = []

def load_file():
    #Load the words from the file

    with open("File1.txt") as file:
        for l in file:
            my_list.append(l.strip())

def matching():

    #everything to Lowercase
    a= [x.lower() for x in my_list]

    #a=my_list
    sentence=str.lower()


    #review matches
    fullmatch= [x for x in a if x in sentence]

    #save matches to variable
    b=fullmatch
    # print(my_list)
    #print(b)

    #assert if matches match words and length
    print (set(a) == set(b) and len(a) == len(b))


load_file()
matching()