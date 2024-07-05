with open("confidential.txt","r") as file:
    for line in file:
        if line == "This is confidential information!":
            print("There is no change")
        else:
            print("There is a change!")
