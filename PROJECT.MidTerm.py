from datetime import date
day = date.today().strftime("%d/%m/%Y")
r=[]
op = open("Listcar.txt","w",encoding="utf-8")
name = input("Enter your name!!: ")
tel = input("Telephone Number!!: ")
op.write("\t"+name+"    เบอร์ติดต่อ :  "+str(tel)+"\tจองรถ :   ")
op.close()
while True:    
    op = open("Listcar.txt","a",encoding="utf-8")
    k= input("*|Welcome to BugYai School|*\n [A] เลือกรถที่ต้องการจอง \n [B] ใบจองรถ \n [E] ออก \n เลือก : ")
    k=k.lower()
    if k == "a":
        print("|-------------รถ------------|")
        print("1) Honda Civic")
        print("2) Van")
        print("3) Bus")
        print("4) BMW")
        print("5) Ford")
        print("6) Yamaha")
        o=input("โปรดเลือกรถที่ต้องการจะยืม:")
        if o == "1":     
            r.append("Honda Civic") 
            op.write("Honda Civic ")
            print("\n*********จองเรียบร้อย!*********\n")
        elif o == "2":
            r.append("Van")
            op.write("Van ")
            print("\n*********จองเรียบร้อย*********\n")
        elif o == "3":
            r.append("Bus")
            op.write("Bus")
            print("\n*********จองเรียบร้อย*********\n")
        elif o == "4":
            r.append("BMW")   
            op.write("BMW ")
            print("\n*********จองเรียบร้อย*********\n")
        elif o == "5":
            r.append("Ford")
            op.write("Ford ")
            print("\n*********จองเรียบร้อย*********\n")
        elif o == "6":
            r.append("Yamaha")  
            op.write("Yamaha ")
            print("\n*********จองเรียบร้อย*********\n")         
        else :
            print("\n******ERROR******\n\n")        
    op.close() 
    if k == "b":
        op = open("Listcar.txt","r",encoding="utf-8")
        print(" "*60,"ใบจองรถ"," "*45)
        print("="*140)
        print("วันที่ยืม %s \t"%(day))
        print("="*140)
        print("ชื่อ :"+op.read())
        print("="*140 )
        op.close()  
    if k == "e":
        print("\n\n♥♥♥♥♥♥♥♥♥♥♥♥♥|Good bye KRUB|♥♥♥♥♥♥♥♥♥♥♥♥♥")    
        break