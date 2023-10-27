import mysql.connector as mq

def database():             #Creating MySQL DataBase..
    con=mq.connect(host='localhost',user='root',passwd='root')
    cur=con.cursor()
    cur.execute("create database if not exists office;")
    con.commit()
    con.close()
    con=mq.connect(host='localhost',user='root',passwd='root',database='office')
    cur=con.cursor()
    cur.execute("create table if not exists employee(name varchar(20),age int,phno char(10),aadhar char(12),addr varchar(100))")
    cur.execute("create table if not exists passwd(password char(30));")
    cur.execute("insert into passwd(password) values('root') ;") #Giving a Default Password for later use..
    con.commit()
    con.close()

def menutext():           #Text to show up on Menu
    print("\n\t\t\t Employee Management System\n\t\t\t ======================\n\n\t\t\t\t Main Menu\n\t\t\t\t ========")
    print('''\t\t1. Add an Employee\n\t\t2. Employee Details\n\t\t3. Update Info\n\t\t4. Support\n\t\t5. Exit\n''')

def registration():     #Registering a New User
    print("\n\t\t\tRegistering New Employee\n\t\t\t====================")
    nam=input("\nEnter the Name : ")                                 #Taking Name from the User
    while not (all(x.isalpha() or x.isspace() for x in nam) and nam!=""):
        nam=input("Please Enter  a Valid Name : ")
    nam=nam.capitalize()
    ph=input("Please enter your 10 Digit Phone Number : ")#Taking Phone Number from User
    while not (len(ph)==10 and ph.isdigit()):
        if not ph.isdigit():
            print("Sorry I didn't Understand that...")
        ph=input("Enter a Valid Phone Number of 10 digits : ")
    aadhar=input("Please enter your 12 Digit Aadhar Number : ")#Taking Aadhar Number from User
    while not (len(aadhar)==12 and aadhar.isdigit()):
        if not aadhar.isdigit():
            print("Sorry I didn't Understand that...")
        aadhar=input("Enter a Valid Aadhar Number of 12 digits : ")
    age=input("Please Enter The Age: ")                                      #Taking Age from User
    while True:
        if age.isdigit():
            if int(age)<100:
                break
        else:
            print("Sorry I didn't Understand that...")
        age=input("Please Enter a Valid Age: ")
    add=input("Enter the Address : ")                                          #Taking Address from User
    while add=="":
        add=input("Please Enter a Valid Address : ")
    con=mq.connect(host='localhost',user='root',passwd='root',database='office')#Starting The MySQL connection
    cur=con.cursor()
    query="insert into employee(phno,name,addr,aadhar,age) values ('{}','{}','{}','{}',{})".format(ph,nam,add,aadhar,age)
    cur.execute(query)                                                                         # Uploading the Above Data Taken from the User to Database
    print("\nRegistration Successfull....")
    print('New Employee Details....')
    query="select * from employee where  phno='{}'".format(ph) #Showing the Details of Newly Registered Employee
    cur.execute(query)
    res=cur.fetchall()
    b=res[0]
    print("--------------------------------------------------------------------------------------------------------------")
    print(": Name                : Age : Phone Number : Aadhar Number : Address                                : ")
    print("--------------------------------------------------------------------------------------------------------------")
    print(": ",b[0]," "*(19-len(b[0])),": ",b[1]," "*0,": ",b[2]," "*(13-len(b[2])),": ",b[3]," "*(14-len(b[3])),": ",b[4]," "*(43-len(b[3])),":")
    print("--------------------------------------------------------------------------------------------------------------\n")
    con.commit()
    con.close()       #Closing The DataBase
    k=input('''1. Go Home\n2. Go Back\n3. Register Another Employee\nAny Other key to exit...\nEnter Your Choice : ''')
    try:                                #Creating an User Friendly Interface like Going Back or Home or to any other  Function
        a=int(k)
        if a==1:
            menu()
        elif a==2:
            register()
        elif a==3:
            registration()
        else:
            exit()
    except:
        exit()

