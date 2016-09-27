#Program to calculate volume or surrface area of different sbjects

import math

print "Welcome to the wonderful SUVAT calculator.\n"
"""
s = distance
u = initial velocity
v = final velocity
a = acceleration
t = time
"""

def Start():
    print "Welcome to the wonderful SUVAT calculator.\n"
    print "Which variables do you have? : "
    choice = raw_input("1 - Displacement - (u,t,a)\n2 - Displacement - (u,v,t)\n3 - Final Velocity - (u,a,t)\n4 - Final Velocity - (u,a,s)\n0 - Close program.\n\n")
    Dec(choice)

def Savfile(output):
    leave = raw_input("Would you like to [s]ave or to [c]lose>  ")

    if leave == "s" or "S":
        #file open
        file = open("calculations.txt", "a")
        #write variables into file in text
        file.write(output + "\n\n")
        file.close()

        end = raw_input("Would you like to [r]estart or press any other key to exit? > ")
        if end == "r":
            Start()
        else:
            exit()

    elif leave == "c" or "C":

        Start()

def Dec(choice):
    if choice == "1":
        u = float(raw_input(" u = ?"))
        t = float(raw_input(" t = ?"))
        a = float(raw_input(" a = ?"))
        S1(u, t, a)
    elif choice == "2":
        u = float(raw_input(" u = ?"))
        v = float(raw_input(" v = ?"))
        t = float(raw_input(" t = ?"))
        S2(u, v, t)
    elif choice =="3":
        u = float(raw_input(" u = ?"))
        t = float(raw_input(" t = ?"))
        a = float(raw_input(" a = ?"))
        V1(u, a, t)
    elif choice =="4":
        s = float(raw_input(" s = ?"))
        u = float(raw_input(" u = ?"))
        a = float(raw_input(" a = ?"))
        V2(u, a, s)
    elif choice =="0":
        exit()
    else:
        print "Please make an available choice."


def S1(u, t, a):
    displacement = (u * t) + ((a * (t ** t)) / 2)
    #print "\nThe displacement is:\n"
    output = "\nThe displacement is:\n" + str(displacement) + " meters.\n"
    print output

    Savfile(output)


def S2(u, v, t):
    displacement = ((u + v) / 2) * t
    #print "\nThe displacement is:\n"
    output = "\nThe displacement is:\n" + str(displacement) + " meters.\n"
    print output

    Savfile(output)


def V1(u, a, t):
    finvel = u + (a * t)
    #print "\nThe velocity is:\n"
    output = "\nThe velocity is:\n" + str(finvel) + " meters per second.\n"
    print output

    Savfile(output)


def V2(u, a, s):
    finvel = math.sqrt((u * u) + (2 * a * s))
    #print "\nThe velocity is: \n"
    output = "\nThe velocity is:\n" + str(finvel) + " meters per second.\n"
    print output

    Savfile(output)

Start()
