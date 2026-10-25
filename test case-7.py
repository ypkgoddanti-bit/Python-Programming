#36.Repeated Word and Phrase Detection
sentence = input("Enter sentence: ")
words = sentence.lower().split()

for word in words:
    if words.count(word) > 1:
        print(word, "appears", words.count(word), "times")