def register():
    print("\n\t\t\tNew Employee Registration\n\t\t\t====================")
    print("\n\t\t1. Register An Employee\n\t\t2. Go Back [Home]\n\n")
    ch=input("Enter Your Choice [1-2] : ")
    while not(ch.isdigit() and (int(ch)==1 or int(ch)==2)):
        print("Sorry I didn't Understand that...")
        ch=input("Enter Your Choice [1-2] : ")
    ch=int(ch) 
    if ch==1:
        registration()
    elif ch==2:
        menu()
    else:
        print("Enter a Valid Option")

def search():
    print("\n\t\t\tSearch Employee\n\t\t\t=============")
    ph=input("Please enter your 10 Digit Phone Number : ")
    while not (len(ph)==10 and ph.isdigit()):
        if not ph.isdigit():
            print("Sorry I didn't Understand that...")
        ph=input("Enter a Valid Phone Number of 10 digits : ")
    con=mq.connect(host='localhost',user='root',passwd='root',database='office')
    cur=con.cursor()
    query="select * from employee where  phno='{}'".format(ph)
    cur.execute(query)
    res=cur.fetchall()
    if res==[]:
        print("\nEmployee Doesn't Exist.....")
        k=input('''\n1. Search Again\n2. Go Back\n3. Home\nAny Other key to exit...\nEnter Your Choice : ''')
        try:
            a=int(k)
            if a==1:
                search()
            elif a==2:
                employeedetails()
            elif a==3:
                menu()
            else:
                exit()
        except:
            exit()
    else:
        b=res[0]
        print("--------------------------------------------------------------------------------------------------------------")
        print(": Name                : Age : Phone Number : Aadhar Number : Address                                : ")
        print("--------------------------------------------------------------------------------------------------------------")
        print(": ",b[0]," "*(19-len(b[0])),": ",b[1]," "*0,": ",b[2]," "*(13-len(b[2])),": ",b[3]," "*(14-len(b[3])),": ",b[4]," "*(43-len(b[3])),":")
        print("--------------------------------------------------------------------------------------------------------------\n")
        con.close()
        k=input('''1. Go Home\n2. Go Back\n3. Search for another Employee\nAny Other key to exit...\nEnter Your Choice : ''')
        try:
            a=int(k)
            if a==1:
                menu()
            elif a==2:
                employeedetails()
            elif a==3:
                search()
            else:
                exit()
        except:
            exit()

def searchall():
    print("\n\t\t\tDetails of Every Employee\n\t\t\t===================")
    con=mq.connect(host='localhost',user='root',passwd='root',database='office')
    cur=con.cursor()
    query="select * from passwd"
    cur.execute(query)
    res=cur.fetchone()
    passwd=res[0]
    password=input("Enter the Password : ")
    if password==passwd:
        con=mq.connect(host='localhost',user='root',passwd='root',database='office')
        cur=con.cursor()
        query="select * from employee; "
        cur.execute(query)
        res=cur.fetchall()
        n=len(res)
        if res==[]:
            print("\nThere are No Employees in the Database.....")
            k=input('''\n1. Go Back\n2. Go Home\nAny Other key to exit...\nEnter Your Choice : ''')
            try:
                a=int(k)
                if a==1:
                    employeedetails()
                elif a==2:
                    menu()
                else:
                    exit()
            except:
                exit()
        else:
            print("--------------------------------------------------------------------------------------------------------------")
            print(": Name                : Age : Phone Number : Aadhar Number : Address                                  : ")
            print("--------------------------------------------------------------------------------------------------------------")
            for l in range (n):
                k=res[l]
                print(": ",k[0]," "*(19-len(k[0])),": ",k[1]," "*0,": ",k[2]," "*(13-len(k[2])),": ",k[3]," "*(14-len(k[3])),": ",k[4]," "*(34-len(k[4])),":")
            print("--------------------------------------------------------------------------------------------------------------\n")
        con.close()
        k=input('''\n1. Go Home\n2. Go Back\nAny Other key to exit...\nEnter Your Choice : \n''')
        try:
            a=int(k)
            if a==1:
                menu()
            elif a==2:
                viewall()
            else:
                exit()
        except:
            exit()
    else:
        print("The Password you Entered is Incorrect..")
        k=input('''\n1. Enter Password Again\n2. Go Back\n3. Go Home\nAny Other key to exit...\nEnter Your Choice : ''')
        try:
            a=int(k)
            if a==1:
                searchall()
            elif a==2:
                viewall()
            elif a==3:
                menu()
            else:
                exit()
        except:
            exit()

