from datetime import datetime
currentYear = datetime.now().year
print(currentYear)
Dob = int(input("Enter the date of birth"))
age = currentYear - Dob
def Dob(age):
   if age<18:
    print("The user is a minor.")
   else:
       if age<36:
        print("The user is a youth.")
       else:
        print("The user is an elder.")  

Dob(age)

