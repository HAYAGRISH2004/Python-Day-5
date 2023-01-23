
salary=int(input("enter your salary:"))
print("grades a/b ")
grade=input("enter your grade:")
print("salary:",salary)
if salary<10000:
    salary+=salary/50
    if grade=="a":
        print("bonus:",salary/20)
        print("total to be paid",salary+salary/20)
    elif grade=="b":
        print("bonus:",salary/10)
        print("total to be paid",salary+salary/10)
    else:
        print("please enter a or b only")
else:        
     if grade=="a":
        print("bonus:",salary/20)
        print("total to be paid",salary+salary/20)
     elif grade=="b":
        print("bonus:",salary/10)
        print("total to be paid",salary+salary/10) 
     else:
        print("please enter a or b only")
