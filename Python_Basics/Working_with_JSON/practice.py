book = {}
book['tom'] = {

    'name': 'Rupesh',
    'address': '1 Red street NY',
    'phone': 23449234
}

book['lob'] = {

    'name': 'Lob',
    'address': '1 Green street NY',
    'phone': 248345334
}
print(book)

import json
s = json.dumps(book) # json.dump's' converts book into JSON string
print(s)
with open("///Working_with_JSON//json.txt", "w") as j:

    j.write(s)  # s is added to j which is json.txt