def changepasswd():
    print("\n\t\t\tChanging Password\n\t\t\t==============")
    password=input("Enter the Current Password : ")
    con=mq.connect(host='localhost',user='root',passwd='root',database='office')
    cur=con.cursor()
    query="select * from passwd"
    cur.execute(query)
    res=cur.fetchall()
    a=res[0]
    passwd=a[0]
    if password==passwd:
        a=input("Enter Your New Password : ")
        b=input("Re-enter Your New Password : ")
        if a==b:
            con=mq.connect(host='localhost',user='root',passwd='root',database='office')
            cur=con.cursor()
            query="update passwd set password='{}';".format(a)
            cur.execute(query)
            query="delete from passwd where password!='{}';".format(a)
            cur.execute(query)
            con.commit()
            con.close()
            print("Password Changed Successfully....")
            k=input('''\n1. Go Home\n2. Go Back\n3. Change Password Again\nAny Other key to exit...\nEnter Your Choice : ''')
            try:
                a=int(k)
                if a==1:
                    menu()
                elif a==2:
                    viewall()
                elif a==3:
                    changepasswd()
                else:
                    exit()
            except:
                exit()
        else:
            print("The Password You Entered Second Time is not the same as The First One....")
            k=input('''\n1. Try Again\n2. Go Back\n3. Go Home\nAny Other key to exit...\nEnter Your Choice : ''')
            try:
                a=int(k)
                if a==1:
                    changepasswd()
                elif a==2:
                    viewall()
                elif a==3:
                    menu()
                else:
                    exit()
            except:
                exit()
    else:
        print("The Password You Entered is Incorrect...")
        k=input('''\n1. Enter Password Again\n2. Go Back\n3. Go Home\nAny Other key to exit...\nEnter Your Choice : ''')
        try:
            a=int(k)
            if a==1:
                changepasswd()
            elif a==2:
                viewall()
            elif a==3:
                menu()
            else:
                exit()
        except:
            exit()

def modify():   
    print("\n\t\t\tUpdate Employee Info\n\t\t\t================")
    ph=input("Please enter your 10 Digit Phone Number : ")#Taking Phone Number from User
    while not (len(ph)==10 and ph.isdigit()):
        if not ph.isdigit():
            print("Sorry I didn't Understand that...")
        ph=input("Enter a Valid Phone Number of 10 digits : ")
    modify.a=ph
    con=mq.connect(host='localhost',user='root',passwd='root',database='office')
    cur=con.cursor()
    query="select * from employee where  phno='{}'".format(ph)
    cur.execute(query)
    res=cur.fetchall()
    if res==[]:
        print("\nEmployee Doesn't Exist.....\n")
        k=input('''\n1. Search Again\n2. Go Home\n3. Go Back\nAny Other key to exit...\nEnter Your Choice : ''')
        try:
            a=int(k)
            if a==1:
                modify()
            elif a==2:
                menu()
            elif a==3:
                update()
            else:
                exit()
        except:
            exit()
    else:
        modify1()
    con.close()
    
