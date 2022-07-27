from curses.ascii import isdigit, islower, isupper

def choices():
    print("Please choose your option.")
    choice = int(input("For Signing Up Type 1 and For Signing in Type 2: "))
    if choice == 1:
       return getdetails()
    elif choice == 2:
       return checkdetails()
    else:
       raise TypeError
def getdetails():
    print("Please Provide")
    name = str(input("Name: "))
    password = str(input("Password: "))
    if(len(password)>=5 and len(password)<16):
        if(str(isdigit(password))):
            if(str(isupper(password))):
                if(str(islower(password))):
                 f = open("C:/guvi_projects/project_1_login_validation/User_Data.txt",'r')
                 info = f.read()
                 if name in info:
                  return "Name Unavailable. Please Try Again"
                 f.close()
                 f = open("C:/guvi_projects/project_1_login_validation/User_Data.txt",'w')
                 info = info + " " +name + " " + password
                 f.write(info)
    else:
     print("Please enter valid password");
     print("done"); 


def checkdetails():
    print("Please Provide")
    name = str(input("Name: "))
    password = str(input("Password: "))
    f = open("C:/guvi_projects/project_1_login_validation/User_Data.txt",'r')
    info = f.read()
    info = info.split()
    if name in info:
        index = info.index(name) + 1
        usr_password = info[index]
        if usr_password == password:
            return "Welcome Back, " + name
        else:
            return "Password entered is wrong"
    else:
        return "Name not found. Please Sign Up."
print(choices())