def write():
        fo = open("data_friends.txt","w")
        i=0
        r=[]
        while i <=4:
            i+=1
            i=str(i)
            print("No %a"%(i))
            name = str(input("Name - Sur name : "))
            nickname = str(input("Nickname : "))
            birthday = input("Birth day(Day/Month/Years) : ")
            n = input("Enter years again!: ")
            r.append(n)
            n = str(n)
            age = (2563-int(n))
            age = str(age)
            province = input("Province : ")
            school = str(input("School : "))
            phone = input("Tel : ")
            fo.write("["+i+"] "+name+"       "+nickname+"\t\t" +birthday+"\t\t"+age+"\t    "+province+"\t\t"+school+"\t"+phone+"\n")
            i=int(i)
            break
        fo.close()
def println():
    fo=open("data_friends.txt","r")
    print(" "*60,"My Friend Report"," "*45)
    print("="*140)
    print("No \t   Name\t\t    Nickname\t      Date of Birth\t        Age\t     Province\t         School\t\tPhone number")
    print("="*140)
    print(fo.read())
    print("="*140)
    fo.close()    
write()
println()