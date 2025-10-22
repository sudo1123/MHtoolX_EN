# -*- coding: UTF-8 -*-
# Copyright (c) 2025 QU QI
# MIT Licensed (https://opensource.org/licenses/MIT)
import os
import json
import decimal
import string
import math
import os
import sys
os.system("")#Fix escape sequence not working issue (principle unknown)
Version="MHtoolX_EN v1.0.0"
#Increase integer limit
try:
    import sys
    from unicodedata import digit
    sys.set_int_max_str_digits(1000000000)
except:
    pass
#Initialization function
def init_files():
    # Initialize file list and default values
    files = {
        "number saved.json": "0",          
        "mode.json": "0",                               
        "history.json": ["prepare done"],
        "result.json": [],
        "No_History.json": "0",
        "picture_choice.json":"0"
    }   
    # Create files by iteration
    for filename, default in files.items():
        if not os.path.exists(filename):
            with open(filename, "w", encoding="UTF-8") as f:
                json.dump(default, f, ensure_ascii=False)
init_files()#Initialization
#Write version number function
def version(version_code):
    INPUT="history"
    b=version_code
    Unit_length=len(b)
    with open(INPUT+".json","r") as OF:
        File=json.load(OF)
        Str_File=str(File)      
    number=0
    for i in range(len(Str_File)-Unit_length+1):
        if Str_File[i:i+Unit_length]==b:
            number=number+1
    if number ==0:
        kk=[]
        with open("history.json","r") as H:
            ee=json.load(H)
            kk.append(ee)
            kk.append(Version)
        with open("history.json","w") as f:
            json.dump(kk,f)
    INPUT="result"
    b=version_code
    Unit_length=len(b)
    with open(INPUT+".json","r") as OF:
        File=json.load(OF)
        Str_File=str(File)      
    number=0
    for i in range(len(Str_File)-Unit_length+1):
        if Str_File[i:i+Unit_length]==b:
            number=number+1
    if number ==0:
        kk=[]
        with open("result.json","r") as H:
            ee=json.load(H)
            kk.append(ee)
            kk.append(Version)
        with open("result.json","w") as f:
            json.dump(kk,f)
version(Version)  
#Check if operation history saving is enabled
import json
with open("No_History.json","r") as NH2:
    NH4=json.load(NH2)
    if NH4=="0":
        Choice=input("Choose whether to save operation history (Enter 1 for Yes, 2 for No)")
        with open("No_History.json","w") as NH3:
            WR=NH3
            if Choice=="2":
                json.dump("2",WR)
            if Choice=="1":
                json.dump("1",WR)
    else:
        pass
