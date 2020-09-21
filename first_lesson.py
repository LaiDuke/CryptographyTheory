system_select = ""
textIn = ""
while 1:
    print("Would you like to continue?")
    system_select = input()
    if system_select == "Y":
        textIn = input()
        for t in textIn:
            t = t.__mod__("hjjijijij")
            print(t)
    else: break