def modify1():
    ph=modify.a
    con=mq.connect(host='localhost',user='root',passwd='root',database='office')
    cur=con.cursor()
    print("\n\t\t\tUpdate Employee Info\n\t\t\t================")
    print("\n1. Name\n2. Address\n3. Aadhar No\n4. Phone Number\n5. Age\n6. Go Back\n")
    ch=input("Choose the Option you want to Update or Press 6 to 'Go Back' [1-6] : ")
    while not(ch.isdigit() and (int(ch)==1 or int(ch)==2 or int(ch)==3 or int(ch)==4 or int(ch)==5 or int(ch)==6)):
        print("Sorry I didn't Understand that...\n")
        ch=input("Choose the Option you want to Update or Press 6 to 'Go Back' [1-6] : ")
    ch=int(ch) 
    if ch==1 :
        nam=input("\nEnter The New Name to Update : ")
        while not (all(x.isalpha() or x.isspace() for x in nam) and nam!=""):
            nam=input("Please Enter a Valid Name to Update : ")
        nam=nam.capitalize()
        query="select name from employee where  phno='{}'".format(ph)
        cur.execute(query)
        res=cur.fetchall()
        res=res[0]
        res=res[0]
        query="update employee set name='{}' where phno='{}'".format(nam,ph)
        cur.execute(query)
        con.commit()
        print("Successfully Updated the Name......\n ",)
        print("Your Old Name is ",'"',res,'"')
        print("Your New Name is ",'"',nam,'"')
        k=input('''\n1. Go Home\n2. Go Back\nAny Other key to exit...\nEnter Your Choice : ''')
        try:
            a=int(k)
            if a==1:
                menu()
            elif a==2:
                modify1()
            else:
                exit()
        except:
            exit()
    elif ch==2:
        add=input("\nEnter The New Address to Update : ")
        while not add!="":
            add=input("Please Enter a Valid Address : ")
        add=add.capitalize()
        query="select addr from employee where  phno='{}'".format(ph)
        cur.execute(query)
        res=cur.fetchall()
        res=res[0]
        res=res[0]                
        query="update employee set addr='{}' where phno='{}'".format(add,ph)
        cur.execute(query)
        con.commit()
        print("Successfully Updated the Address......\n")
        print("Your Old Address is ",'"',res,'"')
        print("Your New Address is ",'"',add,'"')
        k=input('''\n1. Go Home\n2. Go Back\nAny Other key to exit...\nEnter Your Choice : ''')
        try:
            a=int(k)
            if a==1:
                menu()
            elif a==2:
                modify1()
            else:
                exit()
        except:
            exit()
    elif ch==3:
        aadhar=input("Please Enter the New 12 digit Aadhar Number : ")
        while not (aadhar.isdigit() and len(aadhar)==12):
            if not aadhar.isdigit():
                print("Sorry I didn't understand that....")
            aadhar=input("Please Enter a Valid Aadhar Number : ")
        query="select aadhar from employee where  phno='{}'".format(ph)
        cur.execute(query)
        res=cur.fetchall()
        res=res[0]
        res=res[0]
        query="update employee set aadhar='{}' where phno='{}'".format(aadhar,ph)
        cur.execute(query)
        con.commit()
        print("Successfully Updated the Aadhar Number......\n")
        print("Your Old Aadhar Number is ",'"',res,'"')
        print("Your New Aadhar Number is ",'"',aadhar,'"')
        k=input('''\n1. Go Home\n2. Go Back\nAny Other key to exit...\nEnter Your Choice : ''')
        try:
            a=int(k)
            if a==1:
                menu()
            elif a==2:
                modify1()
            else:
                exit()
        except:
            exit()
    elif ch==4:
        ph1=input("\nEnter New Phone Number to Update : ")#Taking Phone Number from User
        while not (len(ph1)==10 and ph1.isdigit()):
            if not ph1.isdigit():
                print("Sorry I didn't Understand that...")
            ph1=input("Please Enter a Valid Phone Number of 10 digits : ")
        query="select phno from employee where  phno='{}'".format(ph)
        cur.execute(query)
        res=cur.fetchall()
        res=res[0]
        res=res[0]
        query="update employee set phno='{}' where phno='{}'".format(ph1,ph)
        cur.execute(query)
        con.commit()
        print("Successfully Updated the Phone Number......\n")
        print("Your Old Phone Number is ",'"',res,'"')
        print("Your New Phone Number is ",'"',ph1,'"')
        k=input('''\n1. Go Home\n2. Go Back\nAny Other key to exit...\nEnter Your Choice : ''')
        try:
            a=int(k)
            if a==1:
                menu()
            elif a==2:
                modify1()
            else:
                exit()
        except:
            exit()
    elif ch==5:
        age=input("Please Enter The Age: ")                                      #Taking Age from User
        while True:
            if age.isdigit():
                if int(age)<100:
                    break
            else:
                print("Sorry I didn't Understand that...")
            age=input("Please Enter a Valid Age: ")
        query="select age from employee where  phno='{}'".format(ph)
        cur.execute(query)
        res=cur.fetchall()
        res=res[0]
        res=res[0]
        query="update employee set age={} where phno='{}'".format(age,ph)
        cur.execute(query)
        con.commit()
        print("Successfully Updated the Age......")
        print("Your Old Age is ",'"',res,'"')
        print("New Age is ",'"',age,'"')
        k=input('''\n1. Go Home\n2. Go Back\nAny Other key to exit...\nEnter Your Choice : ''')
        try:
            a=int(k)
            if a==1:
                menu()
            elif a==2:
                modify1()
            else:
                exit()
        except:
            exit()
    else :
        update()
        
