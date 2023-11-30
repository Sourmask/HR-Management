import mysql.connector as sql
password=input("-- Enter Password :")
SQLconnection=sql.connect(host='localhost',user='root',passwd=password)
cr=SQLconnection.cursor()
dbname="HRDEPT"

def csvtosql(filename,dbname,tbname):
    import csv
    file_name=''
    # To avoid user misinput
    for i in filename:
        if i!='"':
            file_name+=i
    with open(file_name,"r") as f:
        csvr=csv.reader(f,delimiter=',')
        for i in csvr:
            # To avoid possible variable type errors
            for j in i:
                indexx=i.index(j)
                try:
                    J=int(j)
                    i[indexx]=J
                except:
                    continue
            # To convert it into a tuple
            data=()
            for j in i:
                data+=(j,)
                print("\033[1;34;10m",data,"\033[0m")
            cr.execute(f"USE {dbname}")
            cr.execute(f"INSERT INTO {tbname} VALUES {data}")
            SQLconnection.commit()
            print(f"\033[1;32;10mEntered data: {data}\033[m")
        print(f"\033[1;32;10m{tbname} TABLE DATA ENTERED\033[m\n")

try:
   query=f"CREATE DATABASE {dbname}"
   print("\033[1;34;40m",query,"\033[m")
   cr.execute(query)
   print("\033[1;32;10mDATABASE CREATED\033[m\n")
except:
    print("\033[1;31;10mDATABASE CREATION FAILED\033[m\n")

try:
   query=f"USE {dbname}"
   print("\033[1;34;40m",query,"\033[m")
   cr.execute(query)
   print("\033[1;32;10mDATABASE IN USE\033[m\n")
except:
    print("\n\033[1;31;10mUSE DATABASE FAILED\033[m\n")

try:
   query=f"CREATE TABLE employee(ID INT PRIMARY KEY,NAME VARCHAR(40),DOB DATE,OCCUPATION VARCHAR(50),SALARY INT,BRANCH_ID INT,PHONE_NO INT)"
   print("\033[1;34;40m",query,"\033[m")
   cr.execute(query)
   print("\033[1;32;10mEMPLOYEE TABLE CREATED\033[m\n")
   tbname="employee"
except:
    print("\n\033[1;31;10mEMPLOYEE TABLE CREATION FAILED\033[m\n")

try:
    file="HR Management Project 2023\\employee.csv"
    csvtosql(file,dbname,tbname)
except:
    print("\n\033[1;31;10mEMPLOYEE TABLE DATA ADDITION FAILED\033[m\n")

try:
   query=f"CREATE TABLE branch(ID INT PRIMARY KEY,NAME VARCHAR(40),LOCATION VARCHAR(50))"
   print("\033[1;34;40m",query,"\033[m")
   cr.execute(query)
   print("\033[1;32;10mEMPLOYEE TABLE CREATED\033[m\n")
   tbname="branch"
except:
    print("\n\033[1;31;10mEMPLOYEE TABLE CREATION FAILED\033[m\n")

try:
    file="HR Management Project 2023\\branch.csv"
    csvtosql(file,dbname,tbname)
except:
    print("\n\033[1;31;10mBRANCH TABLE DATA ADDITION FAILED\033[m\n")

cont=input("PRESS ENTER TO CONTINUE OR ANY KEY TO DROP DB")

if cont!='':
    cr.execute(f"DROP DATABASE {dbname}")
    print("\n\033[1;31;10mSET UP CANCELLED\033[m\n")
else:
    print("\033[1;32;10mSET UP COMPLETE\033[m\n")
