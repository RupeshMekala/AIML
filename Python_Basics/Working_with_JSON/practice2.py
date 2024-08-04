with open("///Working_with_JSON//json.txt", "r") as j:

    s = j.read()
    print(s)

    import json
    x = json.loads(s) # to read a JSON string json needs to be imported and json.loads() is to be used
    print(x['tom'])
    print(x['tom']['phone'])

    for person in x:
        print(x[person])