def remove() :
    print("\n\t\t\tRemove The Employee")
    print("\t\t\t===============")
    ph=input("\nPlease Enter the 10 digits phone number to Remove the Employee : ") #Taking Phone Number from User
    while not (len(ph)==10 and ph.isdigit()):
        if not ph.isdigit():
            print("Sorry I didn't Understand that...")
        ph=input("Enter a Valid Phone Number of 10 digits : ")
    con=mq.connect(host='localhost',user='root',passwd='root',database='office')
    cur=con.cursor()
    query="select * from employee where  phno='{}'".format(ph)
    cur.execute(query)
    res=cur.fetchall()
    if res==[]:
        print("\nEmployee Doesn't Exist.....")
        k=input('''\n1. Search Again\n2. Go Back\n3. Go Home\nAny Other key to exit...\nEnter Your Choice : ''')
        try:
            a=int(k)
            if a==1:
                remove()
            elif a==2:
                update()
            elif a==3:
                menu()
            else:
                exit()
        except:
            exit()
    else:
        b=res[0]
        print("\n--------------------------------------------------------------------------------------------------------------")
        print(": Name                : Age : Phone Number : Aadhar Number : Address                                : ")
        print("--------------------------------------------------------------------------------------------------------------")
        print(": ",b[0]," "*(19-len(b[0])),": ",b[1]," "*0,": ",b[2]," "*(13-len(b[2])),": ",b[3]," "*(14-len(b[3])),": ",b[4]," "*(43-len(b[3])),":")
        print("--------------------------------------------------------------------------------------------------------------\n")
        a,b="Yy","Nn"
        ch=input("Are you Sure to delete the Employee..... [Y/N] : ")
        while not ((ch in a or ch in b) and ch!="" ):
            print("Please Enter a Valid Option....")
            ch=input("Are you Sure to delete the Employee..... [Y/N] : ")
        if ch in a:
            query="delete from employee where phno='{}'".format(ph)
            cur.execute(query)
            con.commit()
            con.close()
            print("\nSuccessfully Removed The Employee.....\n")
            k=input('''\n1. Remove Another Employee\n2. Go Home\n3. Go Back\nAny Other key to exit...\nEnter Your Choice : ''')
            try:
                a=int(k)
                if a==1:
                    remove()
                elif a==2:
                    menu()
                elif a==3:
                    update()
                else:
                    exit()
            except:
                exit()
        else :
            print("\nNo Changes made...\n")
            k=input('''\n1. Remove Employee \n2. Go Back\n3. Go Home\nAny Other key to exit...\nEnter Your Choice : ''')
            try:
                a=int(k)
                if a==1:
                    remove()
                elif a==2:
                    update()
                elif a==3:
                    menu()
                else:
                    exit()
            except:
                exit()

def update():
    print("\n\t\t\tUpdate Info\n\t\t\t========\n\n\t\t1. Update Employee Info\n\t\t2. Remove the Employee\n\t\t3. Back [Home]\n")
    ch=input("Enter Your Choice [1-3] : ")
    while not(ch.isdigit() and (int(ch)==1 or int(ch)==2 or int(ch)==3)):
        if not ch.isdigit():
            print("Sorry I didn't Understand that..")
        ch=input("Enter a Valid Choice between [1-3] : ")
    ch=int(ch)
    if ch==1:
        modify()
    elif ch==2:
        remove()
    else:
        menu()

