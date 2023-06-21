def createCredentialsCSV(startnum,futrollno):
    credfile = open("credentials.py","w+")
    topstr = "USER_CREDENTIALS=[\n"
    botstr = "]"
    credfile.write(topstr)
    for i in range(startnum,futrollno):
        appendst = f"(\"safestudent{i}@gmail.com\",\"1234qwerlo\"),\n"
        credfile.write(appendst)
    credfile.write(botstr)
    credfile.close()

# This will be used to create dummy data in csv format for SAFE performance testing
# Structure : username(email), password,firstname,lastname,email,rollno
def createUserCSV(num,csvfilename):
    # reading available rollno from .rollno file
    rollnofile=None
    try:
        rollnofile = open(".rollno","r")
    except FileNotFoundError:
        rollnofile = open(".rollno","w+")
        rollnofile.write("1")
        rollnofile.seek(0)
    startnum = int(rollnofile.readline())
    rollnofile.close()
    futureRollNum = startnum + int(num)
    csvlst=[]

    # creating dummydata for DataBase insertion
    csvfile = open(csvfilename,"w") 
    for i in range(startnum,futureRollNum):
        appendst = f"safestudent{i}@gmail.com,1234qwerlo,student{i},demotest1,safestudent{i}@gmail.com,{i}\n"
        csvlst.append(appendst) 
    for obj in csvlst:
        csvfile.write(obj)
    csvfile.close()

    # creating credentials for performance testing
    createCredentialsCSV(startnum,futureRollNum)
    rollnofile = open(".rollno","w")
    rollnofile.write(str(futureRollNum))
    rollnofile.close()
    print(num + " users were created in the "+csvfilename +" file.")

if __name__ == "__main__":
    num = input("Enter the number of students : ")
    csvfilename = input("Enter the name of csv file(without the csv extenstion) : ")
    csvfilename = csvfilename +".csv"
    createUserCSV(num,csvfilename)
