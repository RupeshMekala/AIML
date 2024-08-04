
info = {"china": 143, "india": 136, "usa": 32, "pakistan": 21}
feedback = input("'Print','Add','Remove','Query' : ")

if feedback == "print":
    for key in info:
        print(key, " ==> ", info[key])

elif feedback == "add":
    name1 = input("Enter the country name you would like to add : ")
    check1 = name1 in info
    if check1:
        print("The country already exists")

    elif not check1:
        pop1 = input("Enter the population of the country : ")
        info[name1] = pop1
        for key in info:
            print(key, " ==> ", info[key])


elif feedback == "remove":
    namex = input("Enter the country name you would like to remove : ")
    check2 = namex in info
    if not check2:
        print("The country doesn't exist")

    elif check2:
        del info[namex]
        for key in info:
            print(key, " ==> ", info[key])

elif feedback == "query":
    name2 = input("Which country do you want to query: ")
    check3 = name2 in info
    if not check3:
        print("The country doesn't exist")

    elif check3:
        print(info[name2])







