def my_Vowels():
    Vowels=["a","e","i","o","u"]
    count=0
    vowl=""
    string=input("Enter a string:")
    for i in string:
        for i in Vowels:
            count+=1
            vowl+=i
            print((vowl,count))
my_Vowels()            
        


            
            
            
