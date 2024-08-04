with open("C://Users//rupes//Downloads//stocks.csv","r") as s ,open("///Reading_Writing_Files//stocksout.csv", "w") as p:

    next(s)   # it will skip the first line of s(which are headings)
    for line in s:
        tokens = line.split(",")
        print(type(tokens))
        stock = tokens[0]
        price = float(tokens[1])
        eps = float(tokens[2])
        bv = float(tokens[3])
        pe_ratio = price / eps
        pb_ratio = price / bv
        p.write(f"{stock},{pe_ratio},{pb_ratio}\n")















