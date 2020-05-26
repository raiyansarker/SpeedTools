import time

# Acceleration Function
def a():
    method = ["(1) First Momentum, Last Momentum, Time", "(2) First Momentum, Last Momentum, Distance", "(3) First Momentum, Time, Distance"]

    for x in method:
        time.sleep(0.3)
        print("\033[1;34;49m"+x)

    print("\033[1;31;49mRemember. These have to be number in specified unit\n")
    time.sleep(0.3)
    try:
        mAnswer = float(input("What do you have? - "))

        if mAnswer == 1:
            try:
                u = float(input("Enter first momentum(m/s) - "))
                v = float(input("Enter last momentum(m/s) - "))
                t = float(input("Enter time(s) - "))

                temp1 = v - u
                temp2 = temp1 / t
                answer = temp2

                return answer
            except ValueError:
                print("This is not a number")
        elif mAnswer == 2:
            try:
                u = float(input("Enter first momentum(m/s) - "))
                v = float(input("Enter last momentum(m/s) - "))
                s = float(input("Enter distance(m) - "))

                temp1 = v*v - u*u
                temp2 = 2*s                
                temp3 = temp1 / temp2
                answer = temp3

                return temp2
            except ValueError:
                print("This is not a number")
        elif mAnswer == 3:
            try:
                u = float(input("Enter first momentum(m/s) - "))
                t = float(input("Enter time(s) - "))
                s = float(input("Enter distance(m) - "))

                temp1 = s - u*t
                temp2 = 2 * temp1
                temp3 = t*t
                temp4 = temp2 / temp3
                answer = temp4

                return answer
            except ValueError:
                print("This is not a number")
        else:
            print("Something went wrong")
    except ValueError:
        print("This is not a number")

# Time Function
def t():
    method = ["(1) First Momentum, Last Momentum, Acceleration", "(2) First Momentum, Last Momentum, Distance","(3) First Momentum, Acceleration, Distance", "(4) Distance, Last Momentum"]

    for x in method:
        time.sleep(0.3)
        print("\033[1;34;49m"+x)

    print("\033[1;31;49mRemember. These have to be number in specified unit\n")
    time.sleep(0.3)
    try:
        mAnswer = float(input("What do you have? - "))

        if mAnswer == 1:
            try:
                u = float(input("Enter first momentum(m/s) - "))
                v = float(input("Enter last momentum(m/s) - "))
                a = float(input("Enter acceleration(m/s\u00b2) - "))

                temp1 = v - u
                temp2 = temp1 / a
                answer = temp2
                
                return answer
            except ValueError:
                print("This is not a number")
        elif mAnswer == 2:
            try:
                u = float(input("Enter first momentum(m/s) - "))
                v = float(input("Enter last momentum(m/s) - "))
                s = float(input("Enter distance(m) - "))

                temp1 = 2 * s
                temp2 = v + u
                temp3 = temp1 / temp2
                answer = temp1

                return answer
            except ValueError:
                print("This is not a number")
        elif mAnswer == 3:
            try:
                u = float(input("Enter first momentum(m/s) - "))
                a = float(input("Enter acceleration(m/s\u00b2) - "))
                s = float(input("Enter distance(m) - "))

                temp1 = a / 2
                temp2 = u + temp1
                temp3 = s / temp2
                temp4 = temp3 ** 0.5
                answer = temp4

                return answer
            except ValueError:
                print("Something went wrong")
        elif mAnswer == 4:
            try:
                v = float(input("Enter momentum(m/s) - "))
                s = float(input("Enter distance(m) - "))

                temp1 = s / v
                answer = temp1

                return answer
            except ValueError:
                print("This is not a number")
        else:
            print("Something went wrong")
    except ValueError:
        print("This is not a number")

# Distance Function
def d():
    method = ["(1) First Momentum, Last Momentum, Acceleration", "(2) First Momentum, Last Momentum, Time", "(3) First Momentum, Time, Acceleration", "(4) Momentum, Time"]
    for x in method:
        time.sleep(0.3)
        print("\033[1;34;49m"+x)

    print("\033[1;31;49mRemember. These have to be number in specified unit\n")
    time.sleep(0.3)

    try:
        mAnswer = float(input("What do you have? - "))

        if mAnswer == 1:
            try:
                u = float(input("Enter first momentum(m/s) - "))
                v = float(input("Enter last momentum(m/s) - "))
                a = float(input("Enter acceleration(m/s\u00b2) - "))

                temp1 = v*v -u*u
                temp2 = 2 * a
                temp3 = temp1 / temp2
                answer = temp3

                return answer
            except ValueError:
                print("Something went wrong")
        
        elif mAnswer == 2:
            try:
                u = float(input("Enter first momentum(m/s) - "))
                v = float(input("Enter last momentum(m/s) - "))
                s = float(input("Enter distance(m) - "))

                temp1 = 2 * s
                temp2 = v + u
                temp3 = temp1 / temp2
                answer = temp3

                return answer
            except ValueError:
                print("Something went wrong")
        
        elif mAnswer == 3:
            try:
                u = float(input("Enter first momentum(m/s) - "))
                a = float(input("Enter acceleration(m/s\u00b2) - "))
                t = float(input("Enter time(s) - "))

                temp1 = u * t
                temp2 = t * t
                temp3 = a * temp2
                temp4 = temp3 / 2
                temp5 = temp1 + temp4
                answer = temp5

                return answer
            except ValueError:
                print("Something went wrong")
        elif mAnswer == 4:
            try:
                v = float(input("Enter momentum(m/s) - "))
                t = float(input("Enter time(s) - "))

                temp1 = v * t
                answer = temp1

                return answer
            except ValueError:
                print("Something went wrong")
        else:
            print("Something went wrong")
    except ValueError:
        print("Something went wrong")

