import datetime #importing datetime function to display the date and time
X=1
def returnmovie(): #defining a function returnmovie 
    global X #declaring X as the global variable 
    now=datetime.datetime.now() 
    h=False #assigning h as false to enter the while loop
    i=False #assigning i as false to enter the while loop
    f=""
    d={}
    days=10 #declaring maximum number of days a user can rent a movie without paying fine 
    fine=1 #fine per day
    total_fine=0 #total amount of fine 
    while h==False:
        name=input("Enter your name = ")
        try: #to check if the user has input a valid name
            int(name)
            print("Enter a valid name.")#to print the message if the user has not entered a valid name 
        except:
            h=True #assigning h as true to stop the loop

    while i==False:
        j=False #assigning j as false to enter into while loop
        while h==True:
            try: 
                film=int(input("Enter the movie ID = "))#to take integer input from the user
                if 1<=film<=10: #to check if the user has input value from 1 to 10
                    h=False #assigning h as false to stop the loop
                else:
                    print("Enter the correct Movie ID.")#to print the message if the user has not input value from 1 to 10 
            except:
                print("Enter the valid Movie ID.")#to print the message if the user has not input integer value

        while h==False:
            try: 
                k=int(input("Quantity of movie you would like to return = "))#to take integer input from the user 
                h=True #assigning h as true to stop the loop
            except:
                print("Enter the valid value.")

        file1=open("films.txt","r") #to open and read the file named films
        m=1
        for line in file1: #to iterate through each line in the text file 
            line=line.replace("\n","")
            d[m]=line.split(",")
            m=m+1

        o=1
        while o<=10:
            if film==o: #to check if the movie ID the user entered if equals to the value of o
                p=d[o]
                remaining=int(p[2])+k #to calculate the amount of movies after the user has returned
                b=""
                s=1

                File2=open("films.txt","r")
                for line in File2:
                    if film==b:
                        c=line.replace(p[2],str(remaining))#to update the total number of movies after the user has returned
                        b=b+c
                    else:
                        b=b+line
                        s=s+1
                File3=open("films.txt","w") #to open the text file to write
                File3.write(b)

                t=int(input("The number of days you borrowed this movie for = "))#to take integer input from the user
                if t>days: #to check if the user has rented the movie for more than 10 days
                    v=t-days #to calculate the extra number of days the user has rented the movie for
                    total_fine = ((fine)*(v))#to calculate the total fine for the extra number of days
                    print("Dear customer, since you are",v,"days late, you will have to pay a fine of $",total_fine)#to print out the messagde for the fine
                else:
                    print("Thank you for returning the CD in time")

                while j==False:
                    s=input("Would you like to return any more movies?(Y/N): ")
                    f=f+p[0]+","
                    if s.lower()=="n":
                        print("Name of the person returning the movie = "+name)
                        print("Movie ID: ",film)
                        print("Name of the movie = "+f)
                        print("Movie quantity: ",k)
                        print("Time = "+now.strftime("%Y-%M-%D  %H:%M:%S"))
                        Return=open("Return"+str(X)+".txt","w") #to open a new text file to write
                        Return.write(name+","+p[0]+","+str(now)+",") #to write the name,movies and time in the teaxt file 
                        j=True #assigning j as true to stop the loop
                        i=True #assigning i as true to stop the loop
                    elif s.lower()=="c":
                        j=True
                        i=False
                        h=True
                    else:
                        print("Enter the proper value.") #to print the message if the user has not entered y or n
            X=X+1
            o=o+1
            