#Save result function
with open("mode.json","r") as qu:
    qi=json.load(qu)
    if qi=="0":
        box=int(input("Do you need to enable saving calculation results? (Enter 1 for Yes, 2 for No. Choosing 2 will permanently disable calculation result saving):"))
        if box==1:
            with open("mode.json","w") as z:
                json.dump("1",z)
        if box==2:
            with open("mode.json","w") as z:
                json.dump("2",z)
    if qi == "1":
        def saved(quqi, p):
            c12 = str(input("Do you want to save the result? (Enter 1 for Yes, 2 for No):"))
            if c12 == "1":
                with open("number saved.json", "r") as zz:
                    tt = json.load(zz)
                # Ensure reply.json content is a list
                try:
                    with open("result.json", "r") as g:
                        ee = json.load(g)
                    if not isinstance(ee, list):  # If not a list, reset to empty list
                        ee = []
                except (json.JSONDecodeError, FileNotFoundError):
                    ee = []            
                ee.extend([quqi, p])  # Append result
                with open("result.json", "w") as f:
                    json.dump(ee, f, ensure_ascii=False)
                print("Done, saved to result.json")
                with open("number saved.json", "w") as zz:
                    json.dump(str(len(ee) // 2), zz)  # Update save count
    if qi=="2":
        def saved(quqi,p):
            pass
#File export function
def export_file(filename):
    import json
    with open(filename+".json", "r") as f:
        history_data = json.load(f)
    with open(filename+".txt", "w", encoding="UTF-8") as f:
        for entry in history_data:
            f.write(str(entry) + "\n")
#History recording function
with open("No_History.json","r")as NH:
    NO=json.load(NH)
    if NO=="1":
        def history(quqi):
            ww=[]
            with open("history.json","r") as g:
                ee=json.load(g)
                ww.append(ee)
                ww.append(quqi)
            with open("history.json","w") as f:
                json.dump(ww,f)
    else:
        def history(oo):
            pass
#turtle resource management function
try:
    import turtle
    def reset_turtle():
        try:
            import turtle
            # Close window (if exists)
            if hasattr(turtle.Screen(), "_root") and turtle.Screen()._root:
                turtle.bye()
            # Clear all pens and canvas
            turtle.clearscreen()
            # Force reset module internal state
            turtle.TurtleScreen._RUNNING = False
            turtle.Turtle._pen = None
            turtle.Turtle._screen = None
        except (ImportError, AttributeError, turtle.Terminator):
            pass
except ImportError:
    def reset_turtle():
        pass
#Save image function
with open("picture_choice.json","r") as pic:
    pict=json.load(pic)
    if pict !="3":
        try:
            import turtle
        except ImportError:
            with open("picture_choice.json","w") as o:
                json.dump("3",o)
                bre=input("Current environment does not support graphics, program needs to restart, press any key to continue")
                exit()
    if pict=="0":
        Inputs=input("Do you want to enable image saving function? (Enter 1 to enable, 2 to permanently disable)")
        if Inputs=="1":
            with open("picture_choice.json","w") as o:
                    json.dump("1",o)
        if Inputs=="2":
            with open("picture_choice.json","w") as o:
                    json.dump("2",o)
        Bre=input("Program needs to restart, press any key to continue")
        sys.exit()
    if pict=="1":
        import time
        def saved_picture():
            Choice=input("Do you want to save the current image? (Enter 1 for Yes, 2 for No)")
            if Choice=="1":
                timestamp = time.time()
                canvas = turtle.getcanvas().postscript(file="MHtool_picture"+str(int(timestamp))+".eps")
                print("Image saved as MHtool_picture"+str(int(timestamp))+".eps")
            else:
                pass
    if pict=="2":
        def saved_picture():
            pass
    if pict=="3":
        try:
            import turtle
            with open("picture_choice.json","w") as o:
                json.dump("0",o)
                Input=input("Detected runtime environment change, program needs to restart, press any key to continue")
                exit()
        except ImportError:
            def saved_picture():
                pass
#User operation reminder function
def reminder(te):
    print("You are using the",str(te),"function")
#Square root function
def Squareroot(number,y):
    x = number
    precision = y
    v = 1.0  # Initial guess value
    k = 1.0  # Initial step size
    current_best = 0.0  # Record current best approximation
    u=[]
    for _ in range(precision):
        for _ in range(10):  # Try 10 adjustments per round
            b = v * v
            if b < x:
                current_best = v  # Update as current lower bound
                v += k
            if b==x:
                u.append(v)
                e = len(u)
                for q in range(e-1):
                    u.pop()
            if b>x:
                v = current_best  # Fallback to previous valid value
                k /= 10          # Reduce step size
                v += k           # Continue approximation
                break            # Break inner loop
    if u==[]:
        return(current_best)
    else:
        pre = u[0]
        return(pre)
#Prime factorization function
def prime_factor(on):
    a = on
    factors = []
    if a == 1:
        factors.append(1)
        return(factors)
    if a <= 0:
        return("none")
    else:
        b = 101
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        Break = 0
        while Break == 0:
            for i in range(len(primes)):
                while a % primes[i] == 0:
                    factors.append(primes[i])
                    a = a // primes[i]  
                    if a == 1:
                        Break = 1
                        break
                if Break == 1:
                    break
            if Break == 1:
                break
            if a > 1:
                b = b * 2
                primes = []
                for num in range(2, b):
                    is_prime = True
                    for p in primes:
                        if p * p > num:
                            break
                        if num % p == 0:
                            is_prime = False
                            break
                    if is_prime:
                        primes.append(num)
        return(factors)
#Factorial function
def factorial(n):
    if n == 0:
        return 1
    else:
        answer=1
        for index in range(n):
            kook=index+1
            answer=answer*kook
        return answer
#Trigonometric function calculation function
def tri_function(IN,IN2,MODE,Precision):
    k=decimal.Decimal(IN/IN2*3.1415926535897)
    answer=0
    if MODE=="1":
        for index in range(Precision):
            I=(-1)**index
            IB=factorial(2*index+1)
            IC=decimal.Decimal(k**(2*index+1))
            term=decimal.Decimal(decimal.Decimal(I/IB)*IC)
            answer=answer+term
        return(str(answer))
    if MODE=="2":
        for index in range(Precision):
            I=(-1)**index
            IB=factorial(2*index)
            IC=decimal.Decimal(k**(2*index))
            term=(decimal.Decimal(I/IB))*IC
            answer=answer+term
        return(str(answer))
    if MODE=="3":
        Sin=0
        Cos=0
        if 2*IN%IN2==0 and (2*IN//IN2)%2 !=0:
            return("DNE")
        else:
            for index in range(Precision):
                I=(-1)**index
                IB=factorial(2*index+1)
                IC=decimal.Decimal(k**(2*index+1))
                term=decimal.Decimal(decimal.Decimal(I/IB)*IC)
                answer=answer+term
            Sin=decimal.Decimal(answer)
            answer=0
            for index in range(Precision):
                I=(-1)**index
                IB=factorial(2*index)
                IC=decimal.Decimal(k**(2*index))
                term=decimal.Decimal(decimal.Decimal(I/IB)*IC)
                answer=answer+term
            Cos=decimal.Decimal(answer)
            answer=Sin/Cos
            return(str(answer))
#Draw coordinate system function
def draw_coordinate_system(max_x,max_y):
    myPen=turtle.Turtle()
    myPen.penup()
    myPen.goto(0,0)
    myPen.pendown()
    myPen.write("0")
    if abs(max_x)>=abs(max_y):
        myPen.goto(abs(max_x),0)
        myPen.write("x")
        myPen.goto(-abs(max_x),0)
        myPen.penup()
        myPen.goto(0,0)
        myPen.pendown()
        myPen.goto(0,abs(max_x))
        myPen.write("y")
        myPen.goto(0,-abs(max_x))
    else:
        myPen.goto(abs(max_y),0)
        myPen.write("x")
        myPen.goto(-abs(max_y),0)
        myPen.penup()
        myPen.goto(0,0)
        myPen.pendown()
        myPen.goto(0,abs(max_y))
        myPen.write("y")
        myPen.goto(0,-abs(max_y))
#User interaction
history("turn on*")
print("Hello^=^")
page="1"
menu=""
menu1="1:Generate prime table, 2:Calculate arithmetic square root, 3:Calculate pi\n4:Calculate n-th power, 5:Four arithmetic operations, 6:Generate Fibonacci sequence\n7:Calculate golden ratio, 8:Change program (Greedy algorithm), 9:Statistics\n"
menu2="10:Draw function graph, 11:Exam score data organization, 12:Draw trigonometric function graph\n13:Solve quadratic equation, 14:Calculate factorial, 15:Polar coordinate conversion\n16:String frequency statistics & positioning, 17:Prime factorization, 18:Calculate GCD and LCM\n"
menu3="19:Decimal to binary, 20:Calculate permutations and combinations, 21:Calculate trigonometric function values\n22:Radian-degree conversion, 23:Prime number check, 24:Vector magnitude calculation\n25:Calculate area of any triangle, 26:Vector dot product, 27:Decimal to hexadecimal\n"
menu4="28:Calculate rational roots of integer coefficient polynomial, 29:Calculate numerical integration\n"
menuf="timer:Start timer, rr:View historical calculation results, er:Export historical calculation results\ncr:Clear historical calculation results, rh:View operation history, eh:Export operation history\nch:Clear operation history, cs:Clear screen, version:View version\n"
menu=menu1
page="1"
while True:
    a = input("Please enter command (enter exit to close program, enter menu to view function menu, enter amenu to list all functions):")
    #Menu
    if a=="amenu":
        print(menu1+menu2+menu3+menu4+menuf)
    if a=="menu":
        while True:
            if page=="1":
                print("Function Menu\n"+"Current page "+str(page)+" of "+"5"+" pages\n"+menu+"\nEnter np for next page")
            elif page=="f":
                print("Function Menu\n"+"Current page "+str(page)+" of "+"5"+" pages\n"+menu+"\nEnter pp for previous page")
            else:
                print("Function Menu\n"+"Current page "+str(page)+" of "+"5"+" pages\n"+menu+"\nEnter pp for previous page, enter np for next page")
            E=input("Page command:(Enter quit to exit function menu)")
            if E=="pp":
                if page=="1":
                    print("Already at first page")
                    continue
                if page=="2":
                    menu=menu1
                    page="1"
                    continue
                if page=="3":
                    menu=menu2
                    page="2"
                    continue
                if page=="4":
                    menu=menu3
                    page="3"
                if page=="f":
                    menu=menu4
                    page="4"
                    continue
            if E=="np":
                if page=="1":
                    menu=menu2
                    page="2"
                    continue
                if page=="2":
                    menu=menu3
                    page="3"
                    continue
                if page=="3":
                    menu=menu4
                    page="4"
                    continue
                if page=="4":
                    menu=menuf
                    page="f"
                    continue
                if page=="f":
                    print("Already at last page")
                    continue
            if E=="quit":
                break
    #Generate prime table
    if a=="1":
        reminder("Generate Prime Table")
        mode=input("Select method (Enter 1 for normal method, 2 for Sieve of Eratosthenes)")
        if mode=="1":
            b = int(input("Enter the range for the prime table you want to generate: (Note: add 1):"))
            def prime(b):
                number = (b)
                if number == 1:
                    print(number, "is not a prime number")
                    return False
                for c in range(2, int(math.sqrt(number))+1):
                    if number % c == 0:
                        return False
                return True

            d = []
            for e in range(2, b):
                if prime(e):
                    d.append(e)
            print("Found", len(d), "prime numbers in total")
            print(d)
            saved("the reply from function 1[1]",str(len(d))+" "+"prime numbers:"+str(d))
            history("1[1]*")
        if mode=="2":
            b = int(input("Enter the range for the prime table you want to generate (Note: add 1):"))   
            primes = []
            for num in range(2, b): 
                is_prime = True
                for p in primes:
                    if p*p > num:   
                        break
                    if num % p == 0:
                        is_prime = False
                        break
                if is_prime:
                    primes.append(num)   
            print("Found", len(primes), "prime numbers in total")
            print(primes)
            saved("the reply from function 1[2]",str(len(primes))+" "+"prime numbers:"+str(primes))
            history("1[2]*")
    #Calculate arithmetic square root
    if a == "2":
        reminder("Calculate Arithmetic Square Root")
        INPUT=input("Select calculation method (Enter 1 for successive approximation, 2 for Newton's method)")
        if INPUT=="1":
            x = float(input("Enter the number to calculate the square root of:"))
            precision = int(input("Enter number of iterations (larger value is more accurate, recommended 10000):"))
            v = 1.0  # Initial guess value
            k = 1.0  # Initial step size
            current_best = 0.0  # Record current best approximation
            u=[]
            for _ in range(precision):
                for _ in range(10):  # Try 10 adjustments per round
                    b = v * v
                    if b < x:
                        current_best = v  # Update as current lower bound
                        v += k
                    if b==x:
                        u.append(v)
                        e = len(u)
                        for q in range(e-1):
                            u.pop()
                    if b>x:
                        v = current_best  # Fallback to previous valid value
                        k /= 10          # Reduce step size
                        v += k           # Continue approximation
                        break            # Break inner loop
            if u==[]:
                print("Approximate square root is:", current_best)
                saved("the reply from function 2[1]", str(current_best)+", ,"+"the square root of"+str(x))
            else:
                pre = u[0]
                print("Square root is:", pre)
                saved("the reply from function 2[1]",str(pre)+", ,"+"the square root of"+str(x))
            history("2[1]*")
        if INPUT=="2":
            def sqrt_newton(x, max_iter=1000, precision=1e-10):
                guess = x / 2  # Initial guess value
                for _ in range(max_iter):
                    guess = (guess + x / guess) / 2
                    if abs(guess * guess - x) < precision:
                        break
                return guess
            x = float(input("Enter the number to calculate the square root of:"))
            precision = int(input("Enter number of iterations (larger value is more accurate, recommended 10):"))
            result = sqrt_newton(x, max_iter=precision)
            print("Approximate square root is:", result)
            saved("the reply from function 2[2]",str(result)+", ,"+"the square root of"+str(x))
            history("2[2]*")
    #Calculate pi
    if a =="3":
        reminder("Calculate Pi")
        c=int(input("Select algorithm (1 for Leibniz series, 2 for geometric method, 3 for Monte Carlo method, 4 for Ramanujan formula)"))
        if c==1:#Leibniz series method
            a=0
            b=1
            d=0
            last_p = -1
            e=int(input("Enter required precision (multiple of 10)"))
            show_progress = input("Show calculation progress? (1 for Yes, 2 for No)") == "1"
            for c in range(1,e):
                d=2*c-1
                if b==1:
                    a+=1/d
                else:
                    a-=1/d
                if show_progress:
                    current_p = int((c/(e-1)*100))  # Current percentage
                    if current_p != last_p:        # Print only when percentage changes
                        print(f"Calculating {current_p}%")
                        last_p = current_p
                b=b*-1
                d=4*a
            print("Pi is approximately",d)
            saved("the reply from function 3",d)
            history("3(1)*")
        if c==2:#Geometric method
            reset_turtle()
            try:
                import turtle
            except ImportError:
                print("turtle module not available.")
                continue
            myPen = turtle.Turtle()
            Pos =0
            o = 0
            k = 0
            c = 0
            j = int(input("Enter required precision (multiple of 10)"))
            r = 360*j
            py = r/2
            show_progress = input("Show calculation progress? (1 for Yes, 2 for No)") == "1"
            myPen.speed(0)
            for i in range(int(py)):
                if show_progress:
                    print("Calculating:"+str(i+1)+"/"+str(py))
                myPen.forward(0.0001)
                myPen.left(1/j)
                o = o+1
                if o == r/2:
                    Pos=(myPen.pos())
            Pos1=str(Pos)
            Pos2=Pos1.split("(")
            Pos3=Pos2[1].split(")")
            Pos4=Pos3[0].split(",")
            Pos5=Pos4[1]
            m = float(Pos5)
            q1=r/10000
            t = q1/m
            turtle.bye()
            print("Pi is approximately",t)
            saved("the reply from function 3",t)
            history("3(2)*")
        if c==3:#Monte Carlo method
            import random
            import math
            d=0
            e=int(input("Enter number of points"))
            show_progress = input("Show calculation progress? (1 for Yes, 2 for No)") == "1"
            last_p=-1
            for i in range(e):
                a=random.uniform(0,1)
                b=random.uniform(0,1)
                c=math.sqrt(a*a+b*b)
                if c<1:
                    d=d+1
                if show_progress:
                    current_p = int((i+1)/e*100)
                    if current_p != last_p:
                        print(f"Calculating: {current_p}%")
                        last_p = current_p
            print("Pi is approximately",d/e*4)
            qu=d/e*4
            saved("the reply from function 3",qu)
            history("3(3)*")
        if c==4:#Ramanujan formula method
            acc=int(input("Enter precision"))
            show_progress = input("Show calculation progress? (1 for Yes, 2 for No)") == "1"
            root2=Squareroot(2,acc)
            coe=root2*2/9801
            latter=0
            last_percent = -1
            for index in range(acc):
                v1=4*index
                v2=factorial(v1)*(1103+26390*index)
                v3=factorial(index)**4
                v4=396**(4*index)
                v5=v3*v4
                v6=v2/v5
                latter=latter+v6
                if show_progress:
                    current_percent = int((index + 1) / acc * 100)  # Calculate current percentage
                    if current_percent != last_percent:  # Print only when percentage changes
                        print(f"Calculating: {current_percent}%")
                        last_percent = current_percent
            r=coe*latter
            answer=r**(-1)
            print("Pi is approximately",answer)
            saved("the reply from function 3",answer)
            history("3(4)*")
    #Calculate n-th power
    if a=="4":
        reminder("Calculate n-th Power")
        s = int(input("Enter base"))
        h = int(input("Enter exponent"))
        u=s
        o=0
        w=s
        l=h-1
        ll=0
        for i in range(l):
            u=u*w   
        print("Result is", u)
        saved("the reply from function 4",str(s)+"^"+str(h)+"="+str(u))
        ll=ll+1
        history("4*")
    #Four arithmetic operations
    if a=="5":
        reminder("Four Arithmetic Operations")
        s = int(input("Select mode (1 for addition, 2 for subtraction, 3 for division, 4 for multiplication)"))
        if s == 1:
            b = int(input("Enter an addend"))
            c = int(input("Enter another addend"))
            d = c+b
            print("Result is", d)
            ee=0
            saved("the reply from function 5[1]",str(b)+"+"+str(c)+"="+str(d))
            ee=ee+1
            ee=0
            history("5(1)*")
        if s == 2:
            e = int(input("Enter minuend"))
            f = int(input("Enter subtrahend"))
            g = e-f
            print("Result is", g)
            ff=0
            saved("the reply from function 5[2]",str(e)+"-"+str(f)+"="+str(g))
            ff=ff+1
            ff=0
            history("5(2)*")
        if s == 3:
            h = int(input("Enter dividend"))
            j = int(input("Enter divisor"))
            if j == 0:
                print("You entered 0 as divisor, 0 cannot be a divisor")
                saved("the reply from function 5[3]","error")
                history("5(3)(error)")
                continue
            else:
                k = h/j
                print("Result is", k)
            jj=0
            saved("the reply from function 5[3]",str(h)+"/"+str(j)+"="+str(k))
            jj=jj+1
            jj=0
            history("5(3)*")
        if s == 4:
            l = int(input("Enter a multiplier"))
            m = int(input("Enter another multiplier"))
            n = l*m
            print("Result is", n)
            gg=0
            saved("the reply from function 5[4]",str(l)+"*"+str(m)+"="+str(n))
            gg=gg+1
            history("5(4)*")
    #Generate Fibonacci sequence
    if a =="6":
        reminder("Generate Fibonacci Sequence")
        a = (int(input("Enter range")))
        show_progress = input("Show calculation progress? (1 for Yes, 2 for No)") == "1"
        last_p = -1
        b = 1
        c = 0
        d = []
        for i in range(2):
            d.append(b)
        for e in range(a):
            f = d[e]+d[e+1]
            d.append(f)
            if show_progress:
                current_p = int((e+1)/a*100)
                if current_p != last_p:
                    print(f"Calculating {current_p}%")
                    last_p = current_p
        print("Sequence is"+str(d))
        saved("the reply from function 6",d)
        history("6*")
    #Calculate golden ratio
    if a =="7":
        reminder("Calculate Golden Ratio")
        a = (int(input("Enter range")))
        show_progress = input("Show calculation progress? (1 for Yes, 2 for No)") == "1"
        last_p = -1
        b = 1
        c = 0
        d = []
        for i in range(2):
            d.append(b)
        for e in range(a):
            f = d[e]+d[e+1]
            d.append(f)
            if show_progress:
                current_p = int((e+1)/a*100)
                if current_p != last_p:
                    print(f"Calculating {current_p}%")
                    last_p = current_p
        s=len(d)
        v=d[s-2]/d[s-1]
        print("Golden ratio is approximately",v)
        saved("the reply from function 7",v)
        history("7*")
    #Greedy algorithm
    if a=="8":
        reminder("Greedy Algorithm")
        target= Input=float(input("Enter the amount of change needed: (RMB)"))
        money=[100,50,20,10,5,1,0.5,0.1]
        number=[0,0,0,0,0,0,0,0,0]
        saved1=[]

        for i in range(8):
            number[i]=target//money[i]
            target=target%money[i]
        for i in range(8):
            print(money[i],"Yuan count:",number[i])
            saved1.append(money[i])
            saved1.append(number[i])
        saved("the reply from function 8",saved1)
        history("8*")
    #Statistics
    if a=="9":
        reminder("Statistics")
        b=int(input("Enter 1 for mean, 2 for weighted mean, 3 for variance, 4 for standard deviation, 5 for median, 6 for mode:"))
        if b==1:
            c=[]
            d=[]
            f=2
            while f>0:
                e=input("Enter data (one at a time, enter f when finished)")
                if e=="f":
                    f=0
                    if len(c)==0:
                        print("Error: No data entered!")
                        break
                else:
                    try:
                        c.append(float(e))
                    except:
                        print("Input error!")
            if len(c)>0:
                w2=0.0
                for w3 in range(len(c)):
                    w2 += c[w3]
                w4=w2/len(c)
                print("Mean is",w4)
                saved("the reply from function9(1)",w4)
                history("9(1)*")
        if b==2:
            c=[]
            w1=[]
            f=2
            while f>0:
                e=input("Enter data (one at a time, enter f when finished)")
                if e=="f":
                    f=0
                    if len(c)==0:
                        print("Error: No data entered!")
                        break
                else:
                    try:
                        c.append(float(e))
                    except:
                        print("Input error!")
            f=2
            while f>0:
                e=input("Enter weights (one at a time, enter f when finished)")
                if e=="f":
                    f=0
                    if len(w1)==0:
                        print("Error: No weights entered!")
                        break
                else:
                    try:
                        w1.append(float(e))
                    except:
                        print("Input error!")
            # Check quantity
            if len(c)!=len(w1):
                print("Error: Data and weight counts differ!")
            else:
                w11=0.0
                w12=0.0
                for w7 in range(len(c)):
                    w8=c[w7]
                    w9=w1[w7] 
                    w11 += w8*w9
                    w12 += w9
                if w12==0:
                    print("Error: Sum of weights is 0!")
                else:
                    w14=w11/w12
                    print("Weighted mean is",w14)
                    saved("the reply from function9(2)",w14)
                    history("9(2)*")
        if b==3:
            c=[]
            f=2
            while f>0:
                e=input("Enter data (one at a time, enter f when finished)")
                if e=="f":
                    f=0
                    if len(c)==0:
                        print("Error: No data entered!")
                        break
                else:
                    try:
                        c.append(float(e))
                    except:
                        print("Input error!")
            if len(c)>0:
                w2=0.0
                for w3 in range(len(c)):  
                    w2 += c[w3]
                w4=w2/len(c)
                w6=0.0
                for w7 in range(len(c)): 
                    w8=c[w7]-w4
                    w6 += w8*w8
                w9=w6/len(c)
                print("Variance is",w9)
                saved("the reply from function9(3)",w9)
                history("9(3)*")
        if b==4:
            c=[]
            f=2
            while f>0:
                e=input("Enter data (one at a time, enter f when finished)")
                if e=="f":
                    f=0
                    if len(c)==0:
                        print("Error: No data entered!")
                        break
                else:
                    try:
                        c.append(float(e))
                    except:
                        print("Input error!")
            if len(c)>0:
                w2=0.0
                for w3 in range(len(c)):
                    w2 += c[w3]
                w4=w2/len(c)
                w6=0.0
                for w7 in range(len(c)):
                    w8=c[w7]-w4
                    w6 += w8*w8
                w9=w6/len(c)
                x = w9
                d = int(input("Required precision (enter integer):"))
                current = 0.0
                step = 1.0
                for _ in range(d):  # Limit loop count
                    while (current + step) * (current + step) <= x:
                        current += step
                    step = step / 10
                print("Standard deviation is approximately", round(current, 5))  # Limit decimal places
                saved("the reply from function9(4)",current)
                history("9(4)*")
        if b==5:
            DATA=[]
            Answer=0
            M1=0
            M2=0
            Break=0
            while True:
                data=input("Enter data one by one, enter f when finished")
                if data=="f":
                    break
                else:
                    try:
                        float(data)
                    except:
                        print("Invalid parameter")
                        Break=1
                        break
                    DATA.append(float(data))
            if Break==1:
                continue
            List=DATA
            def selection_sort(List):
                for i in range(len(List)):
                    index=i
                    for x in range(i+1,len(List)):
                        if List[x]<List[i]:
                            index=x
                    List[i],List[index]=List[index],List[i]
            selection_sort(List)
            if ((len(DATA)+1)/2)%1==0:
                Answer=DATA[int((len(DATA)+1)/2-1)]
            else:
                M1=DATA[int((len(DATA)+1)/2-1.5)]
                M2=DATA[int((len(DATA)+1)/2-0.5)]
                Answer=(M1+M2)/2
                print("Median is",Answer)
                saved("the reply from function9(5)",Answer)
                history("9(5)*")
        if b==6:
            DATA=[]
            Frequency={}
            Answer=0
            M1=0
            M2=0
            Break=0
            MAX=0
            MAX2=[]
            nMAX=0
            OL=0
            Answer=""
            while True:
                data=input("Enter data one by one, enter f when finished")
                if data=="f":
                    break
                else:
                    try:
                        float(data)
                    except:
                        print("Invalid parameter")
                        Break=1
                        break
                    DATA.append(float(data))
            if Break==1:
                history("9(6)[error]")
                continue
            for index in range(len(DATA)):
                if DATA[index] in Frequency:
                    Frequency[DATA[index]]=Frequency[DATA[index]]+1
                else:
                    Frequency[DATA[index]]=1
            OL=len(DATA)
            DATA=list(set(DATA))
            AL=len(DATA)
            DI=OL-AL
            for index2 in DATA:
                if Frequency[index2]>MAX:
                    MAX=Frequency[index2]
                    MAX2.clear()
                    MAX2.append(index2)
                if Frequency[index2]==MAX:
                    nMAX=nMAX+1
            if nMAX==OL-DI:
                print("No mode exists")
                saved("the reply from function9(6)","none")
            else:
                if len(MAX2) != 1:
                    print("Multiple modes exist:",MAX2)
                    saved("the reply from function9(6)",MAX2)
                else:
                    print("Unique mode is",MAX2[0])
                    saved("the reply from function9(6)",MAX2[0])
            history("9[6]")
    #Draw function graph
    if a=="10":
        reminder("Draw Function Graph")
        reset_turtle()
        try:
            import turtle
        except ImportError:
            print("turtle module not available")
            continue
        x=int(input("Select mode (1 for linear function, 2 for quadratic function)"))
        if x==1:
            myPen=turtle.Turtle()
            b=float(input("Enter coefficient of x"))
            c=float(input("Enter constant term"))
            e=0
            f=int(input("Enter number of points (must be even)"))
            j=float(input("Enter point spacing"))
            d=-f/2*j
            for i in range(f):
                e=d*b+c
                if i==0:
                    myPen.penup()
                    myPen.goto(d,e)
                    myPen.pendown()
                else:
                    myPen.goto(d,e)
                    d=d+j
            draw_coordinate_system(d,e)
            print("Drawing completed")
            saved_picture()
            turtle.done()
            history("10(1)")
        if x==2:
            myPen=turtle.Turtle()
            a=float(input("Enter coefficient of x^2"))
            b=float(input("Enter coefficient of x"))
            c=float(input("Enter constant term"))
            e=0
            f=int(input("Enter number of points (must be even)"))
            j=float(input("Enter point spacing"))
            d=-f/2*j
            for i in range(f):
                e=d**2*a+d*b+c
                if i==0:
                    myPen.penup()
                    myPen.goto(d,e)
                    myPen.pendown()
                else:
                    myPen.goto(d,e)
                    d=d+j
            draw_coordinate_system(d,e)
            print("Drawing completed")
            saved_picture()
            turtle.done()
            history("10(2)")
#Timer
    if a=="timer":
        import time
        import math
        try:
            import keyboard
            mine=0
            s=0
            start=time.time()
            t2=0
            t3=0
            mine=0
            s=0
            while True:
                end=time.time()
                t=end-start
                t2=t//1
                t3=t2//60
                if t3<1:
                    if t2==1:
                        print(t2,"second","Press a key to stop timer")
                    if t2>1:
                        print(t2,"seconds","Press a key to stop timer")
                if t3>1:
                    mine=t3
                    s=t2-60*t3
                    print(mine,"minutes",s,"seconds","Press a key to stop timer")
                if t3==1:
                    mine=t3
                    s=t2-60*t3
                    print(mine,"minute",s,"seconds","Press a key to stop timer")
                if keyboard.is_pressed('a'):
                    break
            history("timer")
        except:
            print("Current environment does not support timer function")
            history("timer(environment not support)")
            continue
#Exam score data organization
    if a=="11":
        reminder("Exam Score Data Organization")
        s=2
        Sum=0
        average=0
        Max=0
        Min=0
        Dict={}
        while s>1:
            qu=input("Enter student name, enter f when all entered")
            if qu=="f":
                s=0
            else:
                qi=input("Enter student score")
                Dict[qu]=float(qi)
        keys=[]
        z=[]
        x=0
        y=[]
        name=""
        Max=0
        Sum=0
        average=0
        for l in Dict:
            keys.append(l)
        for i in range(len(keys)):
            z.append(Dict[keys[i]])
            if z[i]>Max:
                Max=z[i]
                x=i
                name=keys[x]
            y.append(i)
        print(name,"has the highest score:",Max)
        Min=Max
        for i in range(len(keys)):
            z.append(Dict[keys[i]])
            if z[i]<Min:
                Min=z[i]
                x=i
                name=keys[x]
        print(name,"has the lowest score:",Min)
        for l in Dict:
            Sum=Sum+Dict[l]
            average=Sum/len(keys)
        print("Class total score:",Sum)
        print("Class average score:",average)
        saved("the reply from function 11","max:"+str(Max)+" min:"+str(Min)+" all:"+str(Sum)+" average:"+str(average))
        history("11")
#Draw trigonometric function graph
    if a=="12":
        reminder("Draw Trigonometric Function Graph")
        reset_turtle()
        try:
            import turtle
        except ImportError:
            print("turtle module not available.")
            continue
        print("Note: Tangent function can only be drawn using algebraic method!")
        Method=input("Select algorithm (Enter 1 for geometric algorithm, 2 for algebraic algorithm)")
        mode=input("Select mode (Enter 1 for sine, 2 for cosine, 3 for tangent)")
        acc4=int(input("Set graph X-axis starting point (recommended -300 for sine & tangent, -250 for cosine)"))
        acc5=int(input("Set graph Y-axis starting point (recommended 0 for sine & tangent & algebraic cosine, -10000 for geometric cosine)"))
        Pa=mode
        pi=3.1415926535 
        if Method=="1":#Geometric method
            myPen=turtle.Turtle()
            acc1=float(input("Enter simulation angle (recommended 1)"))
            acc2=int(input("Enter step (recommended 100)"))
            acc3=int(input("Enter geometric method scaling factor (recommended 10000)"))
            if Pa=="3":
                print("Geometric algorithm cannot draw tan graph, please use algebraic algorithm")
                history("12[error]")
                turtle.bye()
                continue
            acc6=acc3/((360/acc1*acc2)/(2*pi))
            step=int(2*pi*acc2/(360/acc1))
            Y_co=[]
            myPen.speed(0)
            myPen.penup()
            myPen.goto((360/acc1*acc2)/(2*pi),0)
            myPen.pendown()
            myPen.left(90)
            for i in range(int(360/acc1)):
                myPen.forward(step)
                myPen.left(acc1)
                Pos=myPen.pos()
                Pos1=str(Pos)
                Pos2=Pos1.split("(")
                Pos3=Pos2[1].split(")")
                Pos4=Pos3[0].split(",")
                if Pa=="1":
                    Pos5=Pos4[1]
                if Pa=="2":
                    Pos5=Pos4[0]
                Y_co.append(float(Pos5))
                print("Sampling,",i+1,"/",int(360/acc1))
            turtle.clearscreen()
            print("Drawing...")
            for r in range(int(360/acc1)):
                step1=r*acc6
                step2=acc6*float(Y_co[r])
                myPen.penup()
                myPen.goto(acc4+step1,acc5+step2)
                myPen.pendown()
                myPen.dot(2)
            print("Drawing completed")
            saved_picture()
            turtle.done()
            history("12[1]")
        if Method=="2":#Algebraic method
            Coordinates_Y=[]
            acc6=int(input("Enter calculation precision (integer) (recommended 100)"))
            acc7=int(input("Enter number of points (recommended 360)"))
            acc8=int(input("Enter algebraic method scaling factor (recommended 2)"))
            show_progress = input("Show sampling progress? (1 for Yes, 2 for No)") == "1"
            last_percent = -1
            C1=2
            C2=acc7
            C3=0
            acc9=acc8*acc7/(2*pi)
            for index in range(acc7):
                try:
                    Coordinates_Y.append(float(tri_function(C3,C2,mode,acc6)))#This except accidentally catches the original invalidoperation error, but doesn't mean the problem is solved
                except:
                    Coordinates_Y.append("DNE")
                if show_progress:
                    current_percent = int((index + 1) / acc7 * 100)  # Calculate current percentage
                    if current_percent != last_percent:  
                        print(f"Calculating sampling: {current_percent}%")
                        last_percent = current_percent
                C3=C3+C1
            turtle.clearscreen()
            print("Drawing...")
            for r in range(acc7):
                step1=acc8*r
                try:
                    step2=acc9*Coordinates_Y[r]
                except:
                    continue
                turtle.speed(0)
                turtle.penup()
                turtle.goto(acc4+step1,acc5+step2)
                turtle.pendown()
                turtle.dot(2)
            print("Drawing completed")
            saved_picture()
            turtle.done()
            history("12[2]")
    #Solve quadratic equation
    if a=="13":
        reminder("Solve Quadratic Equation")
        answer1=0
        answer2=0
        Answer=[]
        Coefficients=[]
        Precision=int(input("Enter precision (larger number is more accurate, recommended 100)"))
        while True:
            Coefficient=input("Enter coefficients in order, from highest degree to constant term (enter 0 if term doesn't exist), enter f when finished")
            if Coefficient=="f":
                break
            else:
                try:
                    float(Coefficient)
                except:
                    print("Invalid parameter")
                    break
                Coefficients.append(float(Coefficient))
        length=len(Coefficients)
        if length != 3:
            print("Coefficient count error!")
        else:
            discriminant = (Coefficients[1] ** 2) - (4 * Coefficients[0] * Coefficients[2])
            if discriminant<0:
                Answer.append("no solution")
            else:
                answer1=((-Coefficients[1])+Squareroot(discriminant,Precision))/(2*Coefficients[0])
                answer2=((-Coefficients[1])-Squareroot(discriminant,Precision))/(2*Coefficients[0])
                if answer1==answer2:
                    Answer.append(answer1)
                else:
                    Answer.append(answer1)
                    Answer.append(answer2)
            print("Equation solutions:",Answer)
            saved("the reply from function 13",Answer)
            history("13")
    #Calculate factorial
    if a == "14":
        reminder("Calculate Factorial")
        n = int(input("Enter positive integer n:"))
        result = factorial(n)
        print(f"{n}! = {result}")
        saved("the reply from function 14", result)
        history("14*")
    #Polar coordinate conversion
    if a == "15":
        reminder("Polar Coordinate Conversion")
        import math
        mode = input("Select conversion direction (1: Cartesian to polar, 2: Polar to Cartesian)")
        
        try:
            if mode == "1":
                x = float(input("Enter x coordinate: "))
                y = float(input("Enter y coordinate: "))
                r = math.sqrt(x**2 + y**2)
                theta = math.degrees(math.atan2(y, x))  # Output in degrees
                result = f"Polar coordinates: ({round(r, 4)}, {round(theta, 4)}°)"
                
            elif mode == "2":
                r = float(input("Enter radius r: "))
                theta = math.radians(float(input("Enter angle θ(°): ")))  # Convert to radians
                x = r * math.cos(theta)
                y = r * math.sin(theta)
                result = f"Cartesian coordinate: ({round(x, 4)}, {round(y, 4)})"
                
            else:
                print("Input error!")
                history("15*[error]")
                continue
                
            print(result)
            saved("the reply from function 15", result)
            history("15*")
            
        except ValueError:
            print("Error: Please enter valid numbers!")
            history("15*[invalid_input]")
    #String frequency statistics & positioning
    if a=="16":
        reminder("String Frequency Statistics & Positioning")
        INPUT=input("Enter the name of the json file you want to search (e.g., enter file for file.json)")
        b=input("Enter the text or number you need to find:")
        Unit_length=len(b)
        try:
            with open(INPUT+".json","r") as OF:
                File=json.load(OF)
                Str_File=str(File)      
            number=0
            for i in range(len(Str_File)-Unit_length+1):
                if Str_File[i:i+Unit_length]==b:
                    number=number+1
                    print("Found, at index position",i,"to",i+Unit_length-1,"in",INPUT,".json")
            print(b,"appears",number,"times in",INPUT,".json")
            saved("the reply from function 16","“"+str(b)+"”"+" "+str(number)+" "+"times"+" "+"in"+" "+"“"+str(INPUT)+".json"+"”")
            history("16")
        except:
            print("File does not exist")
            saved("the reply from function 16","file not exist")
            history("16[error]")
    #Prime factorization
    if a=="17":
        reminder("Prime Factorization")
        a = int(input("Enter number to factorize"))
        if a == 1:
            print("Prime factor is", 1)
            saved("the reply from function 17","factor"+":"+"1")
            history("17")
            continue
        if a <= 0:
            print("0 and negative numbers have no prime factors")
            saved("the reply from function 17","factor"+":"+"none")
            history("17[none]")
            continue
        else:
            b = 101
            primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
            factors = []
            Break = 0
            while Break == 0:
                for i in range(len(primes)):
                    while a % primes[i] == 0:
                        factors.append(primes[i])
                        a = a // primes[i]  
                        if a == 1:
                            Break = 1
                            break
                    if Break == 1:
                        break
                if Break == 1:
                    break
                if a > 1:
                    print("The prime factors of the number you provided are too large, expanding search range, please wait")
                    b = b * 2
                    primes = []
                    for num in range(2, b):
                        is_prime = True
                        for p in primes:
                            if p * p > num:
                                break
                            if num % p == 0:
                                is_prime = False
                                break
                        if is_prime:
                            primes.append(num)
            print("Prime factors are", factors)
            saved("the reply from function 17","factor(s)"+":"+str(factors))
            history("17")
    #Calculate GCD and LCM
    if a == "18":
        reminder("Calculate GCD and LCM")
        choice = input("Select calculation mode: 1 for Greatest Common Divisor (GCD), 2 for Least Common Multiple (LCM): ")   
        UserInput = []
        print("Start entering numbers (enter f when finished):")
        while True:
            Input = input("Enter a positive integer (or enter f to finish): ")
            if Input.lower() == 'f':
                break
            try:
                num = int(Input)
                if num <= 0:
                    print("Error: Please enter positive integers!")
                    continue
                UserInput.append(num)
            except ValueError:
                print("Invalid input, please enter a number or f to finish!")
                continue
        if len(UserInput) < 2:
            print("Error: At least two numbers required!")
            history("18*[error]")
        else:
            nums = UserInput  
        
            # Prime factorization verification
            factors_list = []
            valid = True
            for num in nums:
                factors = prime_factor(num)
                if factors == "none":
                    print(f"Error: Number {num} cannot be prime factorized!")
                    valid = False
                    break
                factors_list.append(factors)
        
            if valid:
                # Count prime factor frequencies for each number
                from collections import defaultdict
                counts_list = []
                for factors in factors_list:
                    counts = defaultdict(int)
                    for p in factors:
                        counts[p] += 1
                    counts_list.append(counts)
            
                # Calculate GCD or LCM
                if choice == "1":
                    # Calculate GCD
                    common_primes = set(counts_list[0].keys())
                    for cnt in counts_list[1:]:
                        common_primes.intersection_update(cnt.keys())
                    gcd = 1
                    for prime in common_primes:
                        min_power = min(cnt[prime] for cnt in counts_list)
                        gcd *= prime ** min_power
                    print(f"Greatest Common Divisor (GCD) is: {gcd}")
                    saved("the reply from function 18[GCD]", gcd)
                    history("18[GCD]*")
            
                elif choice == "2":
                    # Calculate LCM
                    all_primes = set()
                    for cnt in counts_list:
                        all_primes.update(cnt.keys())
                    lcm = 1
                    for prime in all_primes:
                        max_power = max(cnt.get(prime, 0) for cnt in counts_list)
                        lcm *= prime ** max_power
                    print(f"Least Common Multiple (LCM) is: {lcm}")
                    saved("the reply from function 18[LCM]", lcm)
                    history("18[LCM]*")
            
                else:
                    print("Invalid selection!")
                    history("18*[invalid]")
    #Decimal to binary
    if a=="19":
        reminder("Decimal to Binary")
        INPUT=input("Enter decimal integer")
        digits=[]
        reverse=[]
        result=""
        try:
            int(INPUT)
        except:
            print("Invalid input")
            history("19([error]")
            continue
        else:
            ten=int(INPUT)
        if ten==0:
            result="0"           
        else:
            while ten>=1:
                digit=ten%2
                digits.append(int(digit))
                ten=ten//2
            reverse=list(reversed(digits))
            for index2 in range(len(reverse)):
                result=result+str(reverse[index2])
        print(INPUT+" corresponds to binary number",result)
        saved("the reply from function 19", "Decimal:"+str(INPUT)+" "+"Binary:"+str(result))
        history("19")
    # Calculate permutations and combinations
    if a == "20":
        reminder("Calculate Permutations and Combinations")
        import math
        mode = input("Select mode (1 for permutation nPr, 2 for combination nCr): ")
        try:
            n = int(input("Enter positive integer n: "))
            r = int(input("Enter positive integer r (r ≤ n): "))
            if n < 0 or r < 0 or r > n:
                print("Invalid input!")
                history("20*[error]")
            else:
                if mode == "1":
                    # Calculate permutation nPr = n! / (n-r)!
                    result = factorial(n) // factorial(n - r)
                    print(str(n)+"P"+str(r)+"=",result)
                    saved("the reply from function 20[nPr]", str(n)+"P"+str(r)+"="+str(result))
                    history("20[nPr]*")
                elif mode == "2":
                    # Calculate combination nCr = n! / (r!(n-r)!)
                    result = factorial(n) // (factorial(r) * factorial(n - r))
                    print(str(n)+"C"+str(r)+"=",result)
                    saved("the reply from function 20[nCr]",str(n)+"C"+str(r)+"="+str(result))
                    history("20[nCr]*")
                else:
                    print("Invalid mode!")
                    history("20*[invalid]")
        except ValueError:
            print("Error: Please enter valid integers!")
            history("20*[invalid_input]")
    #Calculate trigonometric function values
    if a=="21":
        reminder("Calculate Trigonometric Function Values")
        print("Please enter the angle to evaluate (in fractional form of pi coefficient in radians, e.g., for 360 degrees enter numerator 2, denominator 1)")
        IN=int(input("Enter numerator"))
        IN2=int(input("Enter denominator"))
        MODE=input("Select calculation mode (1 for sin, 2 for cos, 3 for tan)")
        Precision=int(input("Enter number of expansion terms (larger is more accurate)"))
        if MODE=="1":
            if IN==0:
                answer="0"
            else:
                answer=tri_function(IN,IN2,MODE,Precision)
            print("sin"+str(IN)+"/"+str(IN2)+"pi"+"="+answer)
            saved("the reply from function 21","sin"+str(IN)+"/"+str(IN2)+"pi"+"="+answer)
            history("21[1]")
        if MODE=="2":
            if IN==0:
                answer="1"
            else:
                answer=tri_function(IN,IN2,MODE,Precision)
            print("cos"+str(IN)+"/"+str(IN2)+"pi"+"="+answer)
            saved("the reply from function 21","cos"+str(IN)+"/"+str(IN2)+"pi"+"="+answer)
            history("21[2]")
        if MODE=="3":
            if IN==0:
                answer="0"
            else:
                answer=answer=tri_function(IN,IN2,MODE,Precision)
            print("tan"+str(IN)+"/"+str(IN2)+"pi"+"="+answer)
            saved("the reply from function 21","tan"+str(IN)+"/"+str(IN2)+"pi"+"="+answer)
            history("21[3]")
    #Radian-degree conversion
    if a=="22":
        reminder("Radian-Degree Conversion")
        MODE=input("Select mode (1 for degree to radian, 2 for radian to degree)")
        if MODE=="1":
            INPUT=input("Enter degree value")
            k=float(INPUT)/180
            print(INPUT+"°"+"="+str(k)+"pi")
            saved("the reply from function 22",INPUT+"°"+"="+str(k)+"pi")
            history("22[1]")
        if MODE=="2":
            print("Enter the coefficient of pi in radians, e.g., for pi/2 enter numerator 1, denominator 2")
            INPUT=int(input("Enter numerator"))
            INPUT2=int(input("Enter denominator"))
            INPUT3=INPUT/INPUT2
            k=INPUT3*180
            print(str(INPUT)+"/"+str(INPUT2)+"pi"+"="+str(k)+"°")
            saved("the reply from function 22",str(INPUT)+"/"+str(INPUT2)+"pi"+"="+str(k)+"°")
            history("22[2]")
    #Prime number check
    if a=="23":
        reminder("Prime Number Check")
        num = int(input("Enter positive integer to check:"))
        def prime_check(num):
            res=""
            if num == 1:
                res = "1"
            else:
                factors = prime_factor(num)
                if len(factors) == 1:
                    res = "prime number" 
                else: 
                    res = "composite number"
            return res
        resu=prime_check(num)
        if resu=="1":
            print("1 is neither prime nor composite")
            saved("the reply from function 23",str(num)+":"+"neither a prime number nor a composite number")          
        if resu=="prime number":
            print(str(num)+" is a prime number")
            saved("the reply from function 23",str(num)+":"+"prime number")
        if resu=="composite number":
            print(str(num)+" is a composite number")
            saved("the reply from function 23",str(num)+":"+"composite number")
        history("23")
#Vector magnitude calculation
    if a=="24":
        reminder("Vector Magnitude Calculation")
        inp=input("Enter x")
        inp2=input("Enter y")
        answer1=(decimal.Decimal(inp)**2)+(decimal.Decimal(inp2)**2)
        answerf=Squareroot(answer1,1000)
        print("Current vector magnitude is"+str(answerf))
        saved("the reply from function 24","("+str(inp)+","+str(inp2)+")"+"=>"+str(answerf))
        history("24")
#Calculate area of any triangle
    if a=="25":
        reminder("Calculate Area of Any Triangle")
        Mode=input("Select calculation method (1 for three sides, 2 for base-height):")
        if Mode=="1":
            L1=input("Enter first side length of triangle")
            L2=input("Enter second side length of triangle")
            L3=input("Enter third side length of triangle")
            ACC=input("Enter precision (recommended 100)")
            try:
                a=decimal.Decimal(L1)
                b=decimal.Decimal(L2)
                c=decimal.Decimal(L3)
            except:
                print("Input error")
                history("25[error]")
                continue
            if a+b<=c or a+c<=b or b+c<=a:
                print("The side lengths you entered cannot form a triangle")
                history("25[invalid]")
                continue
            else:
                p=decimal.Decimal((a+b+c)/2)
                S1=p*(p-a)*(p-b)*(p-c)
                S=Squareroot(S1,int(ACC))
                print("Triangle area is"+str(S))
                saved("the reply from function 25[1]",str(S))
                history("25[1]")
        if Mode=="2":
            L=input("Enter base length of triangle")
            H=input("Enter height of triangle")
            Answer=decimal.Decimal(L)*decimal.Decimal(H)/2
            print("Triangle area is"+str(Answer))
            saved("the reply from function 25[2]",str(Answer))
            history("25[2]")
    #Vector dot product
    if a=="26":
        reminder("Vector Dot Product")
        Input1=input("Enter first magnitude")
        Input2=input("Enter second magnitude")
        Angle1=input("Enter numerator (numerator of pi coefficient in radians, e.g., 2 for 180 degrees)")
        Angle2=input("Enter denominator (denominator of pi coefficient in radians, e.g., 1 for 180 degrees)")
        Pre=input("Enter precision")
        Answer=float(Input1)*float(Input2)*float(tri_function(float(Angle1),float(Angle2),"2",int(Pre)))
        print(Answer)
        saved("the reply from function 26",str(Answer))
        history("26")
    #Decimal to hexadecimal
    if a=="27":
        reminder("Decimal to Hexadecimal")
        INPUT=input("Enter decimal number to convert")
        def decimal_to_hex(n):
            hex_digits = "0123456789ABCDEF"
            if n == 0:
                return "0"
            hex_str = ""
            while n > 0:
                hex_str = hex_digits[n % 16] + hex_str
                n = n // 16
            return hex_str
        Answer=decimal_to_hex(int(INPUT))
        print(INPUT+" corresponds to hexadecimal number"+str(Answer))
        saved("the reply from function 27",INPUT+" "+"=>"+" "+str(Answer))
        history("27")
    #Calculate rational roots of integer coefficient polynomial
    if a=="28":
        reminder("Calculate Rational Roots of Integer Coefficient Polynomial")
        from fractions import Fraction
        print("This program calculates solutions for equations of the form xxx=0 and is not suitable for equations with constant term 0. If constant term is 0, please reduce the degree yourself until you get a non-zero constant term and then use this program to calculate")
        degree=int(input("Enter the degree of the polynomial to solve"))
        coefficients=[]
        roots=[]
        while True:
            coefficient=input("Enter coefficients in order, from highest degree to constant term (enter 0 if term doesn't exist), enter f when finished")
            if coefficient=="f":
                break
            else:
                int_coefficient=int(coefficient)
                coefficients.append(int_coefficient)
        if len(coefficients) != degree+1:
            print("Coefficient count error!")
            history("28[error]")
            continue
        leading_coefficient=coefficients[0]
        constant_term=coefficients[len(coefficients)-1]
        def get_all_factors(original_number):
            """Get all factors of a number"""
            n=original_number
            factors = []
            if n<0:
                    n=-n
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    factors.append(i)
                    if i != n // i:  # Avoid adding square root twice
                        factors.append(n // i)
            return sorted(factors)
        
        def check_solution(possible_solution):
            global degree,coefficients
            sum=0
            index=0
            for power in range(degree,-1,-1):
                result=coefficients[index]*(possible_solution**power)
                sum+=result
                index+=1
            if int(sum)==0:
                return True
            else:
                return False

        leading_coefficient_factors=get_all_factors(leading_coefficient)
        constant_term_factors=get_all_factors(constant_term)
        for lcf in leading_coefficient_factors:
            for ctf in constant_term_factors:
                possible_solution=Fraction(ctf,lcf)
                if check_solution(possible_solution):
                    roots.append(possible_solution)
                if check_solution(-possible_solution):
                    roots.append(-possible_solution)
        print("All rational solutions of the equation you provided are",roots)
        saved("the reply from function 28",f"highest_degree:{degree},coefficients{coefficients},rational_roots{roots}")
        history("28") 
    #Calculate numerical integration
    if a=="29":
        def function_calculation(expression,x):
            safe_symbol_dict={'math': math, 'sin': math.sin, 'cos': math.cos, 
                        'tan': math.tan, 'exp': math.exp, 'log': math.log,
                        'sqrt': math.sqrt, 'pi': math.pi, 'e': math.e}
            safe_symbol_dict["x"]=x
            return eval(expression,None,safe_symbol_dict)
            
        print("Enter function expression, use x as variable (can include constants and specific functions, enter cons to view all supported scientific constants, enter func to view all supported functions)")
        print("Examples: x**2 + 2*x + 1, math.sin(x), math.exp(x)")

        while True:
            func_str = input("Function f(x) = ")
            if func_str=="cons":
                print("This program supports the following scientific constants, can be directly entered in expressions:")
                print("pi: Pi, e: Natural constant")
            elif func_str=="func":
                print("This program supports the following specific functions, can be directly entered in expressions:")
                print("math: Python's math library, can be called directly via methods like math.sin(x)")
                print("sin: Sine function, cos: Cosine function, tan: Tangent function")
                print("exp: Natural exponential function e^x")
                print("sqrt: Square root function")
                print("log: Natural logarithm function ln(x), Note: log(x,{base}) can specify logarithm with any base")
            else:
                break
        a = float(input("Integration lower limit a = "))
        b = float(input("Integration upper limit b = "))
        n = int(input("Number of partition intervals n = "))
        if n <=0 or n% 1 != 0:
            print("Partition count must be positive integer")
            history("29[error]")
            continue
        else:
            interval_length=b-a
            step=interval_length/n
            sampling_points=[]
            integral_result=0
            for index in range(n):
                sampling_points.append(function_calculation(func_str,a+step*index))
            for sp in sampling_points:
                cache=sp*step
                integral_result=integral_result+cache
        print("Numerical integration result", f"∫[{a},{b}] {func_str} dx = {integral_result}")
        saved("the reply from function 29", f"∫[{a},{b}] {func_str} dx = {integral_result}")
        history("29")
#Read calculation results
    if a=="rr":
        with open("result.json","r") as gu:
            eue=json.load(gu)
            print(eue)
#Clear calculation results
    if a=="cr":
        with open("result.json","w") as gu:
            eue=json.dump("*",gu)
        print("Cleared")
#Terminate run
    if a =="exit":
        history("turn off")
        break
#Read operation history
    if a=="rh":
        with open("history.json","r") as yy:
            o1=json.load(yy)
        print(o1)
#Clear operation history
    if a=="ch":
        with open("history.json","w") as yy:
            json.dump("prepare done ",yy)
        print("Cleared")
#Export operation history
    if a=="eh":
        export_file("history")
        print("Operation history exported to history.txt")
#Export historical calculation results
    if a=="er":
        export_file("result")
        print("Historical calculation results exported to result.txt")
#Clear screen
    if a=="cs":
        print("\033c", end="")
#View version
    if a=="version":
        print("You are currently using "+Version+" by QU QI")
#Doubling calculation (hidden)
    if a=="benchmark":   
        e = int(input("Enter value to double"))
        f = int(input("Enter number of doublings"))
        j = 0
        h = 0
        for i in range(f):
            j= e*2
            h += 1
            e = j
            print("Current value is", j, ", this is the", h, "time doubling.")
            w=j
        saved("the reply from function benchmark",w)
        history("894*")
print("Goodbye")
print("Good-bye!")