# First Momentum Function
def u():
    method = ["(1) Last Momentum, Acceleration, Time", "(2) Last Momentum, Acceleration, Distance", "(3) Last Momentum, Distance, Time", "(4) Distance, Acceleration, Time"]
    for x in method:
        time.sleep(0.3)
        print("\033[1;34;49m"+x)

    print("\033[1;31;49mRemember. These have to be number in specified unit\n")
    time.sleep(0.3)

    try:
        mAnswer = float(input("What do you have? - "))

        if mAnswer == 1:
            try:
                v = float(input("Enter last momentum(m/s) - "))
                t = float(input("Enter time(s) - "))
                a = float(input("Enter acceleration(m/s\u00b2) - "))

                temp1 = a * t
                temp2 = v - temp1
                answer = temp2

                return answer
            except ValueError:
                print("Something went wrong")
        if mAnswer == 2:
            try:
                v = float(input("Enter last momentum(m/s) - "))
                a = float(input("Enter acceleration(m/s\u00b2) - "))
                s = float(input("Enter distance(m) - "))

                temp1 = v * v
                temp2 = 2 * a * s
                temp3 = temp1 - temp2
                temp4 = temp3 ** 0.5
                answer = temp4

                return answer
            except ValueError:
                print("Something went wrong")
        if mAnswer == 3:
            try:
                v = float(input("Enter last momentum(m/s) - "))
                s = float(input("Enter distance(m) - "))
                t = float(input("Enter time(s) - "))

                temp1 = 2 * s
                temp2 = temp1 / t
                temp3 = temp2 - v
                answer = temp3

                return answer
            except ValueError:
                print("Something went wrong")
        if mAnswer == 4:
            try:
                s = float(input("Enter distance(m) - "))
                t = float(input("Enter time(s) - "))
                a = float(input("Enter acceleration(m/s\u00b2) - "))

                temp1 = t * t
                temp2 = a * temp1
                temp3 = temp2 / 2
                temp4 = s - temp3
                temp5 = temp4 / t
                answer = temp5

                return answer
            except ValueError:
                print("Something went wrong")
        else:
            print("Something went wrong")
    except:
        print("Something went wrong")

# Last Mementum Function
def v():
    method = ["(1) First Momentum, Acceleration, Time", "(2) First Momentum, Acceleration, Distance", "(3) First Momentum, Distance, Time", "(4) Distance, Time"]
    for x in method:
        time.sleep(0.3)
        print("\033[1;34;49m"+x)

    print("\033[1;31;49mRemember. These have to be number in specified unit\n")
    time.sleep(0.3)

    try:
        mAnswer = float(input("What do you have? - "))

        if mAnswer == 1:
            try:
                u = float(input("Enter first momentum(m/s) - "))
                t = float(input("Enter time(s) - "))
                a = float(input("Enter acceleration(m/s\u00b2) - "))

                temp1 = a * t
                temp2 = u + temp1
                answer = temp2

                return answer
            except ValueError:
                print("Something went wrong")
        if mAnswer == 2:
            try:
                u = float(input("Enter first momentum(m/s) - "))
                s = float(input("Enter distance(m) - "))
                a = float(input("Enter acceleration(m/s\u00b2) - "))

                temp1 = u * u
                temp2 = 2 * a * s
                temp3 = temp1 + temp2
                temp4 = temp3 ** 0.5
                answer = temp4

                return answer
            except ValueError:
                print("Something went wrong")
        if mAnswer == 3:
            try:
                u = float(input("Enter first momentum(m/s) - "))
                s = float(input("Enter distance(m) - "))
                t = float(input("Enter time(s) - "))

                temp1 = 2 * s
                temp2 = temp1 / t
                temp3 = temp2 - u
                answer = temp3

                return answer
            except ValueError:
                print("Something went wrong")
        if mAnswer == 4:
            try:
                s = float(input("Enter distance(m) - "))
                t = float(input("Enter time(s) - "))
                
                temp1 = s / t
                answer = temp1

                return answer
            except ValueError:
                print("Something went wrong")
        else:
            print("Something went wrong")
    except ValueError:
        print("Something went wrong")