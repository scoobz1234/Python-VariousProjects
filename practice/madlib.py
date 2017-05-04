from time import sleep
print ("Do you want to play a madlib?")

while True:
    sleep (1)
    print ("Adjective:")
    Adjective1 = input(">>>")
    print ("Noun")
    Noun1 = input(">>>")
    print ("Animal")
    Animal = input(">>>")
    print ("Noise")
    Noise1 = input(">>>")
    sleep (1)
    print ("...")
    sleep (1)
    print ("Consulting the cosmos...")
    sleep (1)
    madlibLine1 = Adjective1 + " Macdonald had a " + Noun1 + ", E-I-E-I-O"
    madlibLine2 = "and on that " + Noun1 + " he had an " + Animal + ", E-I-E-I-O"
    madlibLine3 = "With a " + Noise1 + " " + Noise1 + " here"
    madlibLine4 = "and a " + Noise1 + " " + Noise1 + " there,"
    madlibLine5 = "here a " + Noise1 + " there a " + Noise1 + ","
    madlibLine6 = "everywhere a " + Noise1 + Noise1 + ","
    madlibLine7 = Adjective1 + " Macdonald had a " + Noun1 + ", E-I-E-I-O"
    print (madlibLine1)
    sleep (1)
    print (madlibLine2)
    sleep (1)
    print (madlibLine3)
    sleep (1)
    print (madlibLine4)
    sleep (1)
    print (madlibLine5)
    sleep (1)
    print (madlibLine6)
    sleep (1)
    print (madlibLine7)
    sleep (4)
    print ("Want to play again?")
    Answer = input (">>>")
    if Answer == "no" or "No" or "N" or "n":
        break
