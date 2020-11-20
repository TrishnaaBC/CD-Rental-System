def read(): #defining a function read
    print("---------------------------------------------------------------------")
    print("Movie ID         Movie-Name            Price        Quantity")
    print("---------------------------------------------------------------------")
    #to read the text file named movies
    file=open("films.txt","r")
    b=1
    c={}
    d=1

    #to iterate through each line in the txt file 
    for line in file:
        print(" ",b,"\t\t"+line.replace(",","\t\t"))
        b=b+1

    file1=open("films.txt","r")
    #to iterate through the file 
    for line in file1:
        line=line.replace("\n","")
        e=line.split(",")
        c[d]=e
        d=d+1
    return c
