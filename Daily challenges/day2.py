def my_Vowels():
    Vowels=['a,b,c,d,e']
    count=0
    vowl=""
    string=str("Enter your string:")
    for i in string:
        for i in Vowels:
            count+=1
            vowl+=i
            print(vowl,count)
my_Vowels()            
        


            
            
            
