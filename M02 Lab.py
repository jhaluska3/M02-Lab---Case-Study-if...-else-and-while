#Jakob Haluska
#M02 Lab
#This app will accept student's last name, if it is not "ZZZ" then the program will ask for first name and GPA. If GPA >= 3.5 the student makes the deans list, GPA >= 3.25  
#the student makes the honor roll. The name will be printed with their achievement

lastName=input("Please enter student's last name (Enter ZZZ to quit): ") #last name input
while lastName != "ZZZ": #loop checking for "ZZZ"

    firstName=input("Please enter student's first name: ") # first name
    GPA = float(input("Please enter student's GPA: ")) #GPA
    if GPA >= 3.5: #checking for deans list
        print (firstName, lastName, "has made the Dean's List.")
    
    else:
        if GPA >= 3.25:#checking for honor roll
            print (firstName, lastName, "has made the Honor Roll.")
    
    lastName=input("Please enter student's last name (Enter ZZZ to quit):")# taking new last name to restart loop
