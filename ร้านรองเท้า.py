r=[]
n=0
while True:
    k= input("*|Phat Chong Wei Racket Shop|*\n [a] Yonex Sale 20%!! \n [b] Victor Sale 50%!! \n [s] Bill \n [e] Exit \n Choose brand : ")
    k=k.lower()
    if k == "a":
        print("|-------------Yonex------------|")
        print("1) DUORA Z-STRIKE Price 3845")
        print("2) NANORAY Z-SPEED Price 2915")
        print("3) ASTROX 99 LCW Price 6790")
        o=input("Please choose your racket: ")
        if o == "1":     
            r.append("DUORA Z-STRIKE         3076        20%") #เอาไปเก็บในตัวแปร r                       #ราคาเดิม  3845 ลด 20%  เลยเป็น 3076
            print("\n*********Your product has been added to the basket!*********\n")
            n+=3845-(3845*0.2)                                                      #สูตรคำนวนลดราคา
        elif o == "2":
            r.append("NANORAY Z-SPEED       2332          20%") #เอาไปเก็บในตัวแปร r                      #ราคาเดิม 2915 ลด 20%  เลยเป็น 2332
            print("\n*********Your product has been added to the basket!*********\n")
            n+=2915-(2915*0.2)
        elif o == "3":
            r.append("ASTROX 99 LCW         5432          20%") #เอาไปเก็บในตัวแปร r                      #ราคาเดิม 6790 ลด 20%  เลยเป็น 5432
            print("\n*********Your product has been added to the basket!*********\n") 
            n+=6790-(6790*0.2)
        else: print("\n----> ERROR!!! <----\n") #ถ้ายูเซอร์กรอกตัวแปรที่ไม่มีตัวที่เรากำหนดไว้(กวนตีน)จะฟ้อง Error               
    if k == "b":
        print("|-------------Victor------------|")
        print("1) THURSTER K F CLAW Price 4990")
        print("2) JETSPEED S 10 Price 4700")
        print("3) BRAVE SWORD 12 Price 3700")
        o=input("Please choose your racket: ")
        if o == "1":     
            r.append("THURSTER K F CLAW      2495         50%") #เอาไปเก็บในตัวแปร r                        #ราคาเดิม4990ลด50%เลยเป็น2495
            print("\n*********Your product has been added to the basket!*********\n")
            n+=4990-(4990*0.5)                                                      #สูตรคำนวนลดราคา
        elif o == "2":
            r.append("JETSPEED S 10          2350         50%") #เอาไปเก็บในตัวแปร r                        #ราคาเดิม4700ลด50%เลยเป็น2350  
            print("\n*********Your product has been added to the basket!*********\n")
            n+=4700-(4700*0.5)
        elif o == "3":
            r.append("BRAVE SWORD 12        1850          50%") #เอาไปเก็บในตัวแปร r                        #ราคาเดิม3700ลด50%เลยเป็น1850 
            print("\n*********Your product has been added to the basket!*********\n")
            n+=3700-(3700*0.5)
        else: print("\n----> ERROR!!! <----\n") #ถ้ายูเซอร์กรอกตัวแปรที่ไม่มีตัวที่เรากำหนดไว้(กวนตีน)จะฟ้อง Error   
    if k == "s":
        print("="*45)
        print("      รุ่น                ราคา       ส่วนลด")
        print("="*45) 
        count=1              
        for list in r:
            print(count,list) 
            count+=1    
        print("|      Price      : %d     Bath|\n"%(n))    
    if k== "e":
        print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ Good bye :) ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
        break    