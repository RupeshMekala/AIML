with open("///Reading_Writing_Files//poem.txt", "r") as p:

    word_count = {}
    for lines in p:
        word = lines.split(" ")
        for i in word:
            if i in word_count:
                word_count[i] += 1
            else:
                word_count[i] = 1
    print(word_count)
    maximum_repeated_word = ""
    times_repeated = -1
    for word in word_count:
        if word_count[word] > times_repeated:
            times_repeated = word_count[word]

    print(times_repeated)
    print("The maximum repeated words : ")
    for word in word_count:
        if word_count[word] == times_repeated:
            print(word)







