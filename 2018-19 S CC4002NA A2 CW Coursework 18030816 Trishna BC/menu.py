#initializing menu as continue to enter into while loop
menu="continue"
while menu=="continue":
    #to import read function from read module
    import read
    read.read()
    print("-------------------------------------------------------------------")
    #to let the user to choose any option
    print("Choose any option : ")
    print("Enter 1 to borrow CD : ")
    print("Enter 2 to return CD :")
    print("Enter 3 to exit : \n")
    #to assign x as discontinue to enter into while loop
    x="discontinue" 
    while x=="discontinue":
        try:
            a=int(input()) #to take input from the user and to check if the user has input integer value or not 
            x="continue" #to assign x as continue to stop the loop
        except:
            print("Please enter valid number.")
    if a==1:
        print("Borrow a CD")
        import borrow #to import borrow function from borrow module
        borrow.borrow()
    elif a==2:
        print("Return a CD")
        import returnmovie #to import returnmovie function from returnmovie module
        returnmovie.returnmovie()
        
        
    elif a==3:
        print("Thank you for using CD rental system.")
        menu="discontinue" #to stop the loop and exit the program
    else:
        print("Please enter 1, 2 or 3")
