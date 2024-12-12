#activity4 percentage
name = input("Enter students name")
english = int(input("Enter marks for english"))
math = int(input("Enter marks for math"))
science = int(input("Enter marks for science"))
sum = english + math + science
percentage = (sum/300)*100
print(percentage)

if percentage>70:
    print(name , "scored grade A" , percentage)
elif percentage>40:
    print (name ,"scored grade B", percentage)
else :
    print(name, "scored grade C", percentage)