def viewall():
    print("\n\t\t\tEvery Employee Details\n\t\t\t=================\n\n\t\t1. Details of Every Employee\n\t\t2. Change Password\n\t\t3. Back\n")
    ch=input("Enter Your Choice [1-3] : ")
    while not(ch.isdigit() and (int(ch)==1 or int(ch)==2 or int(ch)==3)):
        if not ch.isdigit():
            print("Sorry I didn't Understand that...\n")
        ch=input("Please Enter a Valid Option between [1-3] : ")
    ch=int(ch) 
    if ch==1:
        searchall()
    elif ch==2:
        changepasswd()
    else:
        employeedetails()
    
def employeedetails():
    print("\n\t\t\tEmployee Details\n\t\t\t============\n\n\t\t1. Search For An Employee\n\t\t2. View Every Employee Details\n\t\t3. Back [Home]\n")
    ch=input("Enter Your Choice [1-3] : ")
    while not(ch.isdigit() and (int(ch)==1 or int(ch)==2 or int(ch)==3)):
        if not ch.isdigit():
            print("Sorry I didn't Understand that...\n")
        ch=input("Please Enter a Valid Option between [1-3] : ")
    ch=int(ch) 
    if ch==1:
        search()
    elif ch==2:
        viewall()
    else:
        menu()
        
def support():
    print("\n\t\t\tSupport\n\t\t\t======\n\n\t\t1. Salary Details\n\t\t2. Business holidays\n\t\t3. Back [Home]\n")
    ch=input("Enter Your Choice [1-3] : ")
    while not(ch.isdigit() and (int(ch)==1 or int(ch)==2 or int(ch)==3)):
        if not ch.isdigit():
            print("Sorry I didn't Understand that..")
        ch=input("Enter a Valid Choice between [1-3] : ")
    ch=int(ch)
    if ch==1:
        print('''
                    -----------------------------------------------
                    Basic Salary                       - 48,000
                    Dearness Allowance                - 5,000
                    House Rent Allowance               - 9,600
                    Conveyance Allowance                - 1,200
                    Entertainment Allowance           - 1,200
                    Medical Allowance                   - 1,200
                    Income Tax                          - 5,000
                    Provident Fund                   - 5,700
                    ------------------------------------------------
                    ''')
        k=input('''\n1. Go Home\n2. Go Back\nAny Other key to exit...\nEnter Your Choice : ''')
        try:
            a=int(k)
            if a==1:
                menu()
            elif a==2:
                support()
            else:
                exit()
        except:
                exit()
    elif ch==2:
        l=['Republic Day','Good Friday','Ambedkar Jayanti','Rama Navami','Eid al-Fitr','Eid al-Adha','Indian Independence Day','Gandhi Jayanti','Dussehra','Prophet', 'Birthday','Diwali','Christmas Day']
        print("\t\t\t\tHolidays")
        print("\t\t\t----------------------------------")
        for k in range(len(l)):
            print("\t\t\t",k+1,".",l[k])
        print("\t\t\t----------------------------------")
        k=input('''\n1. Go Home\n2. Go Back\nAny Other key to exit...\nEnter Your Choice : ''')
        try:
            a=int(k)
            if a==1:
                menu()
            if a==2:
                support()
            else:
                exit()
        except:
            exit()
    else :
        menu()
            
def menu():
    menutext()
    ch=input("Enter Your Choice [1-5] : ")
    while not(ch.isdigit() and (int(ch)==1 or int(ch)==2 or int(ch)==3 or int(ch)==4 or int(ch)==5)):
        if not ch.isdigit():
            print("Sorry I didn't Understand that...\n")
        ch=input("Please Enter a Valid Option [1-5] : ")
    ch=int(ch) 
    if ch==1 :
        register()
    elif ch==2:         
        employeedetails()
    elif ch==3:
        update()
    elif ch==4:
        support()
    else:
        exit()

database()
menu()

