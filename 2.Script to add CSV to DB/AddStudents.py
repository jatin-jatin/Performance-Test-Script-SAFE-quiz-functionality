# from apps.organization.models import Organizatioron
import os
import django 
import time
import sys
import csv

def main():
    from apps.organization.models import Organization
    from apps.account.models import SafeUser
    
    searchOrg = input("Enter the organization: ")
    orgref = []
    flag = 1
    allentries = Organization.objects.all()
    
    for org in allentries:
        if org.name == searchOrg:
            orgref.append(org)
            flag = 0
    
    if flag == 1:
        print("The organization you entered is not there in the database. Please enter a valid Organization.")
        sys.exit()
    
    print("Organization exists!")
    
    csvfile = input("Enter the CSV filename (must be in the current directory): ")
    file = open(csvfile)
    reader = csv.reader(file)
    data = [row for row in reader]
    
    for row in data:
        user = SafeUser()
        user.username = row[0]       
        password = row[1] 
        user.set_password(password)
        user.first_name = row[2] 
        user.last_name = row[3] 
        user.email = row[4] 
        user.rollno = row[5] 
        user.save()
        user.organizations.set(orgref)
        user.save()
    
    print("Users were added to the database.")

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "safe.settings.local")
    django.setup()
    main()
