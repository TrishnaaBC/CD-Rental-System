import datetime #to import datetime function to display the date and time of transaction
X=1

def borrow(): #defining the borrow module
    global X #declaring X as a global variable
    Total=0
    f=""
    g = {}
    now=datetime.datetime.now()
    h=False #assigning h as false to enter into while loop 
    i=False #assigning i as false to enter into while loop 
    while h==False:
        name=input("Enter your name = ")
        try: #to check if the user has input a valid name 
            int(name)
            print("Enter a valid name = ") #to display the message if the user has input a valid name
        except:
            h=True #Assigning h as true to stop the loop 

    while i==False:
        j=False #assigning j as false to enter into while loop 
        while h==True:
            try: 
                film=int(input("Enter the Movie ID you would want to borrow = ")) #to input integer value from the user
                if 1<=film<=10: #to check if the user has input value from 1 to 10
                    h=False #assigning h as false to stop the loop
                else:
                    print("Enter the correct Movie ID.") #to display the message if the user has not input value from 1 to 10
            except:
                print("Enter the valid Movie ID")#to display the message if user has not input integer value

        while h==False:
            try: 
                k=int(input("Quantity of movie you want to borrow =  "))#to take integer input from the user
                h=True #assigning h as true to stop the loop
            except:
                print("Enter a valid value")#to display the message if the user has not input integer value 


        file1=open("films.txt","r") #to open and read the text file named films
        m=1 
        for line in file1: #to iterate through each line in the file 
            line=line.replace("\n","")
            g[m]=line.split(",")
            m=m+1
        o=1
        while o<=10:#to run the loop until the value of o is less than and euals to 10 
            if film==o:#to check if the movie ID the user entered is equals to the value of 1

                p=g[o]
                if int(p[2])<=0:#to check if the quantity of movie available the user wants to rent is less than 0
                    print("Sorry! The movie is out of stock.")#to diplay the message if the quantity of the movie available the user wants to rent is 0
                elif int(p[2])<k:#to check if the quantity of movie available is less than the quantity the user wants to rent 
                    print("There is only",int(p[2]),"movie in stock.")
                else:
                    Price=float(p[1].replace("$",""))*k #to calculate the amount of money for a particular movie
                    Total=Total+Price #to calculate the total amount
                    remaining=int(p[2])-k #to find out the remaining movies left
                    b=1
                    d=""


                    File2=open("films.txt","r")
                    for line in File2: #to iterate through each line in the text file
                        if file1==b:
                            c=line.replace(p[2],str(remaining))#to update the remaining number of movies
                            d=d+c
                    
                        else:
                            d=d+line
                        b=b+1
                    File3=open("films.txt","w") #opening the text file to write 
                    File3.write(d)
               
                    while j==False:
                        s=input("Would you like to borrow more movies?(Y/N) = ")
                        f=f+p[0]+"," #to store all the names of the movies the user rented in f
                        if s.lower()=="n":
                            Bill=open("borrow"+str(X)+".txt","w")#to open a new text file to write                                                                                                      
                            Bill.write(name+","+p[0]+str(now)+","+"$"+str(Total))#to write the name,movies,time and total in the text file 
                            print("-------------------------------------------------")
                            print("Name of borrower = "+name)
                            print("Name of the movie = "+f)
                            print("Total amount = ",Total)
                            print("Time = "+now.strftime("%Y-%M-%D  %H:%M:%S"))
                            j=True #assigning j as true to stop the loop
                            i=True #assigning i as true to stop the loop
                        elif s.lower()=="n":
                            h=True
                            j=True
                            i=False
                        else:
                            print("Enter proper value.")#to print the message if the user has not entered y or n

            X=X+1

            o=o+1

            





            
